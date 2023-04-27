import time
import paramiko
from loguru import logger


class RemoteReboot:
    def __init__(self, config):
        self.config = config

    def ssh_connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.config["ip_address"], username=self.config["username"], password=self.config["password"])
        return ssh

    def reboot(self):
        logger.info("正在重启远程主机...")
        ssh = self.ssh_connect()
        ssh.exec_command("reboot")
        ssh.close()

    def execute_shell(self):
        logger.info("重启完成，开始执行 shell 命令...")
        ssh = self.ssh_connect()
        # 在这里添加需要执行的 shell 命令
        _, stdout, stderr = ssh.exec_command("ls -l")
        logger.info("执行结果如下：")
        for line in stdout:
            logger.info(line.strip())
        ssh.close()

    def start(self):
        for i in range(self.config["loop"]):
            logger.info(f"第{i+1}次重启操作开始...")
            self.reboot()
            logger.info(f"等待 5 分钟...")
            time.sleep(300)
            with open(self.config["output"], "a") as f:
                f.write(f"{time.time()}\n")
            logger.info(f"获取到的时间戳为：{time.time()}")
            self.execute_shell()


if __name__ == '__main__':
    configs = [
        {
            "ip_address": "192.168.1.103",
            "username": "root",
            "password": "123456",
            "loop": 3,
            "output": "timestamps1.txt"
        },
        {
            "ip_address": "192.168.1.104",
            "username": "root",
            "password": "123456",
            "loop": 5,
            "output": "timestamps2.txt"
        }
    ]

    for config in configs:
        rr = RemoteReboot(config=config)
        rr.start()
