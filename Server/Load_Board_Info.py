import yaml,os
from MySQL_Model_Cls import board_info
from DB_Access import DBSession
from Server_Config import *
import Filter_File_cls


def mv_load_board():
    Board_File_List=[]
    ##获取目录下的所有borad信息文件
    try:
        filter_func=Filter_File_cls.file_filename(board_file_filter)
        Board_File_List=list(filter(filter_func.filterfile,os.listdir(Info_FilePath)))
    except Exception as e:
        print("获取board文件失败")


    ##打开数据库session
    session = DBSession()


    ###开始循环录入各个文件内容
    for single_file in Board_File_List:
        ##根据文件名头部ID获取客户端号
        Client_id=single_file.split('_')[0]
        with open (os.path.join(Info_FilePath,single_file),'r') as f:
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
                    print("Data Load into DB error")

    ##关闭数据库链接
    session.close()