import os

import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "4"
input1 = tf.compat.v1.placeholder(tf.float32)
input2 = tf.compat.v1.placeholder(tf.float32)
output = tf.matmul(input1, input2)
# output = tf.multiply(input1, input2)
with tf.compat.v1.Session() as sess:
    # r = sess.run(output, feed_dict={input2: [[7., 1], [7., 1]], input1: [[8., 2, 1], [8., 2, 1]]})
    r = sess.run(output, feed_dict={input1: [[7., 1, 2], [7., 1, 2]], input2: [[2,1], [2, 1]]})
    print(r)
