import tensorflow as tf
#测试TensorFlow的Fetc
#Fetch作用是一次执行多个operation
#创建三个常量
input_value1 = tf.constant(2.0)
input_value2 = tf.constant(3.0)
input_value3 = tf.constant(5.0)
#创建两个op
tf_add = tf.add(input_value1,input_value2)#加法的op
tf_mult = tf.multiply(input_value3,tf_add)#乘法的op
with tf.Session() as  sess:
    print(sess.run([tf_add,tf_mult]))#主要要加中括号