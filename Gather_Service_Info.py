import wmi,datetime


def service_info():
    c = wmi.WMI()
    service_list=[]
    for service in c.Win32_Service():
        service_dict={}
        service_dict['Collection_time'] = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        service_dict['srv_name']=service.Caption
        service_dict['StartMode']=service.StartMode
        service_dict['State']=service.State
        service_list.append(service_dict)
    return service_list