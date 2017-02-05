import sys
import getch

class EF:
    values, loc, ptr = [0], 0, 0
    cmds = ['+','-','>','<','[',']','.',',']
    loopLoc = {}
    
    def increment(self):
      self.ptr += 1
      if self.ptr == len(self.values): self.values.append(0)

    def decrement(self):
      self.ptr = 0 if self.ptr <= 0 else self.ptr - 1

    def add(self):
      self.values[self.ptr] += 1 if self.values[self.ptr] < 255 else 0

    def subtract(self):
      self.values[self.ptr] -= 1 if self.values[self.ptr] > 0 else 255

    def begin(self):
       self.loc = self.loopLoc[self.loc] if self.values[self.ptr] == 0 else self.loc

    def end(self):
       self.loc = self.loopLoc[self.loc] if self.values[self.ptr] != 0 else self.loc

    def read(self): self.values[self.ptr] = ord(getch.getch())

    def write(self): sys.stdout.write(chr(self.values[self.ptr]))

    def opposite(self, cmd):
        if self.cmds.index(cmd)%2 == 0:
            return self.cmds[self.cmds.index(cmd)+1]
        else:
            return self.cmds[self.cmds.index(cmd)-1]
        
    def BFify(self, EFcode):
        midPtr = int(len(EFcode)/2)
        ctr = 1
        BFcode = []
        while ctr <= midPtr:
            BFcode.append(EFcode[midPtr+ctr]) if EFcode[midPtr+ctr] != '#' else EFcode
            BFcode.append(self.opposite(EFcode[midPtr-ctr])) if EFcode[midPtr-ctr] != '#' else EFcode
            ctr += 1
            
        return BFcode

    def process(self, code):
        code = self.BFify(self.minify(code))
        self.loopLoc = self.identifyLoops(code)

        midPtr = (len(code)+1)/2
        while self.loc < len(code):
            cmd = code[self.loc]
            if cmd in instructions:
                instructions[cmd](self)

            self.loc += 1

    def minify(self, code):
        return list(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-', '0', '#'], code))

    def identifyLoops(self, code):
        sbList, loopLoc = [], {}

        for idx, cmd in enumerate(code):
            if cmd == '[': sbList.append(idx)
            if cmd == ']': start = sbList.pop();  loopLoc[start] = idx;  loopLoc[idx] = start
        return loopLoc

instructions = {
        '>': EF.increment,
        '<': EF.decrement,
        '+': EF.add,
        '-': EF.subtract,
        '[': EF.begin,
        ']': EF.end,
        ',': EF.read,
        '.': EF.write
        }

def main():
    Eitherfuck = EF()
    f = open('..\examples\example.ef', 'r')
    Eitherfuck.process(f.read())
    f.close()

if __name__ == '__main__': main()