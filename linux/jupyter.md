# 个人虚拟机环境安装

## 安装jupyter

使用anaconda 进行部署 使用清华源方式部署，这种部署方式本地可以使用，但是资源较小的虚拟机还是考虑一下放弃。我们就使用jupyter 就可以

#### 安装步骤
    初始安装pip 和 使用pip安装 jupyter
    apt-get install python3-pip
    pip install jupyter
    
    添加环境变量 
    echo export PATH=$PATH:/home/{youname}/.local/bin
    #生成配置文件
    jupyter notebook --generate-config
    
    生成sha1秘钥
    ipython
    from notebook.auth import passwd
    passwd()
    输入你的密码 
    然后把生产的sha1密码保存下来
    exit()

    修改jupyter配置
    vi .jupyter/jupyter_notebook_config.py 
    搜索并去掉注释修改
    c.NotebookApp.password = u'sha1:XXXXXX'
    c.NotebookApp.port = xxxx
    修改成监听本机所有地址
    c.NotebookApp.ip = '*'

    输入启动
    这种只能是一次性,可以先运行试下效果
    jupyter notebook --ip=0.0.0.0 --no-browser --allow-root
    打开浏览器输入地址+端口 密码登录

####添加开机自启动

```shell
添加service文件
luo@dev:~$ sudo vi  /etc/systemd/system/jupyter.service
[Unit]
Description=Jupyter Notebook
After=network.target
[Service]
Type=simple
ExecStart=/home/luo/.local/bin/jupyter-notebook --config=/home/luo/.jupyter/jupy
ter_notebook_config.py --no-browser

User=luo
Group=luo
WorkingDirectory=/home/luo/
#文件路径名
Restart=always
RestartSec=10
[Install]
WantedBy=multi-user.target
保存退出

#enable system service

systemctl  enable jupyter.service
systemctl  start jupyter.service
```





##### 出现的问题

###### 缺少环境变量
    luo@dev:~$ jupyter notebook --generate-config

    Command 'jupyter' not found, but can be installed with:

    snap install jupyter       # version 1.0.0, or
    apt  install jupyter-core  # version 4.6.3-3

    See 'snap info jupyter' for additional versions.
###### 解决方法

```shell
查找jupyter 所在位置
luo@dev:~$ find -name jupyter
./.local/etc/jupyter
./.local/bin/jupyter
./.local/share/jupyter

```
    添加环境变量
    echo export PATH=$PATH:/home/{youname}/.local/bin

    使能环境变量
    source ~/.bashrc

###### markupsafe软件包版本过低

```shell
luo@dev:~$ jupyter notebook
Traceback (most recent call last):
  File "/home/luo/.local/bin/jupyter-notebook", line 5, in <module>
    from notebook.notebookapp import main
  File "/home/luo/.local/lib/python3.8/site-packages/notebook/notebookapp.py", line 43, in <module>
    from jinja2 import Environment, FileSystemLoader
  File "/usr/lib/python3/dist-packages/jinja2/__init__.py", line 33, in <module>
    from jinja2.environment import Environment, Template
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 15, in <module>
    from jinja2 import nodes
  File "/usr/lib/python3/dist-packages/jinja2/nodes.py", line 23, in <module>
    from jinja2.utils import Markup
  File "/usr/lib/python3/dist-packages/jinja2/utils.py", line 656, in <module>
    from markupsafe import Markup, escape, soft_unicode
ImportError: cannot import name 'soft_unicode' from 'markupsafe' (/home/luo/.local/lib/python3.8/site-packages/markupsafe/__init__.py)

```
###### 解决方法
卸载重装    

    pip uninstall markupsafe
    pip install markupsafe


