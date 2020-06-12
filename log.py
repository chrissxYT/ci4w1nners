#!/usr/bin/env python3

from datetime import datetime
from sys import argv, stdin, exit

while True:
    line = stdin.readline()
    if(len(line) == 0):
        exit(0)
    print('{} [{}] {}'.format(datetime.now(), argv[1], line.rstrip()))
