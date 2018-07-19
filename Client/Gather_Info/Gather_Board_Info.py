import wmi,datetime

def Board_Info():
    c = wmi.WMI()
    borad_list=[]
    for physical_board in c.Win32_BaseBoard():
        board_dict={}
        board_dict['Collection_time'] = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        board_dict['Caption']=physical_board.Caption
        board_dict['ConfigOptions']=physical_board.ConfigOptions
        board_dict['CreationClassName']=physical_board.CreationClassName
        board_dict['Description']=physical_board.Description
        board_dict['HostingBoard']=physical_board.HostingBoard
        board_dict['Manufacturer']=physical_board.Manufacturer
        board_dict['Name']=physical_board.Name
        board_dict['PoweredOn']=physical_board.PoweredOn
        board_dict['Product']=physical_board.Product
        board_dict['Removable']=physical_board.Removable
        board_dict['Replaceable']=physical_board.Replaceable
        board_dict['RequiresDaughterBoard']=physical_board.RequiresDaughterBoard
        board_dict['SerialNumber']=physical_board.SerialNumber
        board_dict['Status']=physical_board.Status
        board_dict['Tag']=physical_board.Tag
        board_dict['Version']=physical_board.Version
        borad_list.append(board_dict)
    return borad_list
