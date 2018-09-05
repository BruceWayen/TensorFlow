# coding: utf-8
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

#载入数据集
mnist = input_data.read_data_sets("F:\PythonSpace\TensorFlow\data",one_hot=True)

#每个批次的大小
batch_size = 100
#计算一共有多少个批次
n_batch = mnist.train.num_examples // batch_size

#定义两个placeholder
#x = tf.placeholder(tf.float32,[None,784])
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])

#创建一个简单的神经网络

#定义神经网络中间层(隐藏层)
Weights_L1 = tf.Variable(tf.random_normal([784,10]))
print(Weights_L1.shape)
biases_L1 = tf.Variable(tf.zeros([1]))

Wx_plus_b_L1 = tf.matmul(x,Weights_L1) + biases_L1
L1 = tf.nn.tanh(Wx_plus_b_L1)#激活函数


W = tf.Variable(tf.zeros([10,10]))
b = tf.Variable(tf.zeros([10]))
prediction = tf.nn.softmax( tf.matmul(Wx_plus_b_L1,W) + b)

#二次代价函数
loss = tf.reduce_mean(tf.square(y-prediction))
#使用梯度下降法
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

#初始化变量
init = tf.global_variables_initializer()

#结果存放在一个布尔型列表中
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))#argmax返回一维张量中最大的值所在的位置
#求准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(21):
        for batch in range(n_batch):
            batch_xs,batch_ys =  mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys})

        acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        print("Iter " + str(epoch) + ",Testing Accuracy " + str(acc))





