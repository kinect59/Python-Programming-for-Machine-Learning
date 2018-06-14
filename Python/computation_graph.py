import tensorflow as tf

# our first computation graph.
tf.reset_defaut_graph()

num1 = tf.constant([1])
num2 = tf.constant([2])

result = tf.add(num1, num2)

with tf.Session() as sess:
  r, nl = sess.run()
