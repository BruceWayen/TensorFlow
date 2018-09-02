import urllib.request
import re
import os
import urllib
import time
import random

#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')

def getImg(html):
  #  reg = r'src="(.+?\.jpg)" '
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)                              #转换成一个正则对象
    imglist = imgre.findall(html)                        #表示在整个网页中过滤出所有图片的地址，放在imglist中

    imgName = 0#声明一个变量赋值


    path = 'F:\PythonWorkSpace\picture2'           #设置保存地址

    if not os.path.isdir(path):
        os.makedirs(path)                           # 将图片保存到H:..\\test文件夹中，如果没有test文件夹则创建
    paths = path+'\\'                               #保存在test路径下

    for imgurl in imglist:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
        req = urllib.request.Request(url=imgurl, headers=headers)
        t = time.time()
        name = str(round(t * 1000))
        num = str(random.randint(1, 20000))
        #urllib.request.urlretrieve(imgurl,'{0}{1}.jpg'.format(paths,x)) #打开imglist，下载图片保存在本地，
        #format格式化字符串
        try:
            f = open(paths+ str(name+num)+".jpg", 'wb')
            f.write((urllib.request.urlopen(req)).read())
            print('第%d张图片已开始下载,图片名为%s，注意查看文件夹' % (imgName,str(name+num)))
            f.close()
        except Exception as e:
            print(imgurl+" error")
            print ('e.message:\t', e.message)
            print (imgurl)
        imgName += 1
       # print('第%d张图片已开始下载，注意查看文件夹' % imgName)
    return imglist

#html = getHtml("http://1024.97cnlp.net/pw/htm_data/15/1808/")         #获取该网址网页详细信息，html就是网页的源代码
#html = getHtml("http://tieba.baidu.com/p/3840085725")         #获取该网址网页详细信息，html就是网页的源代码
urlPath="http://1024.97cnlp.net/pw/htm_data/15/1808/"
suffix = 1238394
#count =10
limit=1193014
while (suffix > limit):
    try:
        urlPathnew=urlPath+str(suffix)+".html"
       # print(urlPathnew)
        html = getHtml(urlPathnew)
        getImg(html)                                        #从网页源代码中分析并下载保存图片
    except Exception as e:
        print(urlPathnew+" error")
    suffix=suffix-1
    #count=count-1