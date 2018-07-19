import wmi,datetime
import psutil
c = wmi.WMI()
def memory_static_info():
    memory_static_list=[]
    for physical_memory in c.Win32_PhysicalMemory():
        memory_dict={}
        memory_dict['Collection_time'] = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        memory_dict['Attributes']=physical_memory.Attributes
        memory_dict['BankLabel'] = physical_memory.BankLabel
        memory_dict['Capacity']=physical_memory.Capacity
        memory_dict['Caption'] = physical_memory.Caption
        memory_dict['ConfiguredClockSpeed'] = physical_memory.ConfiguredClockSpeed
        memory_dict['CreationClassName'] = physical_memory.CreationClassName
        memory_dict['DataWidth'] = physical_memory.DataWidth
        memory_dict['Description'] = physical_memory.Description
        memory_dict['DeviceLocator'] = physical_memory.DeviceLocator
        memory_dict['FormFactor'] = physical_memory.FormFactor
        memory_dict['InterleaveDataDepth'] = physical_memory.InterleaveDataDepth
        memory_dict['InterleavePosition'] = physical_memory.InterleavePosition
        memory_dict['Manufacturer'] = physical_memory.Manufacturer
        memory_dict['MemoryType'] = physical_memory.MemoryType
        memory_dict['Name'] = physical_memory.Name
        memory_dict['PartNumber'] = physical_memory.PartNumber
        memory_dict['PositionInRow'] = physical_memory.PositionInRow
        memory_dict['SerialNumber'] = physical_memory.SerialNumber
        memory_dict['SMBIOSMemoryType'] = physical_memory.SMBIOSMemoryType
        memory_dict['Speed'] = physical_memory.Speed
        memory_dict['Tag'] = physical_memory.Tag
        memory_dict['TotalWidth'] = physical_memory.TotalWidth
        memory_dict['TypeDetail'] = physical_memory.TypeDetail
        memory_static_list.append(memory_dict)
    return memory_static_list

def memory_dynamic_info():
    memory_dynamic_dict={}
    mem_info=psutil.virtual_memory()
    memory_dynamic_dict['Collection_time']=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    memory_dynamic_dict['available']=mem_info[0]
    memory_dynamic_dict['percent']=mem_info[1]
    memory_dynamic_dict['used']=mem_info[2]
    memory_dynamic_dict['free']=mem_info[3]
    return memory_dynamic_dict



