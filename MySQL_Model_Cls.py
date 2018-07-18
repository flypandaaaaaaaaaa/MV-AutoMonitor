from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,DateTime
Base=declarative_base()


class board_info(Base):

    __tablename__='board_info'

    id = Column(Integer,primary_key=True,autoincrement=True)
    Client_id=Column(Integer)
    Collection_time=Column(String(100))
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




class cpu_info(Base):

    __tablename__='cpu_info'

    id = Column(Integer,primary_key=True,autoincrement=True)
    Client_id=Column(Integer)
    Collection_time=Column(String(100))
    AddressWidth = Column(String(100))
    Architecture= Column(String(100))
    AssetTag= Column(String(100))
    Availability= Column(String(100))
    Caption= Column(String(100))
    Characteristics= Column(String(100))
    CpuStatus= Column(String(100))
    CreationClassName= Column(String(100))
    CurrentClockSpeed= Column(String(100))
    CurrentVoltage= Column(String(100))
    DataWidth= Column(String(100))
    Description= Column(String(100))
    DeviceID= Column(String(100))
    ExtClock= Column(String(100))
    Family= Column(String(100))
    L2CacheSize= Column(String(100))
    L3CacheSize= Column(String(100))
    L3CacheSpeed= Column(String(100))
    Level= Column(String(100))
    LoadPercentage= Column(String(100))
    Manufacturer= Column(String(100))
    MaxClockSpeed= Column(String(100))
    Name= Column(String(100))
    NumberOfCores= Column(String(100))
    NumberOfEnabledCore= Column(String(100))
    NumberOfLogicalProcessors= Column(String(100))
    PartNumber= Column(String(100))
    PowerManagementSupported= Column(String(100))
    ProcessorId= Column(String(100))
    ProcessorType= Column(String(100))
    Revision= Column(String(100))
    Role= Column(String(100))
    SecondLevelAddressTranslationExtensions= Column(String(100))
    SerialNumber= Column(String(100))
    SocketDesignation= Column(String(100))
    Status= Column(String(100))
    StatusInfo= Column(String(100))
    SystemCreationClassName= Column(String(100))
    SystemName= Column(String(100))
    ThreadCount= Column(String(100))
    UpgradeMethod= Column(String(100))
    Version= Column(String(100))
    VirtualizationFirmwareEnabled= Column(String(100))
    VMMonitorModeExtensions= Column(String(100))


class disk_static_info(Base):

    __tablename__='disk_static_info'

    id = Column(Integer,primary_key=True,autoincrement=True)
    Client_id=Column(Integer)
    Collection_time=Column(String(100))
    BytesPerSector= Column(String(100))
    Capabilities= Column(String(100))
    CapabilityDescriptions= Column(String(100))
    Caption= Column(String(100))
    ConfigManagerErrorCode= Column(String(100))
    ConfigManagerUserConfig= Column(String(100))
    CreationClassName= Column(String(100))
    Description= Column(String(100))
    DeviceID= Column(String(100))
    FirmwareRevision= Column(String(100))
    Index= Column(String(100))
    InterfaceType= Column(String(100))
    Manufacturer= Column(String(100))
    MediaLoaded= Column(String(100))
    MediaType= Column(String(100))
    Model= Column(String(100))
    Name= Column(String(100))
    Partitions= Column(String(100))
    PNPDeviceID= Column(String(100))
    SCSIBus= Column(String(100))
    SCSILogicalUnit= Column(String(100))
    SCSIPort= Column(String(100))
    SCSITargetId= Column(String(100))
    SectorsPerTrack= Column(String(100))
    SerialNumber= Column(String(100))
    Signature= Column(String(100))
    Size= Column(String(100))
    Status= Column(String(100))
    SystemCreationClassName= Column(String(100))
    SystemName= Column(String(100))
    TotalCylinders= Column(String(100))
    TotalHeads= Column(String(100))
    TotalSectors= Column(String(100))
    TotalTracks= Column(String(100))
    TracksPerCylinder= Column(String(100))


