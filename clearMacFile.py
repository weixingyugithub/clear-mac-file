# -*- coding:utf-8 -*-
#���ܣ�ɾ����._��ͷ���ļ�      �ļ�ģʽgb18030���·�����ĵ�����
import re
import os
import time
#str.split(string)�ָ��ַ���
#'���ӷ�'.join(list) ���б�����ַ���
def change_name(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path)[1] #�ָ��Ŀ¼���ļ�
        before_file = file_path[0:2] #�ָ���ļ����ļ���չ��
        if before_file == '._' or file_path == '.DS_Store':
            os.remove(path)
            print("ɾ���ļ�:"+path)
            log.write("ɾ���ļ�:"+path+'\n')
            i+=1 #ע�������i��һ������
    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_name(os.path.join(path,x)) #os.path.join()��·�������Ϻ�����


img_dir = '/Users/weixingyu/git/best-assemble'
img_dir = img_dir.replace('\\','/')
start = time.time()
log_time = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(start))
i = 0
print('�ļ�ɾ����ʼ')
print('����log��־-delete.log')
log = open("delete-"+log_time+".log",'w')
change_name(img_dir)
log.close()
if i == 0:
    os.remove(os.getcwd()+"/delete-"+log_time+".log")
c = time.time() - start
print('�������к�ʱ:%0.2f'%(c))
print('�ܹ������� %s ���ļ�'%(i))

