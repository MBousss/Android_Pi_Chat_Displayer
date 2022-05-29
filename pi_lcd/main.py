#!/usr/bin/python

from DisplayManager import Display
import sys
import time
import re

display = Display()

while True:
    with open(sys.argv[1]) as f:
        for line in f:
            if re.search('[a-zA-Z]', line):
                print(line)
                display.show(line)
                time.sleep(1)
            else:
                time.sleep(1)