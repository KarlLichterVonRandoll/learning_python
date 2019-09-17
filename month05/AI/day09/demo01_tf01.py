import tensorflow as tf

bias = tf.Variable(tf.zeros(200), name="biases")
w = tf.Variable(tf.random_normal((784, 200), stddev=0.35, mean=0, seed=1), name="weight")
print(bias)
print(w)

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(bias))
    print(sess.run(w))
