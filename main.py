from network import LoRa
import socket
import time
import pycom
from machine import Pin
from dht import DTH

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
while True:
    th = DTH('P3', 0)
    time.sleep(2)
    result = th.read()
    if result.is_valid():
        data = [result.temperature, result.humidity]
        print(data)
        s.send(str(data))
        time.sleep(2)
