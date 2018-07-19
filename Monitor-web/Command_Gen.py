#-*-coding:utf-8-*-
from Server.MySQL_Model_Cls import python_script,board_info
from Server_Config import command_path
from DB_Access import  DBSession
import hashlib,uuid

class My_Command(object):

    def __init__(self,my_id):
        self.__my_id=my_id

    def control_command(self,command):
        session=DBSession()
        my_python=session.query(python_script).filter(python_script.script_name==command).first()#获取重启命令的脚本内容
        my_board=session.query(board_info).filter(board_info.Client_id==self.__my_id).first()#获取用户的主板信息
        if my_board.SerialNumber is None:
            print("我没有序列号，无法定位我的机器")
        else:
            myuniquehash = hashlib.md5(my_board.SerialNumber.encode('utf-8')).hexdigest()#生成用户对应的hash
            with open (command_path+command+'_'+myuniquehash+'.py','w') as f:
                f.write(my_python.script_context)
        session.close()

    def send_file(self):
        session = DBSession()
        my_python = session.query(python_script).filter(python_script.script_name == command).first()  # 获取重启命令的脚本内容
        my_board = session.query(board_info).filter(board_info.Client_id == self.__my_id).first()  # 获取用户的主板信息
        if my_board.SerialNumber is None:
            print("我没有序列号，无法定位我的机器")
        else:
            myuniquehash = hashlib.md5(my_board.SerialNumber.encode('utf-8')).hexdigest()  # 生成用户对应的hash
            with open(command_path + command + '_' + myuniquehash + '.py', 'w') as f:
                my_uuid = str(uuid.uuid1())
                self.uuid = my_uuid
                f.write(my_python.argument.replace('uuid=\'\'','uuid=' + '\'' + my_uuid + '\'') + my_python.script_context)
        session.close()


