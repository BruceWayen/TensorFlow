import tensorflow as tf
import  numpy as np
#一个简单TensorFlow实例,目的是计算线性模型的斜率和截距
#定义100个随机的点
x_data = np.random.rand(100)
#定义一个一元一次函数y=0.7x+1.3
y_data = x_data * 0.7 +1.3
#定义一个变量k,值为10.0
k = tf.Variable(10.0)
#定义一个变量b,值为3.2
b = tf.Variable(3.2)
#预测函数
y=k * x_data + b
#定义一个损失函数tf.reduce_mean是求平均值,tf.square是求平方
loss = tf.reduce_mean(tf.square(y_data-y))
#梯度下降函数,有点类似学习率
optimizer = tf.train.GradientDescentOptimizer(0.2)
#z最小化损失函数
train = optimizer.minimize(loss)
#初始化常量
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for step in range(299):
        sess.run(train)
        if step %20==0:
            print(step,sess.run([k,b]))



