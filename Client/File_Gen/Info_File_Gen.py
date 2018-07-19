from Client.Gather_Info import Gather_Board_Info
from Client.Gather_Info import Gather_CPU_Info
from Client.Gather_Info import Gather_Memory_Info
from Client.Gather_Info import Gather_Disk_Info
from Client.Gather_Info import Gather_Installation_Info
from Client.Gather_Info import Gather_PID_info
from Client.Gather_Info import Gather_Service_Info
from Client.Gather_Info import Gather_Net_Info
from Client.File_Gen.All_FileGen import InfoGen
from Client.Client_Config import WORKPATH,MYID,SUBFIX

def mv_board():
    try:
        boardinfo=InfoGen(Gather_Board_Info.Board_Info(),'board',WORKPATH,MYID,SUBFIX)
        boardinfo.gen_file()
    except Exception as e:
        print(e)
def mv_cpu():
    try:
        cpuinfo=InfoGen(Gather_CPU_Info.CPU_Info(),'cpu',WORKPATH,MYID,SUBFIX)
        cpuinfo.gen_file()
    except Exception as e:
        print(e)


def mv_memdyn():
    try:
        memdyn=InfoGen(Gather_Memory_Info.memory_dynamic_info(),'memory_dynamic',WORKPATH,MYID,SUBFIX)
        memdyn.gen_file()
    except Exception as e:
        print(e)

def mv_memsta():
    try:
        memsta=InfoGen(Gather_Memory_Info.memory_static_info(),'memory_static',WORKPATH,MYID,SUBFIX)
        memsta.gen_file()
    except Exception as e:
        print(e)

def mv_diskdyn():
    try:
        diskdyn=InfoGen(Gather_Disk_Info.disk_dynamic_info(),'disk_dynamic',WORKPATH,MYID,SUBFIX)
        diskdyn.gen_file()
    except Exception as e:
        print(e)


def mv_disksta():
    try:
        disksta=InfoGen(Gather_Disk_Info.disk_static_info(),'disk_static',WORKPATH,MYID,SUBFIX)
        disksta.gen_file()
    except Exception as e:
        print(e)


def mv_install():
    try:
        installinfo=InfoGen(Gather_Installation_Info.installation_info(),'installation',WORKPATH,MYID,SUBFIX)
        installinfo.gen_file()
    except Exception as e:
        print(e)

def mv_pid():
    try:
        pidinfo=InfoGen(Gather_PID_info.PID_info(),'pid',WORKPATH,MYID,SUBFIX)
        pidinfo.gen_file()
    except Exception as e:
        print(e)

def mv_srv():
    try:
        srvinfo=InfoGen(Gather_Service_Info.service_info(),'service',WORKPATH,MYID,SUBFIX)
        srvinfo.gen_file()
    except Exception as e:
        print(e)

def mv_net():
    try:
        srvinfo=InfoGen(Gather_Net_Info.net_info(),'net',WORKPATH,MYID,SUBFIX)
        srvinfo.gen_file()
    except Exception as e:
        print(e)