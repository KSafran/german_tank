import numpy as np
from scipy.stats import randint
import matplotlib.pyplot as plt

n_tanks = 5000
true_tank_distribution = randint(0, n_tanks)

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

def german(ground_truth):
    tank_sample = ground_truth.rvs(50)
    return (double_mean_estimator(tank_sample),
        freq_estimator(tank_sample), 
        bayes_estimator(tank_sample))

samples = np.array([german(true_tank_distribution) for _ in range(100)])

fig, axes = plt.subplots(3, 1, sharex=True)
axes[0].hist(samples[:, 0])
axes[0].title.set_text('double the mean')
axes[1].hist(samples[:, 1])
axes[1].title.set_text('frequentist MVUE')
axes[2].hist(samples[:, 2])
axes[2].title.set_text('bayesian median posterior')
plt.show()
