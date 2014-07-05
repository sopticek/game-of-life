#!/usr/bin/env python
# vim:fileencoding=utf8
#
# Author:   Daniela Ďuričeková, daniela.duricekova@gmail.com
# Date:     2014-07-05
#

"""Representation of a lattice."""

class LatticeError(Exception):
    pass


class OutOfBoundsError(LatticeError):
    pass


class InvalidSymbolError(LatticeError):
    def __init__(self, x, y, symbol):
        msg = "Invalid symbol '{}' on position ({}, {}).".format(symbol, x, y)
        super().__init__(msg)


class Lattice:
    def __init__(self, size):
        self._size = size
        self._lattice = [[False for _ in range(size)] for _ in range(size)]

    @staticmethod
    def from_string(str, dead_symbol=' ', live_symbol='x'):
        rows = str.split('\n')
        size = len(rows[0])
        lattice = Lattice(size)
        for y, row in enumerate(rows):
            for x, symbol in enumerate(row):
                if symbol == live_symbol:
                    lattice.make_live(x, y)
                elif symbol == dead_symbol:
                    lattice.make_dead(x, y)
                else:
                    raise InvalidSymbolError(x, y, symbol)
        return lattice

    @property
    def size(self):
        return self._size

    def is_dead(self, x, y):
        return not self.is_live(x, y)

    def is_live(self, x, y):
        return self._get_cell(x, y) == True

    def make_live(self, x, y):
        self._set_cell(x, y, True)

    def make_dead(self, x, y):
        self._set_cell(x, y, False)

    def toggle_liveness(self, x, y):
        self._set_cell(x, y, not self._get_cell(x, y))

    def _get_cell(self, x, y):
        self._validate_position(x, y)
        return self._lattice[x][y]

    def _set_cell(self, x, y, live):
        self._validate_position(x, y)
        self._lattice[x][y] = live

    def _validate_position(self, x, y):
        if not (0 <= x < self.size) or not (0 <= y < self.size):
            raise OutOfBoundsError(x, y)
