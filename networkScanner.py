#===============================First Program==============================

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

#=========================SECOND PROGRAM-Find open ports=======================================

# import nmap                         # import nmap.py module

# nm = nmap.PortScanner()
# host = '127.0.0.1'
# nm.scan(host, '1-1024')
# nm.command_line()
# nm.scaninfo()
# dictionary_of_stuff = {}


# for host in nm.all_hosts():
#     print('----------------------------------------------------')
#     print('Host : %s (%s)' % (host, nm[host].hostname()))
#     print('State : %s' % nm[host].state())
#     print('----------------------------------------------------')

# for proto in nm[host].all_protocols():
#         print('----------')
#         print('Protocol : %s' % proto)

# lport = nm[host]['tcp'].keys()   #<------ This 'proto' was changed from the [proto] to the ['tcp'].
# lport.sort()
# for port in lport:
#     print('----------------------------------------------------')
#     print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
#     print('port2', port)

#!/usr/bin/python
 
# __author__: Mansoor (manz@digitz.org)
# Visit digitz.org
# Licence: Do whatever you want with it, modify, redistribute, publish in your blog, or whatever
# If you could provide a link back to this article, that would be great though
 
#====================Find and guess open ports=============================
 
import socket,sys,time,datetime,argparse,os
flag = 0
os.system('clear')

print "Computers on the same subnet:"
print [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]
# arrayIP = []
# arrayIP.append(ip)
# print ('')

# line = "+" * 80
# desc = line+'''\nA Simple port scanner that works!! (c) digitz.org
#     Example usage: python port_scanner.py example.com 1 1000
#     The above example will scan the host \'example.com\' from port 1 to 1000
#     To scan most common ports, use: python port_scanner.py example.com\n'''+line+"\n"
 
# parser = argparse.ArgumentParser(description = desc, formatter_class=argparse.RawTextHelpFormatter)
# parser.add_argument('host', metavar='H', help='Host name you want to scan')
# parser.add_argument('startport', metavar='P1', nargs='?', help='Start scanning from this port')
# parser.add_argument('endport', metavar='P2', nargs='?',help='Scan until this port')
# args = parser.parse_args()
 
# host = args.host
# ip = socket.gethostbyname(host)

host = '127.0.0.1'
ip = '127.0.0.1'
start_port = 1
end_port = 1000

print("host: ", host, ' ip: ', ip)


# if (args.startport) and args.endport :
#     start_port = int(args.startport)
#     end_port = int(args.endport)
# else:
#     flag = 1
 
open_ports = []
common_ports = {
    '7': 'Echo',
    '19': 'Chargen',
    '21': 'FTP',
    '22': 'SSH',
    '23': 'TELNET',
    '25': 'SMTP',
    '43': 'WHOIS',
    '53': 'DNS',
    '69': 'TFTP',
    '70': 'Gopher',
    '79': 'Finger',
    '80': 'HTTP',
    '109': 'POP2',
    '110': 'POP3',
    '123': 'NTP',
    '135': 'Microsoft RPC'
,
    '137': 'NETBIOS-NS',
    '138': 'NETBIOS-DGM',
    '139': 'NETBIOS-SSN',
    '143': 'IMAP',
    '156': 'SQL-SERVER',
    '201': 'AppleTalk',
    '389': 'LDAP',
    '443': 'HTTPS',
    '445': 'Microsoft DS',
    '513': 'rlogin',

    '514': 'syslog',
    '540': 'UUCP',

    '546': 'DHCP-CLIENT',
    '547': 'DHCP-SERVER',
    '631': 'Internet Printing',
    '902': 'VMware Server',
    '989': 'FTP',
    '995': 'POP3-SSL',
    '993': 'IMAP-SSL',
    '2086': 'WHM/CPANEL',
    '2087': 'WHM/CPANEL',
    '2082': 'CPANEL',
    '2083': 'CPANEL',
    '3306': 'MYSQL',
    '8443': 'PLESK',
    '10000': 'VIRTUALMIN/WEBMIN'
}
 
starting_time = time.time()
#print "+" * 40
#print "\tSimple Port Scanner..!!!"
#print "+" * 40
 
if (flag):
    print "Scanning common ports on %s" % (host)
else:
    print "Scanning %s from port %s - %s: " % (host, start_port, end_port)
#print "Scanning started at %s" %(time.strftime("%I:%M:%S %p"))
 
def check_port(host, port, result = 1):
    try:
        thesock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        thesock.settimeout(0.5)
        r = thesock.connect_ex((host, port))   
        if r == 0:
            result = r
        thesock.close()
    except Exception, e:
        pass
 
    return result
 
def get_service(port):
    theport = str(port)
    if theport in common_ports: 
        return common_ports[theport]
    else:
        return 0
 
 
try:
    print "Scan in progress.."
    print "Connecting to Port: ",
 
    if flag:
        for p in sorted(common_ports):
            sys.stdout.flush()
            p = int(p)
            print p,    
            response = check_port(host, p)
            if response == 0:
                open_ports.append(p)
            #if not p == end_port:
                sys.stdout.write('\b' * len(str(p)))
    else:
        
        for p in range(start_port, end_port+1):
            sys.stdout.flush()
            print p,
            response = check_port(host, p)
            if response == 0:
                open_ports.append(p)
            if not p == end_port:
                sys.stdout.write('\b' * len(str(p)))
 
    #print "\nScanning completed at %s" %(time.strftime("%I:%M:%S %p"))
    #ending_time = time.time()
    #total_time = ending_time - starting_time
    #print "=" * 40
    print "\tScan Report: %s" %(host)
    #print "=" * 40
    # if total_time <= 60:
    #     total_time = str(round(total_time, 2))
    #     print "Scan Took %s seconds" %(total_time)
    # else:
    #     total_time = total_time / 60
    #     print "Scan Took %s Minutes" %(total_time)
        
    if open_ports:
        print "Open Ports: "
        for i in sorted(open_ports):
            service = get_service(i)
            if not service:
                service = "Unknown"
            print "\t%s %s: Open" % (i, service)
    else:
        print "No ports found"
 
except KeyboardInterrupt:
    print "Exiting "   
    sys.exit(1)
#     print('----------------------------------------------------')
