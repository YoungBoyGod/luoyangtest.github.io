import argparse
import time
import os
import redfish

"""
when you use this script you may need 
pip install argparse 
pip install redfish 
-------------------
then python server_bmc_reboot.py xx(52 53 54 215 your server ip num)

"""

ip_52 = {"login_host": "https://10.2.32.zz",
         "login_account": "ADMIN", "login_password": "ADMIN"}
ip_53 = {"login_host": "https://10.2.32.x",
         "login_account": "ADMIN", "login_password": "ADMIN"}
ip_54 = {"login_host": "https://10.2.32.54",
         "login_account": "admin", "login_password": "admin"}
ip_215 = {"login_host": "https://10.2.27.",
          "login_account": "admin", "login_password": "admin"}

dict_info_all = {"52": ip_52, "53": ip_53, "54": ip_54}


def power_reset_bmc(ip_num):
    poweroff = {"ResetType": "GracefulShutdown"}
    poweron = {"ResetType": "On"}
    REDFISH_OBJ = redfish.redfish_client(base_url=dict_info_all.get(ip_num).get("login_host"),
                                         username=dict_info_all.get(ip_num).get("login_account"),
                                         password=dict_info_all.get(ip_num).get("login_password"),
                                         default_prefix='/redfish/v1')
    REDFISH_OBJ.login(auth="session")
    # body = {"ResetType": "ForceRestart"}
    response_off = REDFISH_OBJ.post(
        "/redfish/v1/Systems/1/Actions/ComputerSystem.Reset", body=poweroff)
    print(response_off)
    # poweroff is automatic in 60s
    time.sleep(70)
    print("wait for 70s then start")
    response_on = REDFISH_OBJ.post(
        "/redfish/v1/Systems/1/Actions/ComputerSystem.Reset", body=poweron)
    print(response_on)
    print("this cost about 2-5 min")

    for i in range(0, 5):
        os.system(f"ping -c 1 10.2.32.{ip_num}")

    REDFISH_OBJ.logout()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reboot your sever")
    parser.add_argument("ip", type=str, help="input 52 or 53 or 54 or 215"
                                             "52:chaowei intel 53:chaowei amd 54:langchao intel  215:langchao amd")
    args = parser.parse_args()
    # print(args)
    power_reset_bmc(args.ip)
    print(args.ip)
