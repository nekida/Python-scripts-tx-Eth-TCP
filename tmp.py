import io
from struct import *

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

#cmd_for_tx = pack('!i', cmd)

with open(bin, 'rb') as myfile:
  data = myfile.read()

#print (data)
#print (len(data))

size = (len(data) + 7).to_bytes(2, byteorder='little')

data = size + data

def crc(fileName):
  prev = 0
  for eachLine in open(fileName, "rb"):
    prev = zlib.crc32(eachLine, prev)
  return "%X" % (prev & 0xFFFFFFFF)

crc_bin = zlib.crc32(data)

print(hex(crc_bin))
print(len(data))

byte1 = crc_bin & (0xFF)
byte2 = (crc_bin >> 8) & (0xFF)
byte3 = (crc_bin >> 16) & (0xFF)
byte4 = (crc_bin >> 24) & (0xFF)

print(hex(byte1))
print(hex(byte2))
print(hex(byte3))
print(hex(byte4))

byte1 = (byte1).to_bytes(1, byteorder='little')
byte2 = (byte2).to_bytes(1, byteorder='little')
byte3 = (byte3).to_bytes(1, byteorder='little')
byte4 = (byte4).to_bytes(1, byteorder='little')

data = data + byte1 + byte2 + byte3 + byte4
print(data)
print(len(data))


while(1):
  print ('sending .bin...')
  socket_system_control_ray.send(bytes(data))
  break

#print (data)
#print (len(data))
