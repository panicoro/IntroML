import numpy as np
from numpy.linalg import inv, det

def generate_discriminat(mu_i, sigma_i, priori_i):
    """
    It generates a discriminant function for 
    multivariate normal densities
    Params:
    * mu: the mean column vector from the distribution.
    * sigma: the covariance matrix.
    * priori: the prior probability for the state.
    """
    inv_sigma_i = inv(sigma_i)
    det_sigma_i = det(sigma_i)
    W_i = -0.5*inv_sigma_i
    w_i = inv_sigma_i.dot(mu_i)
    w_i0 = -0.5*mu_i.T.dot(inv_sigma_i).dot(mu_i) - 0.5*np.log(det_sigma_i) + np.log(priori_i)
    return lambda x: x.T.dot(W_i).dot(x) + w_i.T.dot(x) + w_i0


class ClasssifierBayesian(object):
    
    def __init__(self, mus, sigmas, probs):
        self.num_class = mus.shape[0]
        for k in range(self.num_class):
            discr = generate_discriminat(mus[k], sigmas[k], probs[k])
            name = 'g_' + str(k+1)
            setattr(self, name, (discr, k))
    
    def classify(self, x):
        evals = np.empty((self.num_class, 1))
        keys = list(classifier.__dict__.keys())
        keys.remove('num_class')
        for key in keys:
            discr = classifier.__dict__[key][0]
            _class = classifier.__dict__[key][1]
            evals[_class] = discr(x)
        return np.argmax(evals) + 1
    
    def predict(self, X):
        y_predict = np.apply_along_axis(self.classify, 1, X) 
        return y_predict

class ClassifierOneFeature(object):
    
    def __init__(self):
        pass
    
    def estimate(self, sample1, sample2):
        self.mu_1, self.mu_2 = np.mean(sample1), np.mean(sample2)
        self.std_1, self.std_2 = np.std(sample1, ddof=1), np.std(sample2, ddof=1)
    
    def classify(self, x):
        class_1 = np.log(self.std_1) + ((x-self.mu_1)**2)/(2*self.std_1**2)
        class_2 = np.log(self.std_2) + ((x-self.mu_2)**2)/(2*self.std_2**2)
        if class_1 < class_2:
            return 1
        else:
            return 2
    
    def predict(self, X):
        vclassify = np.vectorize(self.classify)
        y_predict = vclassify(X) 
        return y_predict