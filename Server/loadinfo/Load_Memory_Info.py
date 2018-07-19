import yaml, os
from MySQL_Model_Cls import memory_static_info,memory_dynamic_info
from DB_Access import DBSession
from Server_Config import *
import Load_INDB_cls




#向数据库中录入内存静态信息和动态信息

def mv_load_st_mem():

    #打开一个数据库Session
    session = DBSession()

    try:
        mv_load_file=Load_INDB_cls.load_file_indb(Info_FilePath)

        #获取MS类型记录
        MEM_File_List=mv_load_file.get_filelist('MS')
    except Exception as e:
        print("获取Memory文件失败",e)

    # 开始一个循环，录入所有的文件内容
    for single_file in MEM_File_List:

        #获取文件头，客户端ID
        Client_id = single_file.file_name.split('_')[0]


        # 判断是否是静态信息文件,如果是，则录入静态信息表
        with open(os.path.join(Info_FilePath, single_file.file_name), 'r') as f:
            memory_static_info_list = yaml.load(f.read())

            for single_record in memory_static_info_list:

                #开始把记录载入数据库
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

                # 开始提交记录
                try:
                    session.add(new_memory_static_record)
                    session.commit()
                except Exception as e:
                    print("数据提交失败")
        #整个文件处理完成后，将文件状态置为 O
        mv_load_file.set_filestate(single_file.file_name, 'O')
        #处理完成后将记录移动到历史表中
        mv_load_file.move_file(single_file.file_name,bakup_path)

    ##关闭数据库链接
    session.close()

def mv_load_dy_mem():

    # 打开一个数据库Session
    session = DBSession()

    try:
        mv_load_file = Load_INDB_cls.load_file_indb(Info_FilePath)

        # 获取MD类型记录
        MEM_File_List = mv_load_file.get_filelist('MD')
    except Exception as e:
        print("获取Memory文件失败", e)

    # 开始一个循环，录入所有的文件内容
    for single_file in MEM_File_List:

        # 获取文件头，客户端ID
        Client_id = single_file.file_name.split('_')[0]


        #打开文件
        with open(os.path.join(Info_FilePath, single_file.file_name), 'r') as f:
            memory_dynamic_dic = yaml.load(f.read())
            #开始把记录载入数据库
            new_memory_dynamic_record = memory_dynamic_info(Client_id=Client_id,
                                                            Collection_time=memory_dynamic_dic['Collection_time'],
                                                            available=memory_dynamic_dic['available'],
                                                            percent=memory_dynamic_dic['percent'],
                                                            used=memory_dynamic_dic['used'],
                                                            free=memory_dynamic_dic['free']
                                                            )

            # 开始提交记录
            try:
                session.add(new_memory_dynamic_record)
                session.commit()
            except Exception as e:
                print("数据提交失败")

        #整个文件处理完成后，将文件状态置为 O
        mv_load_file.set_filestate(single_file.file_name, 'O')
        #处理完成后将记录移动到历史表中
        mv_load_file.move_file(single_file.file_name,bakup_path)

    # 关闭数据库链接
    session.close()