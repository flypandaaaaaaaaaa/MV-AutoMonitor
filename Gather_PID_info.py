import psutil,datetime

def PID_info():
    pid = psutil.pids()
    PID_list = []
    for i in pid:
        PID_dict={}
        try:
            proc = psutil.Process(i)
            PID_dict['PID']=i
            PID_dict['memory_percent']=proc.memory_percent()
            PID_dict['cpu_percent']=proc.cpu_percent()
            PID_dict['proc_name']=proc.name()
            PID_dict['proc_exe']=proc.exe()
            PID_dict['Collection_time']=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            PID_list.append(PID_dict)
        except psutil.AccessDenied:
            pass
    return PID_list