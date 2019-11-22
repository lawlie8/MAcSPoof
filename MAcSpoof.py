import os
import sys
import subprocess
import time
import random
import ctypes, sys
import re
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    dl = []
    ml = []
    Adapterlist = []
    Addlist = []
    os.system('ipconfig /all > ip.txt')
    x = open("ip.txt",'r+')
    hu = x.readlines()
    line_numbers = len(hu)
    for i in range(0,line_numbers):
        dev_des = hu[i].find('Description')
        device = hu[i][dev_des:dev_des + 800]
        device = device.strip(':').split('\n')
        #device = device.split('\n')
        device = ''.join(device)
        dl.append(device)
    for r in dl:
        if r != '':
            r = r.split('Description . . . . . . . . . . . : ')
            r = ''.join(r)
            Adapterlist.append(r)
    x = open("ip.txt",'r+')
    hu = x.readlines()
    line_numbers = len(hu)
    for j in range(0,line_numbers):
        dev_des = hu[j].find('Physical Address')
        device = hu[j][dev_des:dev_des + 80]
        device = device.strip(':')
        device = device.split('\n')
        device = ''.join(device)
        ml.append(device)
    for m in ml:
        if m != '':
            m = m.split('Physical Address. . . . . . . . . : ')
            m = ''.join(m)
            #print(r)
            Addlist.append(m)
    for i,k,h in zip(range(1,len(Addlist)+1),Addlist,Adapterlist):
        print(i,k,h)
    x.close()
    os.system('del ip.txt')

    while True:
        try:
            choice = int(input('Choose Device:->'))
            if choice > len(Addlist):
                print("Device out of range")
            else:
                break
        except ValueError as er:
            print(er)
    while True:
        rand_man = int(input('Enter 1 for random assignment 2 for manual:\t'))
        if rand_man == 1:
            random_mac = "02"
            list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            for i in range(0,10):
                x = random.choice(list)
                random_mac = random_mac + x
        break
        if rand_man == 2:
            while True:
                mac1 = input()
                if len(mac1) != 10:
                    print('\nmac to long use 10 characters\n')
                if mac1 in list:
                    random_mac = mac1
                    break
                else:
                    print('enter characters from list',list)
                break

    list = [
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0000' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0001' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0002' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0003' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0004' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0005' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0006' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0007' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0008' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0009' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0010' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0011' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0012' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0013' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0014' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0015' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0016' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0017' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0018' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0019' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0020' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0021' -Name NetworkAddress",
    r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0022' -Name NetworkAddress",
    ]

    i2 = Addlist[choice - 1].split('-')
    cscs = Addlist[choice -1]
    i2 = ''.join(i2)
    for i in list:
        k = i.replace('NetworkAddress','DriverDesc')
        j = i.replace('NetworkAddress','OriginalNetworkAddress')
        cou = os.popen(i).read().split('\n')
        cou = str(''.join(cou))
        if cou.split(' ') == i2.split(' '):
            if os.popen(k).read().split('\n')[0] == Adapterlist[choice - 1].strip(' '):
                i = i.replace('Get-ItemPropertyValue','Set-ItemProperty')

                try:
                    os.system(i + " -Value "+ random_mac)
                except:
                    i = i.replace('NetworkAddress','OriginalNetworkAddress')
                    os.system(i + " -Value "+ random_mac)
                break
        elif os.popen(j).read().split('\n')[0] == cscs.strip(' '):
            if os.popen(k).read().split('\n')[0] == Adapterlist[choice - 1].strip(' '):
                i = i.replace('Get-ItemPropertyValue','Set-ItemProperty')
                i = i.replace('NetworkAddress','OriginalNetworkAddress')
                os.system(i + " -Value "+ cscs)

    try:
        os.system('powershell netsh interface set interface name="Wi-Fi" admin=disabled')
        os.system('powershell netsh interface set interface name="Wi-Fi" admin=enabled')
        os.system('powershell netsh interface set interface name="tap" admin=disabled')
        os.system('powershell netsh interface set interface name="tap" admin=enabled')
        os.system('powershell netsh interface set interface name="Ethernet" admin=disabled')
        os.system('powershell netsh interface set interface name="Ethernet" admin=enabled')
    except:
        print('Problem at restarting device do it manually\n')
        print("Enter to Continue\n")
        lahaghakjgh = input()

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
is_admin()
