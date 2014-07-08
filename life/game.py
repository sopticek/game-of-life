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

    def make_step(self):
        new_lattice = Lattice(self.size)
        for x in range(self.size):
            for y in range(self.size):
                if self._should_become_live(x, y):
                    new_lattice.make_live(x, y)
        self._lattice = new_lattice

    def _should_become_live(self, x, y):
        num_of_live_neighbours = self._lattice.get_num_of_live_neighbours(x, y)

        if self._lattice.is_live(x, y) and num_of_live_neighbours < 2:
            return False
        elif self._lattice.is_live(x, y) and 2 <= num_of_live_neighbours <= 3:
            return True
        elif self._lattice.is_live(x, y) and num_of_live_neighbours > 3:
            return False
        elif self._lattice.is_dead(x, y) and num_of_live_neighbours == 3:
            return True

        return False

    def __eq__(self, other):
        return self._lattice == other._lattice

    def __ne__(self, other):
        return self._lattice != other._lattice

    def __repr__(self):
       return repr(self._lattice)
