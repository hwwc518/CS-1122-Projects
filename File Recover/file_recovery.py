def pdfRecovery(filename):

    file = open(filename,'rb')


    header = [0x25, 0x50, 0x44, 0x46]
    ftrone = [0x0a, 0x25, 0x25, 0x45, 0x4f, 0x46]
    ftrtwo = [0x0a, 0x25, 0x25, 0x45, 0x4f, 0x46, 0x0a]
    ftrthr = [0x0d, 0x0a, 0x25, 0x25, 0x45, 0x4f, 0x46, 0x0d, 0x0a]
    ftrfur = [0x0d, 0x25, 0x25, 0x45, 0x4f, 0x46, 0x0d]
    footer = [ftrone,ftrtwo,ftrthr,ftrfur]

    done = False
    binaryvalues = []
    counter = 0
    action = 0
    match = [0,0,0,0]
    name = 'name'

    for line in file:
        for i in line:
            if(action == 0):
                if( i == header[counter]):
                    counter+=1
                else:
                    counter = 0
                if(counter == 4):
                    action = 1
                    counter = 0
                    binaryvalues+= header
            elif(action == 1):
                binaryvalues.append(i)
                if(match[1] < len(ftrtwo) and i == ftrtwo[match[1]]):
                    match[1] += 1
                elif(match[0] < len(ftrone) and i == ftrone[match[0]]):
                    match[0] += 1
                elif(match[2] < len(ftrthr) and i == ftrthr[match[2]]):
                    match[2] += 1
                elif(match[3] < len(ftrfur) and i == ftrfur[match[3]]):
                    match[3] += 1
                else:
                    match = [0,0,0,0]

                if(match[1] == len(ftrtwo)):
                    action = 0
                    match = [0,0,0,0]
                    done = True
                elif(match[0] == len(ftrone)):
                    action = 0
                    match = [0,0,0,0]
                    done = True
                elif(match[2] == len(ftrthr)):
                    action = 0
                    match = [0,0,0,0]
                    done = True
                elif(match[3] == len(ftrfur)):
                    action = 0
                    match = [0,0,0,0]
                    done = True
        if (done):
            pdf = bytes(binaryvalues)
            name = name+ '1'
            pdffile = open(name + '.pdf','wb')
            pdffile.write(pdf)
            pdffile.close()
            binaryvalues = []
            done = False

    file.close()

def pngRecovery(filename):
    file = open(filename,'rb')
    
    header = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]
    footer = [0x49, 0x45, 0x4e, 0x44, 0xae, 0x42, 0x60, 0x82]
    binaryvalues = []
    counter = 0
    action = 0
    done = False
    name = 'paint'

    for line in file:    
        for i in line:
            if(action == 0):
                if( i == header[counter]):
                    counter += 1
                else:
                    counter = 0
                if( counter == 8):
                    action = 1
                    counter = 0
                    binaryvalues += header
            elif(action == 1):
                binaryvalues.append(i)
                if( i == footer[counter]):
                    counter += 1
                else:
                    counter = 0
                if(counter == 8):
                    action = 0
                    counter = 0
                    done = True
        if (done):
            string = bytes(binaryvalues)
            name = name + '1'
            pngfile = open(name + '.png','wb')
            pngfile.write(string)
            pngfile.close()
            done = False
            binaryvalues = []
    file.close()


pdfRecovery('cyber_security_file_recovery')
pngRecovery('cyber_security_file_recovery')
