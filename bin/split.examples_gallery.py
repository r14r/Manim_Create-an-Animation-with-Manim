#!/usr/bin/env python3

import re

STATE_COLLECTING_HEADER = 1
STATE_END_OF_CLASS = 2
STATE_START_OF_CLASS = 3
STATE_COLLECTING_CLASS = 4

HEADER = ""
WRITING = False

state=""
with open('split.input', 'r') as inp:
    for line in inp:
        line = line.rstrip('\n')

        if (line.startswith("from")):
            state = STATE_COLLECTING_HEADER

            HEADER = ""

        if (line.startswith("References")) or (line.startswith("Example")):
            state = STATE_END_OF_CLASS

            if WRITING:
                out.close()
                WRITING=False

        if (line.startswith("class")):
            state = STATE_START_OF_CLASS

        if state == STATE_COLLECTING_HEADER:
            HEADER = HEADER + '\n' + line

        if state == STATE_START_OF_CLASS:
            state = STATE_COLLECTING_CLASS
            OUTPUT = re.sub(r'^class ([^()]*).*', r'\1', line) + '.py'

            WRITING = True

            out = open(OUTPUT, 'w')
            out.write(HEADER)

        if WRITING:
            out.write(line + '\n')

out.close()
