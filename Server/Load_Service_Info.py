import yaml, os
from MySQL_Model_Cls import service_info
from DB_Access import DBSession
from Server_Config import *
import Load_INDB_cls


def mv_load_srv():

    #打开一个数据库Session
    session = DBSession()


    try:
        mv_load_file=Load_INDB_cls.load_file_indb(Info_FilePath)

        #获取S类型记录
        SRV_File_List=mv_load_file.get_filelist('S')
    except Exception as e:
        print("获取SRV文件失败",e)


    #开始一个循环，录入所有的文件内容
    for single_file in SRV_File_List:

        #获取文件头，客户端ID
        Client_id = single_file.file_name.split('_')[0]

        #打开文件
        with open(os.path.join(Info_FilePath, single_file.file_name), 'r') as f:
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

        #整个文件处理完成后，将文件状态置为 O
        mv_load_file.set_filestate(single_file.file_name, 'O')
        #处理完成后将记录移动到历史表中
        mv_load_file.move_file(single_file.file_name,bakup_path)

    #关闭数据库链接
    session.close()