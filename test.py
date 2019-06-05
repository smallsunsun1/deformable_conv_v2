import tensorflow as tf
tf.enable_eager_execution()

a, b = tf.meshgrid(tf.range(3), tf.range(5))
grid = tf.stack([b, a], axis=-1)
print(grid)


