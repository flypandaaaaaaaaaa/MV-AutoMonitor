import paramiko, os,time,shutil
class sftp(object):

    def __init__(self, host, port, username, password):

        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password

    def batch_upload(self, workpath, remote,backup):
        sf = paramiko.Transport((self.__host, self.__port))
        sf.connect(username=self.__username, password=self.__password)
        sftp = paramiko.SFTPClient.from_transport(sf)

        filelist = os.listdir(workpath)
        time.sleep(10)

        for file in filelist:

            try:
                sftp.put(os.path.join(workpath, file), remote+file)  # 上传文件
            except Exception as e:
                print("上传失败",e)

            try:
                shutil.move(os.path.join(workpath, file), os.path.join(backup, file))
            except Exception as e:
                print("移动文件失败",e)
        sf.close()