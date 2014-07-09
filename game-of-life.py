#!/usr/bin/env python
# vim:fileencoding=utf8
#
# Author:   Daniela Ďuričeková, daniela.duricekova@gmail.com
# Date:     2014-07-09
#

"""Main script that loads and runs the game."""

import fileinput
import os
import time

from life.game import Game


def main():
    with fileinput.input() as f_input:
        game = Game.from_string("".join(f_input))

    while True:
        os.system('clear')
        print(game)
        time.sleep(0.1)
        game.make_step()

if __name__ == '__main__':
    main()
