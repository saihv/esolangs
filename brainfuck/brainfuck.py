import sys
import getch

class BF:
    values, loc, ptr = [0], 0, 0
    cmds = ['+', '-', '>', '<', '[', ']', '.', ',']
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

    def read(self):
        self.values[self.ptr] = ord(getch.getch())

    def write(self):
        sys.stdout.write(chr(self.values[self.ptr]))

    def opposite(self, cmd):
        if self.cmds.index(cmd) % 2 == 0:
            return self.cmds[self.cmds.index(cmd) + 1]
        else:
            return self.cmds[self.cmds.index(cmd) - 1]

    def process(self, code):
        code = self.minify(code)
        self.loopLoc = self.identifyLoops(code)
        while self.loc < len(code):
            cmd = code[self.loc]
            if cmd in instructions:
                instructions[cmd](self)
            self.loc += 1

    def minify(self, code):
        return list(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))

    def identifyLoops(self, code):
        sbList, loopLoc = [], {}
        for idx, cmd in enumerate(code):
            if cmd == '[': sbList.append(idx)
            if cmd == ']': start = sbList.pop();  loopLoc[start] = idx;  loopLoc[idx] = start
        return loopLoc

instructions = {
    '>': BF.increment,
    '<': BF.decrement,
    '+': BF.add,
    '-': BF.subtract,
    '[': BF.begin,
    ']': BF.end,
    ',': BF.read,
    '.': BF.write
}

def main():
    Brainfuck = BF()
    f = open('..\examples\example.bf', 'r')
    Brainfuck.process(f.read())
    f.close()

if __name__ == '__main__': main()