#!python

import sys

if len(sys.argv) > 1:
    param = sys.argv[1]
    print('1st argument found was: ' + param)
else:
    print('No arguments found')
    exit()

if len(sys.argv) > 2:
    param = sys.argv[2]
    print('2nd argument found was: ' + param)
else:
    print('No other arguments found')
    exit()

