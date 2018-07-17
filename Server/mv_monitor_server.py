import schedule,os,time
from Server_Config import *
from Load_Board_Info import mv_load_board
from Load_CPU_Info import mv_load_cpu
from Load_Disk_Info import mv_load_dy_disk,mv_load_st_disk
from Load_Installation_Info import mv_load_installaion
from Load_Memory_Info import mv_load_dy_mem,mv_load_st_mem
from Load_PID_Info import mv_load_pid
from Load_Service_Info import mv_load_srv



if not os.path.exists(Info_FilePath):
    try:
        os.makedirs(Info_FilePath)
    except Exception as e:
        print("新建目录失败",e)
else not os.path.exists(bakup_path):
    try:
        os.makedirs(bakup_path)
    except Exception as e:
        print("新建目录失败", e)

schedule.every(10).seconds.do(mv_load_board)
schedule.every(10).seconds.do(mv_load_cpu)

schedule.every(10).seconds.do(mv_load_dy_disk)
schedule.every(10).seconds.do(mv_load_st_disk)


schedule.every(10).seconds.do(mv_load_installaion)

schedule.every(10).seconds.do(mv_load_dy_mem)
schedule.every(10).seconds.do(mv_load_st_mem)

schedule.every(10).seconds.do(mv_load_pid)
schedule.every(10).seconds.do(mv_load_srv)

while True:
    schedule.run_pending()
    time.sleep(1)