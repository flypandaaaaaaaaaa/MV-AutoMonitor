import socket, getpass, datetime, yaml, uuid
class all_info_gen(object):


    def __init__(self,info_func,info_name,file_gen_path,Client_ID,File_Name_Subfix):
        self.__info_func=info_func
        self.__info_name=info_name
        self.__file_gen_path=file_gen_path
        self.__Client_ID=Client_ID
        self.__File_Name_Subfix=File_Name_Subfix


    # 客户端号+计算机名+登陆用户名+信息类型+全局唯一串号+日期.txt

    def gen_file(self):
        info_list=self.__info_func
        yaml_doc=yaml.dump(info_list)
        with open (self.__file_gen_path+self.__Client_ID+'_'+socket.gethostname()+'_'+getpass.getuser()+'_'+self.__info_name+'_'
                   +str(uuid.uuid1())+'_'+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+self.__File_Name_Subfix,'w') as f:
            f.write(yaml_doc)