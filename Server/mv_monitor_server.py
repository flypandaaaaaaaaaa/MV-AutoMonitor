import schedule,os,time
from Server.LoadInfo.Load_Board_Info import mv_load_board
from Server.LoadInfo.Load_CPU_Info import mv_load_cpu
from Server.LoadInfo.Load_Disk_Info import mv_load_dy_disk,mv_load_st_disk
from Server.LoadInfo.Load_Installation_Info import mv_load_installaion
from Server.LoadInfo.Load_Memory_Info import mv_load_dy_mem,mv_load_st_mem
from Server.LoadInfo.Load_PID_Info import mv_load_pid
from Server.LoadInfo.Load_Service_Info import mv_load_srv
from Server.LoadInfo.Load_Net_Info import mv_load_net
from Server.Server_Config import WORKPATH,BACKUP
from Server.DB.load_file2mysql import mv_loadfile2mysql

if not os.path.exists(WORKPATH):
    try:
        os.makedirs(WORKPATH)
    except Exception as e:
        print("新建目录失败",e)
if not os.path.exists(BACKUP):
    try:
        os.makedirs(BACKUP)
    except Exception as e:
        print("新建目录失败", e)

# schedule.every(10).seconds.do(mv_loadfile2mysql,WORKPATH)

# schedule.every(10).seconds.do(mv_load_board)
# schedule.every(10).seconds.do(mv_load_cpu)
#
schedule.every(10).seconds.do(mv_load_dy_disk)
schedule.every(10).seconds.do(mv_load_st_disk)


schedule.every(10).seconds.do(mv_load_installaion)

schedule.every(10).seconds.do(mv_load_dy_mem)
schedule.every(10).seconds.do(mv_load_st_mem)

schedule.every(10).seconds.do(mv_load_pid)
schedule.every(10).seconds.do(mv_load_srv)

schedule.every(10).seconds.do(mv_load_net)
while True:
    schedule.run_pending()
    time.sleep(1)