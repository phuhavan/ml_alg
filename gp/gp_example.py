import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pylab as plt

np.random.seed(42)

def exponential_cov(x, y, params):
    return params[0] * np.exp( -0.5 * params[1] * np.subtract.outer(x, y)**2)

def conditional(x_new, x, y, params):
    B = exponential_cov(x_new, x, params)
    C = exponential_cov(x, x, params)
    A = exponential_cov(x_new, x_new, params)
    mu = np.linalg.inv(C).dot(B.T).T.dot(y)
    sigma = A - B.dot(np.linalg.inv(C).dot(B.T))
    return(mu.squeeze(), sigma.squeeze())

def predict(x, data, kernel, params, sigma, t):
    k = [kernel(x, y, params) for y in data]
    Sinv = np.linalg.inv(sigma)
    y_pred = np.dot(k, Sinv).dot(t)
    sigma_new = kernel(x, x, params) - np.dot(k, Sinv).dot(k)
    return y_pred, sigma_new

theta = [1, 10]
sig_0 = exponential_cov(0, 0, theta)
xpts = np.arange(-3, 3, step=0.01)
plt.figure()
plt.errorbar(xpts, np.zeros(len(xpts)), yerr=sig_0, capsize=0)
plt.ylim(-3, 3);
plt.show()

x = [1.]
y = [np.random.normal(scale=sig_0)]
y
sig_1 = exponential_cov(x, x, theta)

x_pred = np.linspace(-3, 3, 1000)
predictions = [predict(i, x, exponential_cov, theta, sig_1, y) for i in x_pred]
y_pred, sigmas = np.transpose(predictions)
plt.figure()
plt.errorbar(x_pred, y_pred, yerr=sigmas, capsize=0)
plt.plot(x, y, "ro")
plt.xlim(-3, 3); plt.ylim(-3, 3);
plt.show()


m, s = conditional([-0.7], x, y, theta)
y2 = np.random.normal(m, s)
y2

x.append(-0.7)
y.append(y2)

sig_2 = exponential_cov(x, x, theta)
predictions = [predict(i, x, exponential_cov, theta, sig_2, y) for i in x_pred]
y_pred, sigmas = np.transpose(predictions)
plt.errorbar(x_pred, y_pred, yerr=sigmas, capsize=0)
plt.plot(x, y, "ro")
plt.xlim(-3, 3); plt.ylim(-3, 3);
plt.show()
