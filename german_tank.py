import numpy as np
from scipy.stats import randint
import matplotlib.pyplot as plt

def double_mean_estimator(sample):
    return sample.mean() * 2

def freq_estimator(sample):
    m = sample.max()
    k = len(sample)
    return m + (m/k) - 1

def bayes_estimator(sample):
    m = sample.max()
    k = len(sample)
    return m + (m * np.log(2)) / (k - 1)

def german():
    tank_sample = np.random.choice(5000, 50, replace=False) + 1
    return (double_mean_estimator(tank_sample),
        freq_estimator(tank_sample), 
        bayes_estimator(tank_sample))

samples = np.array([german() for _ in range(100)])

fig, axes = plt.subplots(3, 1, sharex=True, figsize=(10, 10))
axes[0].hist(samples[:, 0])
axes[0].title.set_text('double the mean')
axes[1].hist(samples[:, 1])
axes[1].title.set_text('frequentist MVUE')
axes[2].hist(samples[:, 2])
axes[2].title.set_text('bayesian median posterior')
plt.savefig('plots/german_estimators.png')
plt.close()
