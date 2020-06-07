def matrix_cov(samples):
    nsamples = samples.to_numpy()
    mus = np.mean(nsamples, axis=0)
    diffs = nsamples - mus
    total = np.zeros((2, 2))
    for diff in diffs:
        t = np.array([diff])
        total += np.matmul(t.T, t)
    return (1/9)*total