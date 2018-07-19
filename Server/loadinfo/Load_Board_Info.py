import yaml,os
from MySQL_Model_Cls import board_info
from DB_Access import DBSession
from Server_Config import *
import Load_INDB_cls


def mv_load_board():

    ##打开数据库session
    session = DBSession()

    try:
        mv_load_file=Load_INDB_cls.load_file_indb(Info_FilePath)

        #获取B类型记录，B代表主板
        Board_File_List=mv_load_file.get_filelist('B')
    except Exception as e:
        print("获取board文件失败",e)




###开始循环录入各个文件内容
    for single_file in Board_File_List:
        ##根据文件名头部ID获取客户端号
        Client_id=single_file.file_name.split('_')[0]
        with open (os.path.join(Info_FilePath,single_file.file_name),'r') as f:
            board_info_list=yaml.load(f.read())
            for single_record in board_info_list:

                ##开始将记录映射进数据库
                new_board_record = board_info(Client_id=Client_id,Collection_time=single_record['Collection_time'],Caption=single_record['Caption'],ConfigOptions=single_record['ConfigOptions'],
                                      CreationClassName=single_record['CreationClassName'],Description=single_record['Description'],
                                      HostingBoard=single_record['HostingBoard'],Manufacturer=single_record['Manufacturer'],
                                      Name=single_record['Name'],PoweredOn=single_record['PoweredOn'],Product=single_record['Product'],
                                      Removable=single_record['Removable'],Replaceable=single_record['Replaceable'],
                                      RequiresDaughterBoard=single_record['RequiresDaughterBoard'],SerialNumber=single_record['SerialNumber'],
                                      Status=single_record['Status'],Tag=single_record['Tag'],Version=single_record['Version'])

                ###尝试提交数据
                try:
                    session.add(new_board_record)
                    session.commit()

                except Exception as e:
                    print("数据录入失败",e)

        #整个文件处理完成后，将文件状态置为 O
        mv_load_file.set_filestate(single_file.file_name, 'O')
        #处理完成后将记录移动到历史表中
        mv_load_file.move_file(single_file.file_name,bakup_path)
    ##关闭数据库链接
    session.close()