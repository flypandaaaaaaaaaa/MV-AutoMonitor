import Gather_Board_Info
import socket,getpass,datetime,yaml,uuid
nowTime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
hostname = socket.gethostname()
username=getpass.getuser()
ip = socket.gethostbyname(hostname)
ipList = socket.gethostbyname_ex(hostname)

#计算机名+登陆用户名+信息类型+全局唯一串号+日期.txt
board_info_list=Gather_Board_Info.Board_Info()
yaml_doc=yaml.dump(board_info_list)
with open ('D:'+hostname+'_'+username+'_'+'board'+'_'+str(uuid.uuid1())+'_'+nowTime+'.txt','w') as f:
    f.write(yaml_doc)


