#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import os
from struct import *

import binascii
import zlib

host_ip = "192.168.0.10"
host_port = 80
bin = 'C:\\Users\\User\\Desktop\\bin_collection\\all_leds_blink.bin'

socket_system_control_ray = socket.socket()
socket_system_control_ray.connect((host_ip, host_port))

f = open(bin, 'rb')
cnt_bytes_in_bin = os.path.getsize(bin)
print ('sending .bin...')
l = f.read(cnt_bytes_in_bin)

def crc(fileName):
    prev = 0
    for eachLine in open(fileName,"rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X"%(prev & 0xFFFFFFFF)

print(crc(bin))

cmd = 0x55
cmd_for_tx = pack('!i', cmd)
cnt_bytes_in_bin_for_tx = pack('!i', cnt_bytes_in_bin)

#socket_system_control_ray.send(bytes(cmd_for_tx))
#socket_system_control_ray.send(bytes(cnt_bytes_in_bin_for_tx))


while(1):
    print ('sending .bin...')
    socket_system_control_ray.send(bytes(l))
    l = f.read(len(f.read()))
    if len(l) < cnt_bytes_in_bin:
        break

f.close()
print ('done sending')

socket_system_control_ray.shutdown(socket.SHUT_WR)
socket_system_control_ray.close()
