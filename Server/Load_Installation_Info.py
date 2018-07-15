import yaml,os
from MySQL_Model_Cls import installation_info
from DB_Access import DBSession
from Server_Config import *
import Filter_File_cls



#向数据库中录入安装软件的静态信息


#获取Collection目录下所有的文件列表
try:
    filter_func=Filter_File_cls.file_filename(installation_file_filter)
    Installation_File_List = list(filter(filter_func.filterfile,os.listdir(Info_FilePath)))
except Exception as e:
    print("获取内存文件列表失败")

#打开一个数据库Session
session = DBSession()

# 开始一个循环，录入所有的文件内容
for single_file in Installation_File_List:

    #获取文件头，客户端ID
    Client_id = single_file.split('_')[0]




    # 打开文件
    with open(os.path.join(Installation_FilePath, single_file), 'r') as f:
        installation_info_list = yaml.load(f.read())

        for single_record_index in range(len(installation_info_list)-1):

            #开始把记录载入数据库
            new_installation_record = installation_info(Client_id=Client_id,
                                                        Collection_time=installation_info_list[-1],
                                                        software=installation_info_list[single_record_index]
                                                        )

            # 开始提交记录
            # try:
            session.add(new_installation_record)
            session.commit()
            # except Exception as e:
            #     print("数据提交失败")



# 关闭数据库链接
session.close()