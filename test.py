import psutil,Gather_Disk_Info

list11=Gather_Disk_Info.disk_dynamic_info()
print(list11)
k=0
for disk in psutil.disk_partitions():
    print(disk)
    k=k+1
print(k)