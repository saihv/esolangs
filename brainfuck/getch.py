'''
Code obtained from http://code.activestate.com/recipes/577977-get-single-keypress/
'''

import sys
try:
    import tty, termios
except ImportError:
    # Probably Windows.
    try:
        import msvcrt
    except ImportError:
        
        raise ImportError('getch not available')
    else:
        getch = msvcrt.getch
else:
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
