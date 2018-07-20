import yaml, os
from Server.DB.MySQLModel import disk_dynamic_info,disk_static_info
from Server.DB.DB_Access import DBSession
from Server.DB.convert_db_parameter import  convert_db_par
from Server.Server_Config import WORKPATH,BACKUP
from Server.DB.LoadInDB import LoadFile


#向数据库中录入内存静态信息和动态信息

def mv_load_st_disk():

    #打开一个数据库Session
    session = DBSession()

    try:
        mv_load_file=LoadFile(WORKPATH)

        #获取DS类型记录
        Disk_File_List=mv_load_file.get_filelist('DS')
    except Exception as e:
        print("获取静态硬盘文件失败",e)


    # 开始一个循环，录入所有的文件内容
    for single_file in Disk_File_List:

        #获取文件头，客户端ID
        Client_id = single_file.file_name.split('_')[0]

        # 打开文件
        with open(os.path.join(WORKPATH, single_file.file_name), 'r') as f:
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
                try:
                    session.add(new_disk_static_record)
                    session.commit()
                except Exception as e:
                    print("数据提交失败",e)

        #整个文件处理完成后，将文件状态置为 O
        mv_load_file.set_filestate(single_file.file_name, 'O')
        #处理完成后将记录移动到历史表中
        mv_load_file.move_file(single_file.file_name,BACKUP)

    # 关闭数据库链接
    session.close()

def mv_load_dy_disk():

    # 打开一个数据库Session
    session = DBSession()

    try:
        mv_load_file = LoadFile(WORKPATH)

        # 获取DD类型记录
        Disk_File_List = mv_load_file.get_filelist('DD')
    except Exception as e:
        print("获取动态硬盘文件失败", e)

    # 开始一个循环，录入所有的文件内容
    for single_file in Disk_File_List:
        #获取文件头，客户端ID
        Client_id = single_file.file_name.split('_')[0]
        #打开文件
        with open(os.path.join(WORKPATH, single_file.file_name), 'r') as f:
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

        #整个文件处理完成后，将文件状态置为 O
        mv_load_file.set_filestate(single_file.file_name, 'O')
        #处理完成后将记录移动到历史表中
        mv_load_file.move_file(single_file.file_name,BACKUP)

    # 关闭数据库链接
    session.close()
