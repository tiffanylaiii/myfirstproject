"""
File: BeeperRowAdv.py
Name:
------------------------------
This program makes Karel fill up
Street 1 with some beepers already
existed
(This should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will fill the first Street in any world
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    """
    行走過程中，判斷路上是否已有beeper。
    若沒有，則放置一個beeper；若有，則移動至下一個位置
    """
    if not on_beeper():
        put_beeper()
    """
    解決差一錯誤，於終點時再判斷一次是否需要放置beeper
    """


if __name__ == '__main__':
    execute_karel_task(main)
