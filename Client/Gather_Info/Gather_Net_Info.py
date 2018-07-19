import netifaces
import subprocess
import datetime

def net_info():
    def checkIP(str):
        item=str.split('.')
        num=0
        for x in item:
            try:
                if int(x) >= 0 and int(x) <= 255:
                    num=num+1
            except Exception as e:
                continue
        if num==4:
            return True

    def findDNS():
        output = subprocess.Popen(["ipconfig", "/all"], stdout=subprocess.PIPE).communicate()[0].decode("gbk")
        for i in output.split('\r\n'):
            if 'DNS 服务器' in i:
                if checkIP(i.split(':')[1].strip(' ')):
                    return i.split(':')[1].strip(' ')

    def findDHCP():
        output = subprocess.Popen(["ipconfig", "/all"], stdout=subprocess.PIPE).communicate()[0].decode("gbk")
        for i in output.split('\r\n'):
            if 'DHCP 服务器' in i:
                if checkIP(i.split(':')[1].strip(' ')):
                    return i.split(':')[1].strip(' ')



    routingGateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
    routingNicName = netifaces.gateways()['default'][netifaces.AF_INET][1]
    net_dict={}
    for interface in netifaces.interfaces():
        if interface == routingNicName:
            routingNicMacAddr = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
            try:
                routingIPAddr = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
                routingIPNetmask = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
            except KeyError:
                pass

    net_dict['IP']=routingIPAddr
    net_dict['Gateway']=routingGateway
    net_dict['MAC']=routingNicMacAddr
    net_dict['Netmask']=routingIPNetmask
    net_dict['DNS']=findDNS()
    net_dict['DHCP']=findDHCP()
    net_dict['Collection_time']=datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    return net_dict


