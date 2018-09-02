import tensorflow as tf

#测试TensorFlow中的变量Variable
state = tf.Variable(0, name='zero')#定义一个常量
new_value = tf.add(state, 1)# new_value=state+1
update = tf.assign(state, new_value)#TensorFlow中赋值不能用等号,assign函数就是赋值的
init = tf.global_variables_initializer()#初始化全局变量
with tf.Session() as sess:
    sess.run(init)#初始化全局变量
    print(state)
    for _ in range(5):
        sess.run(update)#执行update方法
        print(sess.run(state))#打印结果
