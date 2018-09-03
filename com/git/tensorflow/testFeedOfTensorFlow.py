import tensorflow as tf
#测试Feed操作
input_value1 = tf.placeholder(tf.float32)#tf.placeholder作用是定义一个占位符,括号的内容为占位符的里面的数据类型
input_value2 = tf.placeholder(tf.float32)
#定义一个操作
tf_div = tf.div(input_value1, input_value2)
with tf.Session() as sess:
    print(sess.run(tf_div,feed_dict={input_value1:9,input_value2:3}))#feed_dict的作用是给占位符的两个值初始化值