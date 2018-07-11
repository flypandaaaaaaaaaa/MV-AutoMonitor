import wmi

def Disk_Info():
    c = wmi.WMI()
    disk_list=[]
    for physical_disk in c.Win32_DiskDrive():
        disk_dict={}
        disk_dict['BytesPerSector']=physical_disk.BytesPerSector
        disk_dict['Capabilities']=physical_disk.Capabilities
        disk_dict['CapabilityDescriptions'] = physical_disk.CapabilityDescriptions
        disk_dict['Caption'] = physical_disk.Caption
        disk_dict['ConfigManagerErrorCode'] = physical_disk.ConfigManagerErrorCode
        disk_dict['ConfigManagerUserConfig'] = physical_disk.ConfigManagerUserConfig
        disk_dict['CreationClassName'] = physical_disk.CreationClassName
        disk_dict['Description'] = physical_disk.Description
        disk_dict['DeviceID'] = physical_disk.DeviceID
        disk_dict['FirmwareRevision'] = physical_disk.FirmwareRevision
        disk_dict['Index'] = physical_disk.Index
        disk_dict['InterfaceType'] = physical_disk.InterfaceType
        disk_dict['Manufacturer'] = physical_disk.Manufacturer
        disk_dict['MediaLoaded'] = physical_disk.MediaLoaded
        disk_dict['MediaType'] = physical_disk.MediaType
        disk_dict['Model'] = physical_disk.Model
        disk_dict['Name'] = physical_disk.Name
        disk_dict['Partitions'] = physical_disk.Partitions
        disk_dict['PNPDeviceID'] = physical_disk.PNPDeviceID
        disk_dict['SCSIBus'] = physical_disk.SCSIBus
        disk_dict['SCSILogicalUnit'] = physical_disk.SCSILogicalUnit
        disk_dict['SCSIPort'] = physical_disk.SCSIPort
        disk_dict['SCSITargetId'] = physical_disk.SCSITargetId
        disk_dict['SectorsPerTrack'] = physical_disk.SectorsPerTrack
        disk_dict['SerialNumber'] = physical_disk.SerialNumber
        disk_dict['Signature'] = physical_disk.Signature
        disk_dict['Size'] = physical_disk.Size
        disk_dict['Status'] = physical_disk.Status
        disk_dict['SystemCreationClassName'] = physical_disk.SystemCreationClassName
        disk_dict['SystemName'] = physical_disk.SystemName
        disk_dict['TotalCylinders'] = physical_disk.TotalCylinders
        disk_dict['TotalHeads'] = physical_disk.TotalHeads
        disk_dict['TotalSectors'] = physical_disk.TotalSectors
        disk_dict['TotalTracks'] = physical_disk.TotalTracks
        disk_dict['TracksPerCylinder'] = physical_disk.TracksPerCylinder
        disk_list.append(disk_dict)
        return disk_list
disk_list=Disk_Info()
for disk in disk_list:
    for disk_item in disk:
        print(disk_item,':',disk[disk_item])