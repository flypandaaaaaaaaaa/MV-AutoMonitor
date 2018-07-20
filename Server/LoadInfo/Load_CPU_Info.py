import yaml, os
from Server.DB.MySQLModel import cpu_info
from Server.DB.DB_Access import DBSession
from Server.Server_Config import WORKPATH,BACKUP
from Server.DB.LoadInDB import LoadFile
#获取CPU目录下所有的文件列表
def mv_load_cpu():

    #打开一个数据库Session
    session = DBSession()

    try:
        mv_load_file = LoadFile(WORKPATH)

        # 获取C类型记录，C代表CPU
        CPU_File_List = mv_load_file.get_filelist('C')
    except Exception as e:
        print("获取CPU文件失败", e)

    #开始一个循环，录入所有的文件内容
    for single_file in CPU_File_List:

        #获取文件头，客户端ID
        Client_id = single_file.file_name.split('_')[0]

        #打开文件
        with open(os.path.join(WORKPATH, single_file.file_name), 'r') as f:
            cpu_info_list = yaml.load(f.read())
            for single_record in cpu_info_list:

                #开始把记录载入数据库
                new_cpu_record = cpu_info(Client_id=Client_id, Collection_time=single_record['Collection_time'],AddressWidth=single_record['AddressWidth'],
                                          Architecture=single_record['Architecture'],
                                          AssetTag=single_record['AssetTag'],
                                          Availability=single_record['Availability'],
                                          Caption=single_record['Caption'],
                                          Characteristics=single_record['Characteristics'],
                                          CpuStatus=single_record['CpuStatus'],
                                          CreationClassName=single_record['CreationClassName'],
                                          CurrentClockSpeed=single_record['CurrentClockSpeed'],
                                          CurrentVoltage=single_record['CurrentVoltage'],
                                          DataWidth=single_record['DataWidth'],
                                          Description=single_record['Description'],
                                          DeviceID=single_record['DeviceID'],
                                          ExtClock=single_record['ExtClock'],
                                          Family=single_record['Family'],
                                          L2CacheSize=single_record['L2CacheSize'],
                                          L3CacheSize=single_record['L3CacheSize'],
                                          L3CacheSpeed=single_record['L3CacheSpeed'],
                                          Level=single_record['Level'],
                                          LoadPercentage=single_record['LoadPercentage'],
                                          Manufacturer=single_record['Manufacturer'],
                                          MaxClockSpeed=single_record['MaxClockSpeed'],
                                          Name=single_record['Name'],
                                          NumberOfCores=single_record['NumberOfCores'],
                                          NumberOfEnabledCore=single_record['NumberOfEnabledCore'],
                                          NumberOfLogicalProcessors=single_record['NumberOfLogicalProcessors'],
                                          PartNumber=single_record['PartNumber'],
                                          PowerManagementSupported=single_record['PowerManagementSupported'],
                                          ProcessorId=single_record['ProcessorId'],
                                          ProcessorType=single_record['ProcessorType'],
                                          Revision=single_record['Revision'],
                                          Role=single_record['Role'],
                                          SecondLevelAddressTranslationExtensions=single_record['SecondLevelAddressTranslationExtensions'],
                                          SerialNumber=single_record['SerialNumber'],
                                          SocketDesignation=single_record['SocketDesignation'],
                                          Status=single_record['Status'],
                                          StatusInfo=single_record['StatusInfo'],
                                          SystemCreationClassName=single_record['SystemCreationClassName'],
                                          SystemName=single_record['SystemName'],
                                          ThreadCount=single_record['ThreadCount'],
                                          UpgradeMethod=single_record['UpgradeMethod'],
                                          Version=single_record['Version'],
                                          VirtualizationFirmwareEnabled=single_record['VirtualizationFirmwareEnabled'],
                                          VMMonitorModeExtensions=single_record['VMMonitorModeExtensions']
                                          )

                #开始提交记录
                try:
                    session.add(new_cpu_record)
                    session.commit()
                except Exception as e:
                    print("数据载入失败",e)

        #整个文件处理完成后，将文件状态置为 O
        mv_load_file.set_filestate(single_file.file_name, 'O')
        #处理完成后将记录移动到历史表中
        mv_load_file.move_file(single_file.file_name,BACKUP)

    #关闭数据库链接
    session.close()