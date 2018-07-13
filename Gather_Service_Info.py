def listservices():
    import wmi

    c = wmi.WMI()
    for service in c.Win32_Service():
        print (service.Caption,service.StartMode,service.State)

listservices()