import os,datetime
from Server_Config import *
from MySQL_Model_Cls import clt_filelist,clt_filelist_his
from DB_Access import DBSession
import shutil
class load_file_indb(object):

    def __init__(self,filepath):
        self.__filepath=filepath

    def set_filetype(self,filename):
        #根据文件名设定文件类型
        if board_file_filter in filename:
            file_type = 'B'
        elif cpu_file_filter in filename:
            file_type = 'C'
        elif disk_file_filter in filename:
            if 'dynamic' in filename:
                file_type = 'DD'
            elif 'static' in filename:
                file_type = 'DS'
            else:
                file_type = 'X'
        elif installation_file_filter in filename:
            file_type = 'I'
        elif pid_file_filter in filename:
            file_type = 'P'
        elif memory_file_filter in filename:
            if 'dynamic' in filename:
                file_type = 'MD'
            elif 'static' in filename:
                file_type = 'MS'
            else:
                file_type = 'X'
        elif service_file_filter in filename:
            file_type = 'S'
        elif net_file_filter in filename:
            file_type = 'N'
        else:
            file_type = 'X'

        self.__filetype=file_type

    def __unique_file(self,filename):
        session = DBSession()
        db_result=session.query(clt_filelist).filter_by(file_name=filename).first()
        db_result_his=session.query(clt_filelist_his).filter_by(file_name=filename).first()
        # 判断数据文件是否已经入库，重复不入库
        if db_result is None and db_result_his is None:
            return True


    def load_file(self,filename):

        if self.__unique_file(filename):
            session = DBSession()
            clt_file_new_record=clt_filelist(file_name=filename,file_path=self.__filepath,file_type=self.__filetype
                                             ,file_time=datetime.datetime.now().strftime('%Y%m%d%H%M%S'),State='I')
            try:
                session.add(clt_file_new_record)
                session.commit()
            except Exception as e:
                print("录入数据库失败",e)
        else:
            print("文件重复，不录入")

    def get_filelist(self,filetype):
        session = DBSession()
        get_filelist = session.query(clt_filelist).filter(clt_filelist.State=='I').filter(clt_filelist.file_type==filetype)
        return get_filelist

    def set_filestate(self,filename,filestate):
        session=DBSession()
        single_record=session.query(clt_filelist).filter_by(file_name=filename).first()
        if single_record.State=='I':
            single_record.State=filestate
            session.commit()
        else:
            print("状态无需修改")
    def move_file(self,filename,bakpath):
        # 读取数据库中已经处理完成的记录，转移文件记录到历史表，文件转移到备份目录
        session = DBSession()
        clt_filelist_check = session.query(clt_filelist).filter(clt_filelist.file_name==filename).filter(clt_filelist.State=='O').first()
        if clt_filelist_check is not None:
            clt_filelist_his_record=clt_filelist_his(file_name=clt_filelist_check.file_name,file_path=bakup_path,
                                                     file_type=clt_filelist_check.file_type,file_time=datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
                                                     State=clt_filelist_check.State)
        else:
            print("没有找到处理完的记录")
        session.delete(clt_filelist_check)
        session.add(clt_filelist_his_record)
        session.commit()

        try:
            shutil.move(os.path.join(clt_filelist_check.file_path,clt_filelist_check.file_name),bakpath)
        except Exception as e:
            print("文件移动失败",e)