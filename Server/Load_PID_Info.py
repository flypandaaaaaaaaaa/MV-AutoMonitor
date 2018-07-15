import yaml, os
from MySQL_Model_Cls import pid_info
from DB_Access import DBSession
from Server_Config import *

#获取PID目录下所有的文件列表
try:
    filter_func=Filter_File_cls.file_filename(pid_file_filter)
    PID_File_List = list(filter(filter_func.filterfile,os.listdir(Info_FilePath)))
except Exception as e:
    print("获取PID文件列表失败")

#打开一个数据库Session
session = DBSession()

#开始一个循环，录入所有的文件内容
for single_file in PID_File_List:

    #获取文件头，客户端ID
    Client_id = single_file.split('_')[0]

    #打开文件
    with open(os.path.join(Process_FilePath, single_file), 'r') as f:
        pid_info_list = yaml.load(f.read())
        for single_record in pid_info_list:

            #开始把记录载入数据库
            new_pid_record = pid_info(Client_id=Client_id,
                                      Collection_time=single_record['Collection_time'],
                                      PID=single_record['PID'],
                                      memory_percent=single_record['memory_percent'],
                                      cpu_percent=single_record['cpu_percent'],
                                      proc_name=single_record['proc_name'],
                                      proc_exe=single_record['proc_exe']
                                      )

            #开始提交记录
            try:
                session.add(new_pid_record)
                session.commit()
            except Exception as e:
                print("数据载入失败",single_record['proc_name'])

#关闭数据库链接
session.close()