import Gather_Board_Info,Gather_CPU_Info,Gather_Memory_Info
import socket,getpass,datetime,yaml,uuid
from Client_Config import *
nowTime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
hostname = socket.gethostname()
username=getpass.getuser()
ip = socket.gethostbyname(hostname)
ipList = socket.gethostbyname_ex(hostname)

#客户端号+计算机名+登陆用户名+信息类型+全局唯一串号+日期.txt
board_info_list=Gather_Board_Info.Board_Info()
yaml_doc=yaml.dump(board_info_list)
with open (File_Gen_Path+Client_ID+'_'+hostname+'_'+username+'_'+'board'+'_'+str(uuid.uuid1())+'_'+nowTime+File_Name_Subfix,'w') as f:
    f.write(yaml_doc)


cpu_info_list=Gather_CPU_Info.CPU_Info()
yaml_doc=yaml.dump(cpu_info_list)
with open (File_Gen_Path+Client_ID+'_'+hostname+'_'+username+'_'+'cpu'+'_'+str(uuid.uuid1())+'_'+nowTime+File_Name_Subfix,'w') as f:
    f.write(yaml_doc)


memory_dynamic_info_list=Gather_Memory_Info.memory_dynamic_info()
yaml_doc=yaml.dump(memory_dynamic_info_list)
with open (File_Gen_Path+Client_ID+'_'+hostname+'_'+username+'_'+'memory_dynamic'+'_'+str(uuid.uuid1())+'_'+nowTime+File_Name_Subfix,'w') as f:
    f.write(yaml_doc)

memory_static_info_list=Gather_Memory_Info.memory_static_info()
yaml_doc=yaml.dump(memory_static_info_list)
with open (File_Gen_Path+Client_ID+'_'+hostname+'_'+username+'_'+'memory_static'+'_'+str(uuid.uuid1())+'_'+nowTime+File_Name_Subfix,'w') as f:
    f.write(yaml_doc)
