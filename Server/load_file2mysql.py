from Load_INDB_cls import load_file_indb
import os
from Server_Config import *
def mv_loadfile2mysql(infopath):

    filelist=os.listdir(infopath)

    for singlefile in filelist:
        mv_load=load_file_indb(infopath)
        mv_load.set_filetype(singlefile)
        mv_load.load_file(singlefile)



