from Client_Config import host,port,username,password,Server_command_Path,Client_command_Path
from Client.Command import command
def execute_command():
    mv_receive_command=command(host,port,username,password)
    mv_receive_command.command_download(Server_command_Path,Client_command_Path)
    mv_receive_command.command_execute()

execute_command()