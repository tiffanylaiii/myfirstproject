"""
File: BeeperRow.py
Name:
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    """
    於最後再放置一個beeper，解決差一錯誤
    """


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