class disk_dynamic_info(Base):

    __tablename__='disk_dynamic_info'

    id = Column(Integer,primary_key=True,autoincrement=True)
    Client_id=Column(Integer)
    Collection_time=Column(String(100))
    device= Column(String(100))
    mountpoint= Column(String(100))
    fstype= Column(String(100))
    opts= Column(String(100))
    total= Column(String(100))
    used= Column(String(100))
    free= Column(String(100))
    percent= Column(String(100))


class memory_static_info(Base):

    __tablename__='memory_static_info'
    id = Column(Integer,primary_key=True,autoincrement=True)
    Client_id= Column(Integer)
    Collection_time=Column(String(100))
    Attributes= Column(String(100))
    BankLabel= Column(String(100))
    Capacity= Column(String(100))
    Caption= Column(String(100))
    ConfiguredClockSpeed= Column(String(100))
    CreationClassName= Column(String(100))
    DataWidth= Column(String(100))
    Description= Column(String(100))
    DeviceLocator= Column(String(100))
    FormFactor= Column(String(100))
    InterleaveDataDepth= Column(String(100))
    InterleavePosition= Column(String(100))
    Manufacturer= Column(String(100))
    MemoryType= Column(String(100))
    Name= Column(String(100))
    PartNumber= Column(String(100))
    PositionInRow= Column(String(100))
    SerialNumber= Column(String(100))
    SMBIOSMemoryType= Column(String(100))
    Speed= Column(String(100))
    Tag= Column(String(100))
    TotalWidth= Column(String(100))
    TypeDetail= Column(String(100))



class memory_dynamic_info(Base):

    __tablename__='memory_dynamic_info'

    id = Column(Integer,primary_key=True,autoincrement=True)
    Collection_time=Column(String(100))
    Client_id=Column(Integer)
    available= Column(String(100))
    percent= Column(String(100))
    used= Column(String(100))
    free= Column(String(100))


class installation_info(Base):


    __tablename__='installation_info'
    id = Column(Integer,primary_key=True,autoincrement=True)
    Client_id=Column(Integer)
    Collection_time=Column(String(100))
    software= Column(String(100))


class pid_info(Base):


    __tablename__='pid_info'
    id = Column(Integer,primary_key=True,autoincrement=True)
    Client_id=Column(Integer)
    Collection_time=Column(String(100))
    PID= Column(String(100))
    memory_percent= Column(String(100))
    cpu_percent= Column(String(100))
    proc_name= Column(String(100))
    proc_exe= Column(String(1000))


class service_info(Base):


    __tablename__='service_info'
    id = Column(Integer,primary_key=True,autoincrement=True)
    Client_id=Column(Integer)
    Collection_time=Column(String(100))
    srv_name= Column(String(100))
    StartMode= Column(String(100))
    State= Column(String(100))


class net_info(Base):


    __tablename__='net_info'
    id = Column(Integer,primary_key=True,autoincrement=True)
    Client_id=Column(Integer)
    Collection_time=Column(String(100))
    IP= Column(String(100))
    Netmask= Column(String(100))
    MAC= Column(String(100))
    Gateway=Column(String(100))
    DHCP=Column(String(100))
    DNS=Column(String(100))

class clt_filelist(Base):

    __tablename__='clt_filelist'
    id = Column(Integer,primary_key=True,autoincrement=True)
    file_name= Column(String(100))
    file_path= Column(String(100))
    file_type=Column(String(20))
    file_time=Column(String(100))
    State= Column(String(100))


class clt_filelist_his(Base):
    __tablename__ = 'clt_filelist_his'
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String(100))
    file_path = Column(String(100))
    file_type = Column(String(20))
    file_time = Column(String(100))
    State = Column(String(100))

class file_type(Base):
    __tablename__ = 'file_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_type = Column(String(100))
    file_type_name = Column(String(100))

class file_state(Base):
    __tablename__ = 'file_state'
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_state = Column(String(100))
    file_state_name = Column(String(100))

