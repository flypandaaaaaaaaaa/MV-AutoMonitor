import yaml, os
from MySQL_Model_Cls import service_info
from DB_Access import DBSession
from Server_Config import *
import Filter_File_cls


def mv_load_srv():
    SRV_File_List=[]
    #获取SRV目录下所有的文件列表
    try:
        filter_func=Filter_File_cls.file_filename(service_file_filter)
        SRV_File_List = list(filter(filter_func.filterfile,os.listdir(Info_FilePath)))
    except Exception as e:
        print("获取SRV文件列表失败")

    #打开一个数据库Session
    session = DBSession()

    #开始一个循环，录入所有的文件内容
    for single_file in SRV_File_List:

        #获取文件头，客户端ID
        Client_id = single_file.split('_')[0]

        #打开文件
        with open(os.path.join(Info_FilePath, single_file), 'r') as f:
            service_info_list = yaml.load(f.read())
            for single_record in service_info_list:

                #开始把记录载入数据库
                new_service_record = service_info(Client_id=Client_id,
                                                  Collection_time=single_record['Collection_time'],
                                                  srv_name=single_record['srv_name'],
                                                  StartMode=single_record['StartMode'],
                                                  State=single_record['State']
                                                  )

                #开始提交记录
                try:
                    session.add(new_service_record)
                    session.commit()
                except Exception as e:
                    print("数据载入失败",single_record['srv_name'])

    #关闭数据库链接
    session.close()