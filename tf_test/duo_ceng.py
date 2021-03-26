import tensorflow as tf
import numpy as np


def add_layer(inputs, in_size, out_size, activate_function=None):
    weights = tf.Variable(tf.random.uniform([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    wx_plus_b = tf.matmul(inputs, weights) + biases
    if activate_function:
        outputs = activate_function(wx_plus_b)
    else:
        outputs = wx_plus_b
    return outputs

#
# x_data = np.random.uniform(-1, 1, [300, 1]).astype(np.float32)
# noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
# y_data = x_data * x_data - 0.5 + noise
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise
x = tf.compat.v1.placeholder(tf.float32, [None, 1])
y = tf.compat.v1.placeholder(tf.float32, [None, 1])
l1 = add_layer(x, 1, 10, activate_function=tf.nn.relu)
prediction = add_layer(l1, 10, 1)
loss = tf.reduce_mean(tf.reduce_sum(tf.square(prediction - y), reduction_indices=[1]))
learning_rate = 0.000001
train = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(loss)
init = tf.compat.v1.global_variables_initializer()
with tf.compat.v1.Session() as sess:
    sess.run(init)
    for i in range(400001):
        sess.run(train, feed_dict={x: x_data, y: y_data})
        if i % 20 == 0:
            print(i, round(sess.run(loss), 6))
