131import time
import paramiko
import os
import subprocess
import re

dict_switch = {'154': '1', '140': '2', '112': '3', '156': '4', '128': '5', '158': '6', '155': '7', '106': '8', '124': '9', '117': '10', '129': '11', '138': '12', '131': '13', '157': '14', '141': '15', '105': '16', '146': '17', '119': '18', '109': '19', '120': '20', '103': '21', '143': '22', '144': '23', '145': '24', '104': '25', '139': '26', '159': '27', '00028': '28', '00029': '29', '00030': '30', '00031': '31', '00032': '32'}


def ssh_server(command):
    hostname = "10.2.32.251"
    username = "public"
    password = "bluepublic"
    paramiko.util.log_to_file("idc_pc_switch.log")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(hostname=hostname, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read())
    ssh.close()
    stdin.close()

def ping_server(n,ip):
    
    ip_addr="10.2.32."+ip
    for i in range(0,n):
        p=subprocess.run(["ping","-c","1","-w","2",ip_addr],stdout=subprocess.PIPE)
        pattern="(\d*) packets transmitted, (\d*) received, (\d*)% packet loss, time (\d*)ms"   
        s=re.findall(pattern, str(p.stdout.decode("utf8")))
    
        if int(list(s[0])[2]) == 100:
            print(f"{ip_addr} 不通")

        else:
            print(f"{ip_addr} 通")



if __name__ == "__main__":
    ip_num = input("输入ip地址后两或三位,比如10.2.32.139,请输入139:\n")
    switch_num=dict_switch.get(ip_num)
    choice_switch = input("输入开关选项:off on reboot:\n 说明:\noff关机 on开机 reboot关机再开机:\n")
    if choice_switch =="off":
        ssh_server(f"python switch_off.py -i {switch_num}") # 时延10s
        print("wait 5 seconds")
        time.sleep(5)
        ping_server(2,ip_num)

    elif choice_switch =="on":
        ssh_server(f"python switch.py -i {switch_num}") # 时延是1.5s
        print("每60s检测一次ping,一共检查5次")
        for i in range(0,5):
            time.sleep(60)
            ping_server(1,ip_num)
    elif choice_switch == "reboot":
        ssh_server(f"python switch_off.py -i {switch_num}")
        time.sleep(5)
        ssh_server(f"python switch.py -i {switch_num}")
        print("每60s检测一次ping,一共检查5次")
        for i in range(0,5):
            time.sleep(60)
            ping_server(1,ip_num)
