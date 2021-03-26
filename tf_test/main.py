import tensorflow as tf
import numpy as np


def main():
    x_data = np.random.uniform(1, 20, 100).astype(np.float32)
    y_data = x_data * x_data + 0.3

    a = tf.random.uniform([1], -1.0, 1.0)
    weights = tf.Variable(a)
    biases = tf.Variable(tf.zeros([1]))

    y = weights * x_data + biases

    loss = tf.reduce_mean(tf.square(y - y_data))
    learning_rate = 0.001

    # def gen_learning_rate():
    #     global_step = tf.Variable(0)
    #     decay_steps = 10
    #     decay_rate = 0.9
    #     learning_tate = tf.compat.v1.train.exponential_decay(learning_tate, global_step, decay_steps, decay_rate,
    #                                                          staircase=True)
    #     return learning_tate
    # learning_rate = gen_learning_rate()
    # optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.5)
    optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate)
    train = optimizer.minimize(loss)
    init = tf.compat.v1.global_variables_initializer()
    with tf.compat.v1.Session() as sess:
        sess.run(init)
        for i in range(40001):
            sess.run(train)
            if i % 20 == 0:
                print(i, sess.run(weights), sess.run(biases), round(sess.run(loss), 6))


if __name__ == '__main__':
    # main()
    print(globals())
    print(locals())
    print(dir())

