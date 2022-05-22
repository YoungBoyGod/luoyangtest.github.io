# shell

2022年5月22日

基本思路

    拆解要求

    每个步骤书写成伪代码

    根据伪代码书写shell脚本

    检查与测试

代码运行方式：

    编译型：写完需要编译之后才能运行    比如C    代码--》命令

    解释型：书写完成后通过命令解释器运行 SHELL

规范习惯

    开头第一行 写命令解释器 #! 在linux中叫幻数

```shell
#！ /bin/bash

不带的话
[root@VM-16-3-centos shell]# file test.sh 
test.sh: ASCII text
带的话：
(base) [root@VM-16-3-centos shell]# file test.sh 
test.sh: Bourne-Again shell script, ASCII text executable
(base) [root@VM-16-3-centos shell]# sh test.sh 
heheh
```

    尽量不要用中文 机器可能不识别 尽量英文

    尽量不要包含**服务名**

用于系统执行脚本，比如开机执行 

```shell
 test.sh 
 chmod +x test.sh
 ./test.sh
```

sh 使用最多 本质上是bash

```shell
通用必备
```

source 或者 .替换

```shell
让环境变量生效： source/etc/profile

类似于include功能：把放在其他位置的配置文件包含进主配置文件   (先理解)
```

输入重定向

```shell
< 与 tr xargs 三剑客 sh
```

## source 和sh 区别？

```shell

```

| 方法                | 使用场景                  | 注意事项 |
| ----------------- | --------------------- | ---- |
| sh 、bash          | 通用                    |      |
| chmod + x 加执行权限执行 | 系统脚本文件执行 开机脚本之类的      |      |
| source、 .         | 让环境变量生效，实现文件包含include |      |
| 输入重定向<            | 几乎不用                  |      |

### shell中的变量

变量的本质是内存中的区域，变量名称区域的地址

不能以数字做开头

驼峰命名

多单词 中间用下划线

#### 分类

环境变量 系统定义好的 大写字母

```shell
env  #可以直接查询
export
declare
```

    常用的

```shell
PATH

(base) [root@VM-16-3-centos shell]# echo $PATH
/opt/anaconda3/bin:/opt/anaconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/opt/anaconda3/bin:/root/bin
```

```shell
UID  userid 记录用户信息 判断是不是root 安全加固里面用的多
系统脚本中会用到
```

```shell
HOSTNAME
HISTSIZE 就是记录 history命令的最大条数 实际成生产环境中要设置的小一点
HISTFILE 制定记录的位置
TIMOUT 自动断开时间 export TIMOUT=0  永不掉线
HISTCONTROL  export HISTCONTROL=ignorespace 配置完成后 只要以后的命令行前面有空格就不记录

PROMPT_COMMAND 存放的命令或者脚本在命令执行前运行   用来做日志审计非常好用

(base) [root@VM-16-3-centos shell]# export PROMPT_COMMAND=date
Sun May 22 11:59:05 CST 2022
(base) [root@VM-16-3-centos shell]# ls
test.sh
Sun May 22 11:59:08 CST 2022

root用户身份下，进行以下操作

vi /etc/profile


#在最后一行追加以下环境变量
export HISTORY_FILE=/var/log/`date '+%y-%m-%d'`.log
export PROMPT_COMMAND='{ date "+%y-%m-%d %T ##### $(who am i |awk "{print \$1\" \"\$2\" \"\$5}") #### $(pwd) #### $(history 1 | { read x cmd; echo "$cmd"; })"; } >> $HISTORY_FILE'

#保存并重新编译
source /etc/profile
```

普通变量

```shell
一般变量用带{}的形式,不带{}向后匹配容易多匹配

$day
${day}
```

与变量有关的文件

```shell
/etc/profile 存放环境变量  全局生效
/etc/bashrc  别名  全局生效
~/.bashrc 当前用户的别名
~/.bash_profile 当前用户的环境变量
```

特殊变量：匹配脚本参数 服务状态 特殊替换

| 符号     | 含义                              | 作用                                                           |
| ------ | ------------------------------- | ------------------------------------------------------------ |
| $0     | 当前的文件名                          | 脚本执行错误 给出错误提示或者使用帮助                                          |
| $n(数字) | 脚本的第几个参数                        | 命令行中传递给脚本中使用  一般就是 start stop这种的     n>10的时候就开始就需要用{} 0-9不用管 |
| $#     | 脚本参数的个数，一般就是总数                  | 主要是用来判断参数是0的时候                                               |
| $*     | 取出所有的参数，加上双引号相当于1个整体 一个参数       |                                                              |
| $@     | 取出所有的参数 加上双引号，就是每个都是独立 把每一个都取出来 |                                                              |

```shell
(base) [root@VM-16-3-centos shell]# echo  \${0..12}
$0 $1 $2 $3 $4 $5 $6 $7 $8 $9 $10 $11 $12
(base) [root@VM-16-3-centos shell]# sh 03_var_parameter.sh {a..z}
03_var_parameter.sh a b c d e f g h i a0 a1 a2
(base) [root@VM-16-3-centos shell]# more 04_var_paramter.sh 
#! /bin/bash
echo $0 $1 $2 
echo $#   脚本参数的个数
(base) [root@VM-16-3-centos shell]# sh 04_var_paramter.sh sss sss dddd
04_var_paramter.sh sss sss 3
3




(base) [root@VM-16-3-centos shell]# more 04_var_paramter.sh 
#! /bin/bash
if [ $# == 0 ];then
 echo Usage: "$0 {start|stop|restart}"
fi

(base) [root@VM-16-3-centos shell]# sh 04_var_paramter.sh 
Usage: 04_var_paramter.sh {start|stop|restart}
(base) [root@VM-16-3-centos shell]# sh 04_var_paramter.sh ssfi
#

#!/bin/bash 
# $* $@ 加上“” 之后不同 
echo start:$*  相当于一个 全部取出
echo paramter: $@  就一个


echo "$*"
for n in "$*"
do
 echo $n
done

echo "$@"
for n in "$@"
do
 echo $n
done
#
```

状态

| 符号  | 含义                    |     |
| --- | --------------------- | --- |
| $?  | 上一个脚本返回值              |     |
| $!  | 上一个运行脚本的pid           |     |
| $$  | 当前运行脚本的pid            |     |
| $_  | 上一个命令或者脚本的最后一个参数 esc+ | \   |
