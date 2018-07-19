def convert_db_par(*args):
    string=''
    for i in args:
        if not string:
            if type(i)==type(1):
                string=string+str(i)
            elif type(i)== type('a'):
                string=string+i
            else:
                string=string+'#'
        else:
            if type(i)==type(1):
                string=string+','+str(i)
            elif type(i)== type('a'):
                string=string+','+i
            else:
                string=string+','+'#'
    return string