import sys
import winsound

freq = {
    '+': 'c1',
    '-': 'g1',
    '<': 'd1',
    '>': 'a1',
    '[': 'e1',
    ']': 'b1',
    '.': 'f1',
    ',': 'c2'
    }

def play(EFcode):
    midPtr = int(len(EFcode)/2)
    ctr = 1
    while ctr <= midPtr:
        #winsound.Beep(freq[EFcode[midPtr+ctr]], 200) if EFcode[midPtr+ctr] != '#' else EFcode
        #winsound.Beep(freq[EFcode[midPtr-ctr]], 200) if EFcode[midPtr-ctr] != '#' else EFcode
        note = 'sounds\\' + freq[EFcode[midPtr+ctr]] + '.wav'
        winsound.PlaySound(note, winsound.SND_FILENAME)
        note = 'sounds\\' + freq[EFcode[midPtr-ctr]] + '.wav'
        winsound.PlaySound(note, winsound.SND_FILENAME)        
        ctr += 1

def main():
    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        play(f.read())
        f.close()
    else:
        print("Please provide the path to the .ef file")

if __name__ == '__main__': main()
