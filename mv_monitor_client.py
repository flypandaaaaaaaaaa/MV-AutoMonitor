# -*- coding: utf-8 -*-

from Info_File_Gen import mv_gen_boardfile,mv_gen_cpufile,mv_gen_disk_dyn,mv_gen_disk_sta,mv_gen_installation,mv_gen_mem_dyn,mv_gen_mem_sta,mv_gen_pidfile,mv_gen_srvifile
from mv_file_transfer import mv_upload
import schedule,time,os
from Client_Config import  *


# logger = logging.getLogger(__name__)
# logger.setLevel(level = logging.INFO)
# handler = logging.FileHandler(os.path.join(Log_Pathlog,'log.txt')
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)

if  not os.path.exists(File_Gen_Path):
    try:
        os.makedirs(File_Gen_Path)
    except Exception as e:
        print('创建失败')
elif not os.path.exists(File_Backup):
    try:
        os.makedirs(File_Backup)
    except Exception as e:
        print('创建失败')
else:
    pass

#生成主板信息文件
schedule.every(5).seconds.do(mv_gen_boardfile)

#生成CPU信息文件
schedule.every(5).seconds.do(mv_gen_cpufile)

#生成硬盘静态信息文件
schedule.every(5).seconds.do(mv_gen_disk_sta)

#生成硬盘动态信息文件
schedule.every(5).seconds.do(mv_gen_disk_dyn)

#生成安装信息文件
schedule.every(5).seconds.do(mv_gen_installation)

#生成内存信息文件
schedule.every(5).seconds.do(mv_gen_mem_dyn)
schedule.every(5).seconds.do(mv_gen_mem_sta)

#生成进程信息文件
schedule.every(5).seconds.do(mv_gen_pidfile)

#生成服务信息文件
schedule.every(5).seconds.do(mv_gen_srvifile)

#FTP传输所有信息文件到服务器
schedule.every(5).seconds.do(mv_upload)



while True:
    schedule.run_pending()
    time.sleep(1)