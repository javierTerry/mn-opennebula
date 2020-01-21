#!/usr/bin/python3

import oca

client = oca.Client("virtualizacion:V1rtu4l$", "http://192.168.20.6:2633/RPC2")
print client.version()

vm_pool = oca.Host(client)

vm_pool.info()
for vm in vm_pool:
    print "%s (memory: %s MB)" % ( vm.name, vm.template.memory)

print client.version()


CTLGRFS_PROD01
CTLGRFS_PROD02



DISK = [
  ALLOW_ORPHANS = "NO",
  CLONE = "YES",
  CLONE_TARGET = "SYSTEM",
  CLUSTER_ID = "0,100,101",
  DATASTORE = "HDD-Images",
  DATASTORE_ID = "103",
  DEV_PREFIX = "vd",
  DISK_ID = "0",
  DISK_SNAPSHOT_TOTAL_SIZE = "0",
  DISK_TYPE = "FILE",
  DRIVER = "raw",
  IMAGE = "CentOS 7 - Container",
  IMAGE_ID = "41",
  IMAGE_STATE = "2",
  LN_TARGET = "SYSTEM",
  ORIGINAL_SIZE = "3072",
  READONLY = "NO",
  SAVE = "NO",
  SIZE = "3072",
  SOURCE = "/var/lib/one//datastores/103/7bfeabad2d167e02de4024c6c5a2c8da",
  TARGET = "vda",
  TM_MAD = "ssh",
  DISK_TYPE = "FILE" ]


  mn_portales1      21:00:00:1b:32:80:24:ce


centos7
8@8

30 Gb

172.21.48.12


172.20.36.138
172.20.36.144
172.20.42.97
172.20.42.98
 
172.28.76.133  172.28.97.171


02:00:ac:15:30:15




