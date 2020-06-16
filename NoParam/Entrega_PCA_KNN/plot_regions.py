from matplotlib.colors import ListedColormap
from sklearn.metrics import zero_one_loss
import matplotlib.pyplot as plt
import numpy as np

def plot_decision_regions(ax, X, y, classifier, xy_labels,
                          resolution=0.02):
    
    # setup marker generator and color map
    markers = ('$B$', '$M$')
    colors = ('red', 'blue', 'lightgreen')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    labels = ['B', 'M']
    
    # train the classifier and get the predictions
    y_predict = classifier.fit(X, y).predict(X)
    # plot the decision surface
    x1_min, x1_max = X.iloc[:, 0].min() - 1, X.iloc[:, 0].max() + 1
    x2_min, x2_max = X.iloc[:, 1].min() - 1, X.iloc[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution, dtype=np.float16),
                           np.arange(x2_min, x2_max, resolution, dtype=np.float16))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    ax.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    ax.set_xlim(xx1.min(), xx1.max())
    ax.set_ylim(xx2.min(), xx2.max())
    
    # plot examples by class
    for idx, cl in enumerate(np.unique(y)):
        ax.scatter(x=X[y == cl].iloc[:, 0],
                   y=X[y == cl].iloc[:, 1],
                   edgecolors=cmap(idx),
                   marker=markers[idx],
                   label=labels[idx])
        ax.set_xlabel(xy_labels[0])
        ax.set_ylabel(xy_labels[1])
    error_rate = round(zero_one_loss(y, y_predict), 3)
    title = 'K = ' + str(classifier.n_neighbors) + ' - ' + 'Error rate: ' + str(error_rate)
    ax.set_title(title)