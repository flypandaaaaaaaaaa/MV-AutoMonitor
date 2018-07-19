from Info_File_Transfer import sftp
from Client.Client_Config import HOST,PORT,USERNAME,PASSWORD
from Client.Client_Config import WORKPATH,REMOTE,BACKUP

def mv_upload():
    try:
        mv_sftp=sftp(HOST,PORT,USERNAME,PASSWORD)
        mv_sftp.batch_upload(WORKPATH,REMOTE,BACKUP)
    except Exception as e:
        print('上传失败',e)