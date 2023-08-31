#!/bin/bash

# 定义变量
NFS_SERVER=xx.xx.xx.xx
SHARE_DIR=/nas/nas 
MOUNT_DIR=/home/$USER/nas01

# 检查挂载点是否存在,不存在则创建
if [ ! -d "$MOUNT_DIR" ]; then
  mkdir -p "$MOUNT_DIR"
fi

# 在/etc/fstab中添加挂载配置
if ! grep -q "$NFS_SERVER:$SHARE_DIR $MOUNT_DIR" /etc/fstab; then
  echo "$NFS_SERVER:$SHARE_DIR $MOUNT_DIR nfs vers=3 0 0" >> /etc/fstab
fi

# 挂载所有fstab中的挂载点
mount -a

# 检查指定目录是否成功挂载
if mount | grep -q "$MOUNT_DIR"; then
  echo "NFS directory mounted successfully."
else
  echo "Failed to mount NFS directory."
fi
