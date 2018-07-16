import paramiko, os,time,shutil
from Client_Config import *
class sftp(object):

    def __init__(self, host, port, username, password):

        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password

    def file_upload(self, basedir, file, remote):
        sf = paramiko.Transport((self.__host, self.__port))
        sf.connect(username=self.__username, password=self.__password)
        sftp = paramiko.SFTPClient.from_transport(sf)
        try:
            sftp.put(os.path.join(basedir, file), remote+file)  # 上传文件
        except Exception as e:
            print('upload exception:', e)
        sf.close()

    def batch_upload(self, path, remote):
        sf = paramiko.Transport((self.__host, self.__port))
        sf.connect(username=self.__username, password=self.__password)
        sftp = paramiko.SFTPClient.from_transport(sf)

        filelist = os.listdir(path)
        time.sleep(10)

        for file in filelist:

            try:
                sftp.put(os.path.join(path, file), remote+file)  # 上传文件
            except Exception as e:
                print("上传失败")

            try:
                shutil.move(os.path.join(path, file), os.path.join(File_Backup, file))
            except Exception as e:
                print("移动文件失败")
        sf.close()