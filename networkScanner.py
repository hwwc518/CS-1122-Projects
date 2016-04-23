import socket
import os

def get_nmap(options, ip):
    command = "nmap " + options + ip
    process = os.popen(command)
    results = str(process.read())
    return results
'''
s = socket.socket.AF_INET, socket.SOCK_STREAM
server = 'server name'

def portScanner(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(1,26):
    if portScanner(x):
        print('Port',x,'is open')
    else:
        print('Port',x,'is not open')
'''
print(get_nmap('F', '54.186.250.79'))

