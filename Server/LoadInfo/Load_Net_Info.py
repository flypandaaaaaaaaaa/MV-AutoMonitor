import yaml, os
from Server.DB.MySQLModel import net_info
from Server.DB.DB_Access import DBSession
from Server.Server_Config import WORKPATH,BACKUP
from Server.DB.LoadInDB import LoadFile



def mv_load_net():

    # 打开一个数据库Session
    session = DBSession()

    try:
        mv_load_file = LoadFile(WORKPATH)

        # 获取N类型记录
        Net_File_List = mv_load_file.get_filelist('N')
    except Exception as e:
        print("获取net文件失败", e)

    # 开始一个循环，录入所有的文件内容
    for single_file in Net_File_List:

        # 获取文件头，客户端ID
        Client_id = single_file.file_name.split('_')[0]


        #打开文件
        with open(os.path.join(WORKPATH, single_file.file_name), 'r') as f:
            net_dic = yaml.load(f.read())
            #开始把记录载入数据库
            new_net_record = net_info(Client_id=Client_id,
                                    Collection_time=net_dic['Collection_time'],
                                      IP=net_dic['IP'],
                                      Netmask=net_dic['Netmask'],
                                      MAC=net_dic['MAC'],
                                      Gateway=net_dic['Gateway'],
                                      DHCP=net_dic['DHCP'],
                                      DNS=net_dic['DNS']
                                                        )

            # 开始提交记录
            try:
                session.add(new_net_record)
                session.commit()
            except Exception as e:
                print("数据提交失败",e)

        #整个文件处理完成后，将文件状态置为 O
        mv_load_file.set_filestate(single_file.file_name, 'O')
        #处理完成后将记录移动到历史表中
        mv_load_file.move_file(single_file.file_name,BACKUP)

        # 关闭数据库链接
    session.close()