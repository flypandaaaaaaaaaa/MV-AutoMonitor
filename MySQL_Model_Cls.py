from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import  sessionmaker
import yaml
Base=declarative_base()


class board_info(Base):

    __tablename__='board_info'

    id = Column(String(100), primary_key=True)
    Caption = Column(String(100))
    ConfigOptions= Column(String(100))
    CreationClassName= Column(String(100))
    Description= Column(String(100))
    HostingBoard= Column(String(100))
    Manufacturer= Column(String(100))
    Name= Column(String(100))
    PoweredOn= Column(String(100))
    Product= Column(String(100))
    Removable= Column(String(100))
    Replaceable= Column(String(100))
    RequiresDaughterBoard= Column(String(100))
    SerialNumber= Column(String(100))
    Status= Column(String(100))
    Tag= Column(String(100))
    Version= Column(String(100))


with open ('D:\\'+'boardinfo'+'.txt','r') as f:
    list=yaml.load(f.read())


DBSession = sessionmaker(bind=engine)
session = DBSession()

with open ('D:\\'+'boardinfo'+'.txt','r') as f:
    list=yaml.load(f.read())
    temp_list=list[0]
    new_board_info = board_info(id=1,Caption=temp_list['Caption'],ConfigOptions=temp_list['ConfigOptions'],
                          CreationClassName=temp_list['CreationClassName'],Description=temp_list['Description'],
                          HostingBoard=temp_list['HostingBoard'],Manufacturer=temp_list['Manufacturer'],
                          Name=temp_list['Name'],PoweredOn=temp_list['PoweredOn'],Product=temp_list['Product'],
                          Removable=temp_list['Removable'],Replaceable=temp_list['Replaceable'],
                          RequiresDaughterBoard=temp_list['RequiresDaughterBoard'],SerialNumber=temp_list['SerialNumber'],
                          Status=temp_list['Status'],Tag=temp_list['Tag'],Version=temp_list['Version'])
    session.add(new_board_info)
    session.commit()
    session.close()
