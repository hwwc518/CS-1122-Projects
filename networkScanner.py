#scans all ports
 
import socket,sys,time,datetime,argparse,os
from netaddr import *
flag = 0
os.system('clear')
def checkIP(ip):

    host = str(ip)
    ip = str(ip)
    start_port = 1
    end_port = 1000

    print("host: ", host, ' ip: ', ip)

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
    
     
    if (flag):
        print "Scanning common ports on %s" % (host)
    else:
        print "Scanning %s from port %s - %s: " % (host, start_port, end_port)
     
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
     
        print "\tScan Report: %s" %(host)
      
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

allips = []
for ip in IPNetwork('128.238.66.0/24'):
    allips.append(ip)
    print(ip)

for ip in allips:
    checkIP(ip)

