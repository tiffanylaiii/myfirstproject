"""
File: PotholeFilling.py
Name: Tiffany Lai
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()
    """
    decomposition the method
    """


def turn_right():
    for i in range(3):
        turn_left()
# define turn right


def turn_around():
    turn_left()
    turn_left()
# define turn around


def go_in():
    move()
    turn_right()
    move()
    """
    precondition:Karel is at the upper left of the pothole, facing east.
    post-condition: Karel is in the pothole, facing south.
    """


def put_99_beepers():
    for i in range(99):
        put_beeper()


def go_out():
    turn_around()
    move()
    turn_right()
    move()
    """
    precondition:Karel is in the pothole, facing south.
    post-condition: Karel is at the upper left of the pothole, facing east.
    """


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
