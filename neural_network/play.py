from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from neural_network.main import *
import numpy as np
import matplotlib.pyplot as plt
from neural_network.mnist import load_mnist

(X_train, t_train), (X_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

train_loss_list = []

iter_num = 100
train_size = X_train.shape[0]
batch_size = 100
learning_rate = 0.1

network = NeuralNet(input_size=784, hidden_size=50, output_size=10)

for i in range(iter_num):
    print("Iter {0}".format(i))
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = X_train[batch_mask]
    t_batch = t_train[batch_mask]

    grad = network.numerical_gradient(x_batch, t_batch)

    for key in ("W1", "b1", "W2", "b2"):
        network.params[key] -= learning_rate * grad[key]

    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)


plt.scatter(train_loss_list)
plt.show()
