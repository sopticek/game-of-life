#!/usr/bin/env python
# vim:fileencoding=utf8
#
# Author:   Daniela Ďuričeková, daniela.duricekova@gmail.com
# Date:     2014-07-05
#

"""Representation of a lattice."""

class OutOfBoundsError(Exception):
    pass


class Lattice:
    def __init__(self, size):
        self._size = size
        self._lattice = [[False for _ in range(size)] for _ in range(size)]

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
