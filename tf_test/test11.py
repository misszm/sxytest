import numpy as np
import tensorflow as tf
a = np.array([[1],
                [2],
                [3]])
b = np.array([[1, 2, 3]])
print(a)
print(b)
c = np.matmul(a, b)
print(c)
d= a * a
print(d)
e = c - d
print(e)
f = tf.square(e)
sf = tf.reduce_sum(f, reduction_indices=[1])
g = tf.reduce_mean(sf)
init = tf.compat.v1.global_variables_initializer()
with tf.compat.v1.Session() as sess:
    sess.run(init)
    f = sess.run(f)
    print(f)
    g = sess.run(g)
    print(g)
    sf = sess.run(sf)
    print(sf)
