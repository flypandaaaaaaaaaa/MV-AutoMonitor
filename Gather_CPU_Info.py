import wmi

def CPU_Info():
    c = wmi.WMI()
    cpu_list=[]
    for physical_cpu in c.Win32_Processor():
        cpu_dict={}
        cpu_dict['AddressWidth']=physical_cpu.AddressWidth
        cpu_dict['Architecture']=physical_cpu.Architecture
        cpu_dict['AssetTag']=physical_cpu.AssetTag
        cpu_dict['Availability']=physical_cpu.Availability
        cpu_dict['Caption']=physical_cpu.Caption
        cpu_dict['Characteristics']=physical_cpu.Characteristics
        cpu_dict['CpuStatus']=physical_cpu.CpuStatus
        cpu_dict['CreationClassName']=physical_cpu.CreationClassName
        cpu_dict['CurrentClockSpeed']=physical_cpu.CurrentClockSpeed
        cpu_dict['CurrentVoltage']=physical_cpu.CurrentVoltage
        cpu_dict['DataWidth']=physical_cpu.DataWidth
        cpu_dict['Description']=physical_cpu.Description
        cpu_dict['DeviceID']=physical_cpu.DeviceID
        cpu_dict['ExtClock']=physical_cpu.ExtClock
        cpu_dict['Family']=physical_cpu.Family
        cpu_dict['L2CacheSize']=physical_cpu.L2CacheSize
        cpu_dict['L3CacheSize']=physical_cpu.L3CacheSize
        cpu_dict['L3CacheSpeed']=physical_cpu.L3CacheSpeed
        cpu_dict['Level']=physical_cpu.Level
        cpu_dict['LoadPercentage']=physical_cpu.LoadPercentage
        cpu_dict['Manufacturer']=physical_cpu.Manufacturer
        cpu_dict['MaxClockSpeed']=physical_cpu.MaxClockSpeed
        cpu_dict['Name']=physical_cpu.Name
        cpu_dict['NumberOfCores']=physical_cpu.NumberOfCores
        cpu_dict['NumberOfEnabledCore']=physical_cpu.NumberOfEnabledCore
        cpu_dict['NumberOfLogicalProcessors']=physical_cpu.NumberOfLogicalProcessors
        cpu_dict['PartNumber']=physical_cpu.PartNumber
        cpu_dict['PowerManagementSupported']=physical_cpu.PowerManagementSupported
        cpu_dict['ProcessorId']=physical_cpu.ProcessorId
        cpu_dict['ProcessorType']=physical_cpu.ProcessorType
        cpu_dict['Revision']=physical_cpu.Revision
        cpu_dict['Role']=physical_cpu.Role
        cpu_dict['SecondLevelAddressTranslationExtensions']=physical_cpu.SecondLevelAddressTranslationExtensions
        cpu_dict['SerialNumber']=physical_cpu.SerialNumber
        cpu_dict['SocketDesignation']=physical_cpu.SocketDesignation
        cpu_dict['Status']=physical_cpu.Status
        cpu_dict['StatusInfo']=physical_cpu.StatusInfo
        cpu_dict['SystemCreationClassName']=physical_cpu.SystemCreationClassName
        cpu_dict['SystemName']=physical_cpu.SystemName
        cpu_dict['ThreadCount']=physical_cpu.ThreadCount
        cpu_dict['UpgradeMethod']=physical_cpu.UpgradeMethod
        cpu_dict['Version']=physical_cpu.Version
        cpu_dict['VirtualizationFirmwareEnabled']=physical_cpu.VirtualizationFirmwareEnabled
        cpu_dict['VMMonitorModeExtensions']=physical_cpu.VMMonitorModeExtensions
        cpu_list.append(cpu_dict)
    return cpu_list

CPU_Info=CPU_Info()
for CPU in CPU_Info:
    for i in CPU:
        print(i,CPU[i])

