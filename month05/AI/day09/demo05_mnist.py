import tensorflow as tf
import numpy as np
import pandas as pd

# 1.加载数据集
train = pd.read_csv("./mnist/train.csv")
test = pd.read_csv("./mnist/test.csv")

# 2.提取图片数据
x_train = train.iloc[:, 1:].values
x_train = x_train.astype(np.float)
x_test = test.iloc[:, 1:].values
x_test = x_test.astype(np.float)

# 3.给到的图片灰度值在0-255，这里将图片的信息控制在0~1之间
x_train = np.multiply(x_train, 1.0 / 255)
x_test = np.multiply(x_test, 1.0 / 255)

# 4.计算图片的长和高
image_size = x_train.shape[1]
image_width = image_height = np.ceil(np.sqrt(image_size)).astype(np.uint8)

# 5.把数据集的标签提取出来
labels_train = train.iloc[:, 0].values
label_count = np.unique(labels_train).shape[0]


# 将label数据转换为 one-hot 向量
def dense_to_one_hot(labels_dense, num_classes):
    num_labels = labels_dense.shape[0]  # 42000
    print(num_labels)
    index_offset = np.arange(num_labels) * num_classes  # (420000,1)
    print(index_offset.shape)
    print(labels_dense)
    labels_one_hot = np.zeros((num_labels, num_classes))  # (42000, 10)
    print(labels_one_hot.shape)
    # .flat 函数将 42000 * 10 的矩阵拉伸为 420000 的一维矩阵，但原来矩阵的维度不变
    labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1  #
    return labels_one_hot


# 6.对label进行one-hot处理
labels = dense_to_one_hot(labels_train, label_count)

# 7.设置批次大小，求得批次量
batch_size = 128
n_batch = int(len(x_train) / batch_size)

# 8.定义两个placeholder
x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])


# 9.定义几个处理函数
def weight_variable(shape):
    initial = tf.random_normal(shape, stddev=0.1)
    return tf.Variable(initial)


# 生成偏置
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


# 卷积层
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


# 池化层
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


# 10.将输入转换为4d张量
x_image = tf.reshape(x, [-1, 28, 28, 1])

# 11.第一层使用32个过滤器计算32个特征，和偏置项
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

# 12.对数据进行第一层卷积和第一层池化
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

# 13.第二层卷积使用64个过滤器计算64个特征，设置偏置项
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

# 14.对数据进行第二层卷积和第二层池化
h_conv2 = tf.nn.relu(conv2d(h_conv1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

# 15.将池化后的数据拉伸
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])

# 16.构建第一层全连接层
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# 17.使用dropout操作
keep_prob = tf.placeholder("float")
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 18.构建第二层全连接层
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.matmul(h_fc1, W_fc2) + b_fc2
predictions = tf.nn.softmax(y_conv)

# 19.创建损失函数
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))

# 20.使用梯度下降优化参数
train_step_1 = tf.train.AdadeltaOptimizer(0.1).minimize(loss)

# 21.计算准确度
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 22.设置保存模型的文件名参数
global_step = tf.Variable(0, name='global_step', trainable=False)

saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(30):
        print("epoch", i + 1)
        for batch in range(n_batch):
            batch_x = x_train[batch * batch_size:(batch + 1) * batch_size]
            batch_y = labels[batch * batch_size:(batch + 1) * batch_size]
            if i % 100 == 0:
                train_accuracy = accuracy.eval(feed_dict={
                    x: batch_x, y_: batch_y})
                print("step %d, training accuracy %g" % (i, train_accuracy))
            sess.run(train_step_1, feed_dict={x: batch_x, y_: batch_y, keep_prob:0.5})

    saver.save(sess, 'ModelconvNN2/model.ckpt')
