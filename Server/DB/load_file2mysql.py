from Server.DB.LoadInDB import LoadFile
import os


def mv_loadfile2mysql(infopath):

    filelist=os.listdir(infopath)

    for singlefile in filelist:
        mv_load=LoadFile(infopath)
        mv_load.set_filetype(singlefile)
        mv_load.load_file(singlefile)



