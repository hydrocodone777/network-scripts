import os, ipaddress 
 
os.system('clear')
 
while True:
    ip = input('Enter IP Address: ')
    try: 
        print(ipaddress.ip_address(ip))
        print(ip + ' is a valid IP address.')
        print('press Q to exit')
    except: 
        print:('-' *50)
        print(ip + ' is not a valid address')
    finally: 
        if ip =='q':
           print('Script Finished')
           break
