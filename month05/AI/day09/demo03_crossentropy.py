"""
交叉商损失函数
"""
import numpy as np
import tensorflow as tf

# 5个样本三分类问题，且一个样本可以同时拥有多类
y = np.array([[1, 0, 0], [1, 0, 0]], dtype='f8')
y_ = np.array([[12, 3, 2], [3, 10, 1]], dtype='f8')


with tf.Session() as sess:
    # 计算sigmoid交叉熵
    loss = tf.nn.sigmoid_cross_entropy_with_logits(
            labels=y, logits=y_)
    error = sess.run(loss)
    print(error)
    print(error.mean(axis=1))

    # 计算softmax交叉熵
    loss = tf.nn.softmax_cross_entropy_with_logits(
            labels=y, logits=y_)
    error = sess.run(loss)
    print(error)
    print(error.mean())
