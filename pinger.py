import os
import time
import socket
import ctypes

while True:
    url_or_ip = input("Enter the URL or IP address to ping: ")
    try:
        ip_address = socket.gethostbyname(url_or_ip)
    except socket.gaierror:
        ip_address = url_or_ip
    response = os.system("ping -t " + ip_address)
    if response == 0:
        print(ip_address, 'is up!')
    else:
        ctypes.windll.user32.MessageBoxW(0, f"{ip_address} is down", "Ping Result", 0)
    time.sleep(1)
