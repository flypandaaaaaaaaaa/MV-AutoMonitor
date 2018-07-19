from Info_File_Transfer import sftp
from Client_Config import *

def mv_upload():
    try:
        mv_sftp=sftp(host,port,username,password)
        mv_sftp.batch_upload(LocalPath,RemotePath)
    except Exception as e:
        print('上传失败',e)