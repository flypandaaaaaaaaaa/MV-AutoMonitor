import yaml,os
from MySQL_Model_Cls import board_info
from DB_Access import DBSession
from Server_Config import *


'''获取Board目录下所有的文件列表'''
try:
    Board_File_List=os.listdir(Board_FilePath)
except Exception as e:
    print("Get Board File list Fail")

'''打开一个数据库Session'''
session = DBSession()

'''开始一个循环，录入所有的文件内容'''
for single_file in Board_File_List:
    '''获取文件头，客户端ID'''
    Client_id=single_file.split('_')[0]
    with open (os.path.join(Board_FilePath,single_file),'r') as f:
        board_info_list=yaml.load(f.read())
        for single_record in board_info_list:

            '''开始把记录载入数据库'''
            new_board_record = board_info(Client_id=Client_id,Caption=single_record['Caption'],ConfigOptions=single_record['ConfigOptions'],
                                  CreationClassName=single_record['CreationClassName'],Description=single_record['Description'],
                                  HostingBoard=single_record['HostingBoard'],Manufacturer=single_record['Manufacturer'],
                                  Name=single_record['Name'],PoweredOn=single_record['PoweredOn'],Product=single_record['Product'],
                                  Removable=single_record['Removable'],Replaceable=single_record['Replaceable'],
                                  RequiresDaughterBoard=single_record['RequiresDaughterBoard'],SerialNumber=single_record['SerialNumber'],
                                  Status=single_record['Status'],Tag=single_record['Tag'],Version=single_record['Version'])

            '''开始提交记录'''
            try:
                session.add(new_board_record)
                session.commit()
            except Exception as e:
                print("Data Load into DB error")

'''关闭数据库链接'''
session.close()