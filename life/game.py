#!/usr/bin/env python
# vim:fileencoding=utf8
#
# Author:   Daniela Ďuričeková, daniela.duricekova@gmail.com
# Date:     2014-07-08
#

"""Representation of a lattice."""

from life.lattice import Lattice


class Game:
    def __init__(self, size):
        self._lattice = Lattice(size)

    @staticmethod
    def from_string(str, dead_symbol=' ', live_symbol='x'):
        lattice = Lattice.from_string(str, dead_symbol, live_symbol)
        game = Game(lattice.size)
        game._lattice = lattice
        return game

    @property
    def size(self):
        return self._lattice.size

    def is_dead(self, x, y):
        return self._lattice.is_dead(x, y)

    def is_live(self, x, y):
        return self._lattice.is_live(x, y)

    def make_step():
        pass
