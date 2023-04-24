"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    precondition:karel is on the left, facing east
    post-condition:karel is at the upper left, facing north
    """
    up()
    cross()
    down()


def up():
    """
    precondition:karel is on the left, facing east
    post-condition:karel is at the upper left, facing north
    """
    turn_left()
    while not right_is_clear():
        move()


def cross():
    """
     precondition:karel is at the upper left, facing north
     post-condition:karel is at the upper right, facing south
    """
    turn_right()
    move()
    turn_right()


def down():
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
