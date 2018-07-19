from Client.Info_File_Gen import mv_board
from Client.Info_File_Gen import mv_cpu
from Client.Info_File_Gen import mv_diskdyn
from Client.Info_File_Gen import mv_disksta
from Client.Info_File_Gen import mv_install
from Client.Info_File_Gen import mv_memdyn
from Client.Info_File_Gen import mv_memsta
from Client.Info_File_Gen import mv_net
from Client.Info_File_Gen import mv_pid
from Client.Info_File_Gen import mv_srv
from mv_file_transfer import mv_upload
import schedule
import os
import time
from Client.Client_Config import WORKPATH,BACKUP,LOGPATH


if  not os.path.exists(WORKPATH):
    try:
        os.makedirs(WORKPATH)
    except Exception as e:
        print('创建失败',e)
if not os.path.exists(BACKUP):
    try:
        os.makedirs(BACKUP)
    except Exception as e:
        print('创建失败',e)

if not os.path.exists(LOGPATH):
    try:
        os.makedirs(LOGPATH)
    except Exception as e:
        print('创建失败',e)

# # #生成主板信息文件
# # schedule.every().hour.do(mv_board)
# schedule.every(5).seconds.do(mv_board)
#
# # #生成CPU信息文件
# # schedule.every().hour.do(mv_cpu)
# schedule.every(5).seconds.do(mv_cpu)
#
# # #生成硬盘静态信息文件
# # schedule.every(30).minutes.do(mv_disksta)
# schedule.every(5).seconds.do(mv_disksta)
#
#
# # #生成硬盘动态信息文件
# # schedule.every(10).minutes.do(mv_diskdyn)
# schedule.every(5).seconds.do(mv_diskdyn)
#
# # #生成安装信息文件
# # schedule.every().hour.do(mv_install)
# schedule.every().minute.do(mv_install)

# #生成内存信息文件
# schedule.every(10).seconds.do(mv_memdyn)
# schedule.every(5).seconds.do(mv_memdyn)
#
# # schedule.every().hour.do(mv_memsta)
# schedule.every(5).seconds.do(mv_memsta)

# #生成进程信息文件
# schedule.every().hour.do(mv_pid)
# schedule.every(5).seconds.do(mv_pid)
#
# # #生成服务信息文件
# # schedule.every().hour.do(mv_srv)
# schedule.every(5).seconds.do(mv_srv)

# #生成网络信息文件
# schedule.every().hour.do(mv_net)
# schedule.every(5).seconds.do(mv_net)

# # #FTP传输所有信息文件到服务器
# # schedule.every(10).minutes.do(mv_upload)
schedule.every(5).seconds.do(mv_upload)


while True:
    schedule.run_pending()
    time.sleep(1)