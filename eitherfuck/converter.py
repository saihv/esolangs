import sys

cmds = ['+','-','>','<','[',']','.',',']

def minify(code):
    return list(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))

def opposite(cmd):
    if cmds.index(cmd) % 2 == 0:
        return cmds[cmds.index(cmd) + 1]
    else:
        return cmds[cmds.index(cmd) - 1]

def convert(fileName):
    f = open(fileName, 'r')
    code = minify(f.read())
    ctr = 0

    EFcode = ['0']
    while ctr <= len(code):
        EFcode.append(code[ctr])
        ctr += 1
        EFcode = [opposite(code[ctr])] + EFcode if ctr < len(code) else ['#'] + EFcode
        ctr += 1
    return EFcode

def main():
    if len(sys.argv) == 2:
        fileName = sys.argv[1]
        EFcode = convert(fileName)
        codestring = ''.join(map(str, EFcode))
        EFfile = open("converted.ef", "w")
        EFfile.write(codestring)
        EFfile.close()
    else:
        print("Please provide path to BF file that needs converting.")

if __name__ == '__main__': main()
