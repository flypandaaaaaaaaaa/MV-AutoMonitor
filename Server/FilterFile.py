class file_filename(object):

    def __init__(self,filter):

        self.__filter=filter


    def filterfile(self,filename):

        return  self.__filter in filename
