import time
import sys


def typewriter(string):

    for letter in string:  # letter by letter print for intro -
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
