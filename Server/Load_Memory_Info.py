import yaml, os
from MySQL_Model_Cls import memory_static_info,memory_dynamic_info
from DB_Access import DBSession
from Server_Config import *


'''向数据库中录入内存静态信息和动态信息'''



'''获取Memory目录下所有的文件列表'''
try:
    MEM_File_List = os.listdir(Memory_FilePath)
except Exception as e:
    print("获取内存文件列表失败")

'''打开一个数据库Session'''
session = DBSession()

'''开始一个循环，录入所有的文件内容'''
for single_file in MEM_File_List:

    '''获取文件头，客户端ID'''
    Client_id = single_file.split('_')[0]


    '''判断是否是静态信息文件,如果是，则录入静态信息表'''

    if 'static' in single_file:

        '''打开文件'''
        with open(os.path.join(Memory_FilePath, single_file), 'r') as f:
            memory_static_info_list = yaml.load(f.read())

            for single_record in memory_static_info_list:

                '''开始把记录载入数据库'''
                new_memory_static_record = memory_static_info(Client_id=Client_id, Attributes=single_record['Attributes'],
                                                              BankLabel=single_record['BankLabel'],
                                                              Capacity=single_record['Capacity'],
                                                              Caption=single_record['Caption'],
                                                              ConfiguredClockSpeed=single_record['ConfiguredClockSpeed'],
                                                              CreationClassName= single_record['CreationClassName'],
                                                              DataWidth= single_record['DataWidth'],
                                                              Description= single_record['Description'],
                                                              DeviceLocator = single_record['DeviceLocator'],
                                                              FormFactor = single_record['FormFactor'],
                                                              InterleaveDataDepth=single_record['InterleaveDataDepth'],
                                                              InterleavePosition= single_record['InterleavePosition'],
                                                              Manufacturer= single_record['Manufacturer'],
                                                              MemoryType= single_record['MemoryType'],
                                                              Name= single_record['Name'],
                                                              PartNumber= single_record['PartNumber'],
                                                              PositionInRow= single_record['PositionInRow'],
                                                              SerialNumber= single_record['SerialNumber'],
                                                              SMBIOSMemoryType= single_record['SMBIOSMemoryType'],
                                                              Speed = single_record['Speed'],
                                                              Tag= single_record['Tag'],
                                                              TotalWidth= single_record['TotalWidth'],
                                                              TypeDetail = single_record['TypeDetail']
                                                              )

                '''开始提交记录'''
                try:
                    session.add(new_memory_static_record)
                    session.commit()
                except Exception as e:
                    print("数据提交失败")


    '''开始录入动态内存信息'''


    elif 'dynamic' in single_file:
    '''打开文件'''
        with open(os.path.join(Memory_FilePath, single_file), 'r') as f:
            memory_dynamic_info_list = yaml.load(f.read())

            for single_record in memory_dynamic_info_list:

                '''开始把记录载入数据库'''
                new_memory_dynamic_record = memory_dynamic_info(Client_id=Client_id,
                                                                Collection_time=single_record['Collection_time'],
                                                                available=single_record['available'],
                                                                percent=single_record['percent'],
                                                                used=single_record['used'],
                                                                free=single_record['free']
                                                                )

                '''开始提交记录'''
                try:
                    session.add(new_memory_dynamic_record)
                    session.commit()
                except Exception as e:
                    print("数据提交失败")
    else:
        print ('文件格式非法')


'''关闭数据库链接'''
session.close()