import paramiko

def sftp_upload(host,port,username,password,local,remote):
    sf = paramiko.Transport((host,port))
    sf.connect(username = username,password = password)
    sftp = paramiko.SFTPClient.from_transport(sf)
    try:
        sftp.put(local,remote)#上传文件
    except Exception as e:
        print('upload exception:',e)
    sf.close()


host = '192.168.29.150'
port = 22
username = 'root'
password = '123456'
local_file='boardinfo.txt'
local_path = 'D:\\'
remote_path = '/tmp/'
remote_file=local_file
sftp_upload(host,port,username,password,local_path+local_file,remote_path+remote_file)
