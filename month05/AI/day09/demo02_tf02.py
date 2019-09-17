import tensorflow as tf

with tf.Session() as sess:
    x = tf.placeholder(tf.float32, shape=(1, 2))
    y = x + x
    r = sess.run(y, feed_dict={x: [[0.5,0.6]]})
    print(r)

    a = tf.placeholder(tf.float32, shape=(None, 2))
    b = tf.reduce_sum(a, 0)
    r = sess.run(b, feed_dict={a: [[3.0, 4.0], [1.2, 1.3], [1.0, 2.0]]})
    print(r)
