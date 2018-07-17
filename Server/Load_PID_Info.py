import yaml, os
from MySQL_Model_Cls import pid_info
from DB_Access import DBSession
from Server_Config import *
import Load_INDB_cls


def mv_load_pid():

    #打开一个数据库Session
    session = DBSession()

    try:
        mv_load_file=Load_INDB_cls.load_file_indb(Info_FilePath)

        #获取P类型记录
        PID_File_List=mv_load_file.get_filelist('P')
    except Exception as e:
        print("获取pid文件失败",e)

    #开始一个循环，录入所有的文件内容
    for single_file in PID_File_List:

        #获取文件头，客户端ID
        Client_id = single_file.file_name.split('_')[0]

        #打开文件
        with open(os.path.join(Info_FilePath, single_file.file_name), 'r') as f:
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

        # 整个文件处理完成后，将文件状态置为 O
        mv_load_file.set_filestate(single_file.file_name, 'O')
        # 处理完成后将记录移动到历史表中
        mv_load_file.move_file(single_file.file_name, bakup_path)

    #关闭数据库链接
    session.close()

