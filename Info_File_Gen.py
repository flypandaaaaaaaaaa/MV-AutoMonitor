import Gather_Board_Info,Gather_CPU_Info,Gather_Memory_Info,Gather_Disk_Info,Gather_Installation_Info,Gather_PID_info,Gather_Service_Info
import all_file_gen_cls
from Client_Config import File_Name_Subfix,File_Gen_Path,Client_ID

def mv_gen_boardfile():
    try:
        ob_gen_board_info=all_file_gen_cls.all_info_gen(Gather_Board_Info.Board_Info(),'board',File_Gen_Path,Client_ID,File_Name_Subfix)
        ob_gen_board_info.gen_file()
    except Exception as e:
        print()
def mv_gen_cpufile():
    try:
        ob_gen_cpu_info=all_file_gen_cls.all_info_gen(Gather_CPU_Info.CPU_Info(),'cpu',File_Gen_Path,Client_ID,File_Name_Subfix)
        ob_gen_cpu_info.gen_file()
    except Exception as e:
        print()


def mv_gen_mem_dyn():
    try:
        ob_gen_mem_dyn=all_file_gen_cls.all_info_gen(Gather_Memory_Info.memory_dynamic_info(),'memory_dynamic',File_Gen_Path,Client_ID,File_Name_Subfix)
        ob_gen_mem_dyn.gen_file()
    except Exception as e:
        print()

def mv_gen_mem_sta():
    try:
        ob_gen_mem_sta=all_file_gen_cls.all_info_gen(Gather_Memory_Info.memory_static_info(),'memory_static',File_Gen_Path,Client_ID,File_Name_Subfix)
        ob_gen_mem_sta.gen_file()
    except Exception as e:
        print()

def mv_gen_disk_dyn():
    try:
        ob_gen_disk_dyn=all_file_gen_cls.all_info_gen(Gather_Disk_Info.disk_dynamic_info(),'disk_dynamic',File_Gen_Path,Client_ID,File_Name_Subfix)
        ob_gen_disk_dyn.gen_file()
    except Exception as e:
        print()


def mv_gen_disk_sta():
    try:
        ob_gen_disk_sta=all_file_gen_cls.all_info_gen(Gather_Disk_Info.disk_static_info(),'disk_static',File_Gen_Path,Client_ID,File_Name_Subfix)
        ob_gen_disk_sta.gen_file()
    except Exception as e:
        print()


def mv_gen_installation():
    try:
        ob_gen_install_info=all_file_gen_cls.all_info_gen(Gather_Installation_Info.installation_info(),'installation',File_Gen_Path,Client_ID,File_Name_Subfix)
        ob_gen_install_info.gen_file()
    except Exception as e:
        print('fail')

def mv_gen_pidfile():
    try:
        ob_gen_pid_info=all_file_gen_cls.all_info_gen(Gather_PID_info.PID_info(),'pid',File_Gen_Path,Client_ID,File_Name_Subfix)
        ob_gen_pid_info.gen_file()
    except Exception as e:
        print()

def mv_gen_srvifile():
    try:
        ob_gen_srv_info=all_file_gen_cls.all_info_gen(Gather_Service_Info.service_info(),'service',File_Gen_Path,Client_ID,File_Name_Subfix)
        ob_gen_srv_info.gen_file()
    except Exception as e:
        print()