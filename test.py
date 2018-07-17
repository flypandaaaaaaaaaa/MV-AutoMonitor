from Info_File_Gen import mv_gen_boardfile,mv_gen_cpufile,mv_gen_disk_dyn,mv_gen_disk_sta,mv_gen_installation,mv_gen_mem_dyn,mv_gen_mem_sta,mv_gen_pidfile,mv_gen_srvifile
from mv_file_transfer import mv_upload
import schedule,time



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