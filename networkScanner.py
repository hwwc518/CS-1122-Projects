# import socket
# import os
# import nmap

# def get_nmap(options, ip):
#     command = "nmap " + options + ip
#     process = os.popen(command)
#     results = str(process.read())
#     return results
# '''
# s = socket.socket.AF_INET, socket.SOCK_STREAM
# server = 'server name'

# def portScanner(port):
#     try:
#         s.connect((server,port))
#         return True
#     except:
#         return False

# for x in range(1,26):
#     if portScanner(x):
#         print('Port',x,'is open')
#     else:
#         print('Port',x,'is not open')
# '''
# print(get_nmap('F', '192.168.0.20'))


import nmap                         # import nmap.py module

nm = nmap.PortScanner()
host = '127.0.0.1'
nm.scan(host, '1-1024')
nm.command_line()
nm.scaninfo()

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    print('----------------------------------------------------')

for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

lport = nm[host]['tcp'].keys()   #<------ This 'proto' was changed from the [proto] to the ['tcp'].
lport.sort()
for port in lport:
    print('----------------------------------------------------')
    print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
    print('----------------------------------------------------')