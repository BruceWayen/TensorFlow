import tensorflow as tf
#测试TensorFlow安装是否成功
m1 = tf.constant([[3,3]])#定义一个1x2的矩阵常量
m2 = tf.constant([[2],[3]])#定义一个2x1的矩阵常量
session = tf.Session()#获取session会话,注意要加括号
result = tf.matmul(m1,m2)#计算矩阵相乘
run = session.run(result)#执行图

print(run)#打印结果
session.close()#关闭会话