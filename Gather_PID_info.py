import psutil

def PID_info():
    pid = psutil.pids()
    PID_list = []
    for i in pid:
        PID_dict={}
        try:
            proc = psutil.Process(i)
            PID_dict['PID']=i
            PID_dict['memory_percent']=proc.memory_percent()
            PID_dict['proc_name']=proc.name()
            PID_dict['proc_exe']=proc.exe()
            PID_list.append(PID_dict)
        except psutil.AccessDenied:
            print("psutil.AccessDenied")
    return PID_list

print(PID_info())