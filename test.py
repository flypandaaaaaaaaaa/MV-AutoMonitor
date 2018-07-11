import wmi
class servicePython():
    def __init__(self, serviceName):
        self.c = wmi.WMI()
        self.serviceName = serviceName
    def setServiceName(self, serviceName):
        self.serviceName = serviceName
    def getStatus(self):
        srv = self.c.Win32_Service (name=self.serviceName)
        if srv != []:
        return c.Status