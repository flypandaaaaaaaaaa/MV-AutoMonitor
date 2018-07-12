import Gather_Board_Info
import socket,getpass,datetime,yaml,uuid

#计算机名+登陆用户名+信息类型+全局唯一串号+日期.txt
with open ('D:\\'+'boardinfo'+'.txt','r') as f:
    list=yaml.load(f.read())
    print(list)

