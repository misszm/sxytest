import tensorflow as tf
state = tf.Variable(0, name="counter")
one = tf.constant(1)
new_state = tf.add(state, one)
update_state = tf.compat.v1.assign_add(state, one)
init = tf.compat.v1.global_variables_initializer()
with tf.compat.v1.Session() as sess:
    sess.run(init)
    for _ in range(3):
        s = sess.run(state)
        r = sess.run(update_state)
        print(s, r)
