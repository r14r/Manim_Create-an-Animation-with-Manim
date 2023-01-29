#!/usr/bin/env python3

import sys
import os
import re

"""
"""

DEBUG = False


def Debug(line):
    if DEBUG:
        print(f"DEBUG: {line}")

def Log(line):
    print(f"LOG: {line}")


def parse(filename):
    STATE_PARSER_START = "-"
    STATE_EXAMPLE_START = "S"
    STATE_EXAMPLE_END = "E"
    STATE_EXAMPLE_COLLECT = "C"
    STATE_COMMENT = "#"

    WRITING = False

    OUTPUT = "NONE"
    HEADER = f"""
from manim import *

"""

    state = STATE_PARSER_START
    indent1 = 0

    Debug(f"Open file {filename}")

    with open(filename, 'r') as inp:
        for line in inp:
            line = line.rstrip('\n')

            Debug(f"# {state}: {line}")

            if (re.match(r'^\s+:media:', line)):
                Debug(f"Ignore :media: {line}")
                continue

            if (re.match(r'^\s*\.\.\s*manim\s*::.*', line)) or (re.match(r'^\s*\.\.\s*manim-example\s*::.*', line)):
                Debug(f"Found .. manim: {line}")

                indent1 = line.index("..")

                if state == STATE_EXAMPLE_COLLECT:
                    out.close()
                    WRITING = False

                state = STATE_EXAMPLE_START

            # Comment ends an example
            if (re.match(r'^[\s]*\"\"\"$', line)) and state == STATE_EXAMPLE_COLLECT:
                state = STATE_EXAMPLE_END
                Debug(f"Found Comment: set state to {state}")

            # Comment ends an example
            if (re.match(r'^[\s]*:\w+:', line)):
                state = STATE_EXAMPLE_END

            # .. directive ends an example (..warning, ..note)
            if (re.match(r'^\s*\.\.\s*\w+', line)) and state == STATE_EXAMPLE_COLLECT:
                state = STATE_EXAMPLE_END
                Debug(f"Found other manim command: set state to {state}")

            # Normal Text at start of line ends an example
            if STATE_EXAMPLE_COLLECT:
                if (re.match(r'^\w+', line)) or (re.match(r'^\w+', line[indent1:])):
                    state = STATE_EXAMPLE_END
                    Debug(f"Found normal text: set state to {state}")

            # End of Example, save current file
            if state == STATE_EXAMPLE_END:
                indent1 = 0

                if WRITING:
                    Debug(f"Close previous file")
                    out.close()
                    WRITING = False

            if state == STATE_EXAMPLE_START and (re.match(r'^\s*class\s+', line)):
                state = STATE_EXAMPLE_COLLECT
                OUTPUT = re.sub(r'^\s*class\s+([^(]+).*', r'\1', line)
                SKIPCHARS = line.index("class")

                WRITING = True

                if os.path.exists(f"{OUTPUT}.py"):
                    postfix = 0
                    while os.path.exists(f"{OUTPUT}_{postfix:02}.py"):
                        postfix += 1

                    OUTPUT = f"{OUTPUT}_{postfix:02}.py"
                else:
                    OUTPUT = f"{OUTPUT}.py"

                out = open(OUTPUT, 'w')
                out.write(HEADER)

                print(f"- {OUTPUT}")
                print("", end="")

            if WRITING:
                out.write(line[SKIPCHARS:] + '\n')
                pass

            if state == STATE_EXAMPLE_COLLECT:
                pass

            Debug(f"  {state}: {line}")

    if WRITING:
        out.close()
        # print("#")


"""
"""


def walk(rootdir='.', pattern='*'):
    for root, dirs, files in os.walk(rootdir):
        for folder in dirs:
            if folder in ["changelog", "_templates", "i18n", "LC_MESSAGES"]:
                continue

            d_name = root + "/" + folder

            walk(d_name, pattern)

        for file in files:
            f_name = root + '/' + file

            if re.match(pattern, file):
                parse(f_name)


"""
"""


def main(rootdir, pattern):
    print(f"Main: looking for '{pattern}' in {rootdir}")

    if pattern == '*':
        walk(rootdir, r'.*')
    else:
        walk(rootdir, r'.*' + pattern + '$')


if __name__ == "__main__":
    rootdir = '.+'
    pattern = '*'

    if len(sys.argv) > 1:
        rootdir = sys.argv[1]

    if len(sys.argv) > 2:
        pattern = sys.argv[2]

    main(rootdir, pattern)
    print("")
