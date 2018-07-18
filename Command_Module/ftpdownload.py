uuid='sdfghf34543'
local_path='D:\\'




host='192.168.29.250'
port=22
username='root'
password='123456'
remote_path='/tmp/'


import shutil,winreg
import paramiko,os

def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders\\',)
    return winreg.QueryValueEx(key, "Desktop")[0]

def file_download(host,port,username,password,remote_path, local_path,uuid):
    sf = paramiko.Transport((host,port))
    sf.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(sf)
    try:

        ###命令文件模板将带入一个UUID，根据这个值去找到对应的文件

        dir = sftp.listdir(remote_path)
        for filename in dir:
            if uuid in filename:
                ##当发现第一个文件中包含UUID时直接退出本次循环，开始下载操作
                break
        sftp.get(remote_path + filename, os.path.join(local_path, filename))  # 下载文件
        sftp.remove(remote_path + filename)
    except Exception as e:
        print('下载文件失败', e)
    sf.close()
    desktop=get_desktop()
    shutil.move(os.path.join(local_path,filename),desktop)


file_download(host,port,username,password,remote_path, local_path,uuid)
