import yaml, os
from MySQL_Model_Cls import disk_dynamic_info,disk_static_info
from DB_Access import DBSession
from Server_Config import *
import Filter_File_cls
from convert_db_parameter import  convert_db_par


#向数据库中录入内存静态信息和动态信息


#获取Memory目录下所有的文件列表
try:
    filter_func=Filter_File_cls.file_filename(disk_file_filter)
    Disk_File_List = list(filter(filter_func.filterfile,os.listdir(Info_FilePath)))
except Exception as e:
    print("获取内存文件列表失败")

#打开一个数据库Session
session = DBSession()

# 开始一个循环，录入所有的文件内容
for single_file in Disk_File_List:

    #获取文件头，客户端ID
    Client_id = single_file.split('_')[0]


    # 判断是否是静态信息文件,如果是，则录入静态信息表

    if 'static' in single_file:

        # 打开文件
        with open(os.path.join(Info_FilePath, single_file), 'r') as f:
            disk_static_info_list = yaml.load(f.read())

            for single_record in disk_static_info_list:

                #开始把记录载入数据库
                new_disk_static_record = disk_static_info(Client_id=Client_id,Collection_time=single_record['Collection_time'], BytesPerSector=single_record['BytesPerSector'],
                                                          Capabilities=convert_db_par(*single_record['Capabilities']),
                                                          CapabilityDescriptions=convert_db_par(*single_record['CapabilityDescriptions']),
                                                          Caption=single_record['Caption'],
                                                          ConfigManagerErrorCode=single_record['ConfigManagerErrorCode'],
                                                          ConfigManagerUserConfig= single_record['ConfigManagerUserConfig'],
                                                          CreationClassName= single_record['CreationClassName'],
                                                          Description= single_record['Description'],
                                                          DeviceID = single_record['DeviceID'],
                                                          FirmwareRevision = single_record['FirmwareRevision'],
                                                          Index=single_record['Index'],
                                                          InterfaceType= single_record['InterfaceType'],
                                                          Manufacturer= single_record['Manufacturer'],
                                                          MediaLoaded= single_record['MediaLoaded'],
                                                          MediaType= single_record['MediaType'],
                                                          Model= single_record['Model'],
                                                          Name= single_record['Name'],
                                                          Partitions= single_record['Partitions'],
                                                          PNPDeviceID= single_record['PNPDeviceID'],
                                                          SCSIBus = single_record['SCSIBus'],
                                                          SCSILogicalUnit= single_record['SCSILogicalUnit'],
                                                          SCSIPort= single_record['SCSIPort'],
                                                          SCSITargetId = single_record['SCSITargetId'],
                                                          SectorsPerTrack = single_record['SectorsPerTrack'],
                                                          SerialNumber = single_record['SerialNumber'],
                                                          Signature = single_record['Signature'],
                                                          Size = single_record['Size'],
                                                          Status = single_record['Status'],
                                                          SystemCreationClassName = single_record['SystemCreationClassName'],
                                                          SystemName = single_record['SystemName'],
                                                          TotalCylinders = single_record['TotalCylinders'],
                                                          TotalHeads = single_record['TotalHeads'],
                                                          TotalSectors = single_record['TotalSectors'],
                                                          TotalTracks = single_record['TotalTracks'],
                                                          TracksPerCylinder = single_record['TracksPerCylinder']
                                                          )

                # 开始提交记录
                # try:
                session.add(new_disk_static_record)
                session.commit()
                # except Exception as e:
                #     print("数据提交失败")

    ##开始提交动态数据
    elif 'dynamic' in single_file:

        #打开文件
        with open(os.path.join(Info_FilePath, single_file), 'r') as f:
            disk_dynamic_list = yaml.load(f.read())
            for single_record in disk_dynamic_list:

                #开始把记录载入数据库
                new_disk_dynamic_record = disk_dynamic_info(Client_id=Client_id,
                                                            Collection_time=single_record['Collection_time'],
                                                            device=single_record['device'],
                                                            mountpoint=single_record['mountpoint'],
                                                            fstype=single_record['fstype'],
                                                            opts=single_record['opts'],
                                                            total = single_record['total'],
                                                            used = single_record['used'],
                                                            free = single_record['free'],
                                                            percent = single_record['percent']
                                                            )

                # 开始提交记录
                try:
                    session.add(new_disk_dynamic_record)
                    session.commit()
                except Exception as e:
                    print("数据提交失败")
    else:
        print ('文件格式非法')


# 关闭数据库链接
session.close()