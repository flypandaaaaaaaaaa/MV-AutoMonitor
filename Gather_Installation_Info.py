import winreg
#-*- coding:utf-8 -*-
sub_key = ['SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
           'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall']

software_name = []

for i in sub_key:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, i, 0, winreg.KEY_ALL_ACCESS)
    for j in range(0, winreg.QueryInfoKey(key)[0] - 1):
        try:
            key_name = winreg.EnumKey(key, j)
            key_path = i + '\\' + key_name
            each_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
            DisplayName, REG_SZ = winreg.QueryValueEx(each_key, 'DisplayName')
            software_name.append(DisplayName)
        except WindowsError:
            pass


software_name = list(set(software_name))
software_name = sorted(software_name)

for result in software_name:
    print(result)
