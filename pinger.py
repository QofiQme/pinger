import ping3

ip_address = input("Enter the IP address to ping: ")
while True:
    response = ping3.ping(ip_address)
    if response is not None:
        print(ip_address, 'is up!')
    else:
        print(ip_address, 'is down.')
    time.sleep(1)
