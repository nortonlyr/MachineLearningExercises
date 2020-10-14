import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

np.random.seed(12)
num_observations = 5000

# 高斯分佈數列
x1 = np.random.multivariate_normal([0, 0], [[2, 0.75], [0.75, 2]], num_observations)
x2 = np.random.multivariate_normal([1, 4], [[1, 0.75], [0.75, 1]], num_observations)
x3 = np.random.multivariate_normal([2, 8], [[0, 0.75], [0.75, 0]], num_observations)

simulated_separableish_features = np.vstack((x1, x2, x3)).astype(np.float32)
simulated_labels = np.hstack((np.zeros(num_observations),
                np.ones(num_observations), np.ones(num_observations) + 1))


plt.figure(figsize=(12,8))
plt.scatter(simulated_separableish_features[:, 0], simulated_separableish_features[:, 1],
            c = simulated_labels, alpha = .4)