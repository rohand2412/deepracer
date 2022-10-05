import time
import sys

x = 0

while True:
    print("\x1b[1mdone {}\x1b[0m".format(x))
    sys.stdout.flush()
    time.sleep(1)
    x += 1