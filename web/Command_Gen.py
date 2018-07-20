#-*-coding:utf-8-*-
from Server.DB.MySQLModel import python_script,board_info
from Server.Server_Config import WORKPATH
from Server.DB.DB_Access import  DBSession
import hashlib,uuid
from werkzeug import secure_filename

class My_Command(object):

    def __init__(self,my_id):
        self.__my_id=my_id

    def __control(self):
        with open (WORKPATH+self.__scriptname+'_'+self.__my_uniquehash+'.py','w') as f:
            f.write(self.__my_python_script)

    def __send_file(self):
        with open(WORKPATH + self.__scriptname + '_' + self.__my_uniquehash + '.py', 'w') as f:
            my_uuid = str(uuid.uuid1())
            self.uuid = my_uuid
            f.write(self.__my_argument.replace('uuid=\'\'','uuid=' + '\'' + my_uuid + '\'') + self.__my_python_script)
        my_filename=secure_filename(self.__file.filename)
        self.__file.save(WORKPATH + my_uuid + my_filename)

    def my_command(self,command,file):
        session=DBSession()
        my_python = session.query(python_script).all()
        for i in my_python:
            if i.script_name == command:
                my_python_script=i.script_context
                my_argument=i.argument
                my_scriptname=i.script_name
                break
        my_board = session.query(board_info).filter(board_info.Client_id == self.__my_id).first()
        session.close()
        if my_board.SerialNumber is None:
            print("我没有序列号，无法定位我的机器")
        else:
            self.__my_uniquehash = hashlib.md5(my_board.SerialNumber.encode('utf-8')).hexdigest()
            self.__my_python_script=my_python_script
            self.__scriptname=my_scriptname
            self.__my_argument=my_argument
            self.__file=file
            if command in ['reboot','shutdown']:
                self.__control()
            elif command in ['sendfile']:
                self.__send_file()

