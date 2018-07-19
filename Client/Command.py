import paramiko, os,hashlib
from Gather_Board_Info import Board_Info
class command(object):

    def __init__(self, host, port, username, password):

        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password

    def __whoami(self):
        serial_num=Board_Info()[0]['SerialNumber']
        if serial_num is not None:
            myuniquehash=hashlib.md5(serial_num.encode('utf-8')).hexdigest()
        else:
            myuniquehash='Ihavenohash'
        return myuniquehash

    def command_download(self, remote_command_path,local_command_path):
        sf = paramiko.Transport((self.__host, self.__port))
        sf.connect(username=self.__username, password=self.__password)
        sftp = paramiko.SFTPClient.from_transport(sf)
        myuniquehash = self.__whoami()
        if myuniquehash=='Ihavenohash':
            print("没有hash值，无法定位本机")
        else:
            try:
                ###根据主板序列号算出本机的hash值，下载包含该hash值的命令文件

                dir=sftp.listdir(remote_command_path)
                for command_file in dir:
                    if myuniquehash in command_file:
                        self.__commandfile=command_file
                        self.__Client_command_Path=local_command_path
                        ##当发现第一个文件中包含本机的hash值时直接退出本次循环，针对第一个命令文件进行下载操作
                        break
                sftp.get(remote_command_path+command_file,os.path.join(local_command_path,self.__commandfile))  # 下载命令文件
                sftp.remove(remote_command_path+self.__commandfile)
            except Exception as e:
                print('下载命令文件失败', e)
        sf.close()

    def command_execute(self):

        #拼装出dos命令行，并用os模块进行执行
        command="python"+" "+os.path.join(self.__Client_command_Path,self.__commandfile)
        try:
            os.system(command)
        except Exception as e:
            print("命令执行失败",e)