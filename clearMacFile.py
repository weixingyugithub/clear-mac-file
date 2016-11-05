# -*- coding:utf-8 -*-
#功能：删除以._开头的文件      文件模式gb18030解决路径中文的问题
import re
import os
import time
#str.split(string)分割字符串
#'连接符'.join(list) 将列表组成字符串
def change_name(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path)[1] #分割出目录与文件
        before_file = file_path[0:2] #分割出文件与文件扩展名
        if before_file == '._' or file_path == '.DS_Store':
            os.remove(path)
            print("删除文件:"+path)
            log.write("删除文件:"+path+'\n')
            i+=1 #注意这里的i是一个陷阱
    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_name(os.path.join(path,x)) #os.path.join()在路径处理上很有用


img_dir = '/Users/weixingyu/git/best-assemble'
img_dir = img_dir.replace('\\','/')
start = time.time()
log_time = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(start))
i = 0
print('文件删除开始')
print('创建log日志-delete.log')
log = open("delete-"+log_time+".log",'w')
change_name(img_dir)
log.close()
if i == 0:
    os.remove(os.getcwd()+"/delete-"+log_time+".log")
c = time.time() - start
print('程序运行耗时:%0.2f'%(c))
print('总共处理了 %s 个文件'%(i))

