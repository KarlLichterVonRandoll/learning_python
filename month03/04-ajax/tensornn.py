import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

batch_size = 8

w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

x = tf.placeholder(tf.float32, shape=(None, 2), name='x_input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y_input')

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

y = tf.sigmoid(y)

cross_entropy = -tf.reduce_mean(
    y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0))
    + (1 - y_) * tf.log(tf.clip_by_value(1 - y, 1e-10, 1.0))
)

train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

rdm = np.random.RandomState(1)
data_size = 128
X = rdm.rand(data_size, 2)

Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

print(X)
print(Y)
