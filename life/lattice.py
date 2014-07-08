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


class InvalidSizeError(LatticeError):
    pass


class Lattice:
    def __init__(self, size):
        self._validate_size(size)
        self._size = size
        self._lattice = [[False for _ in range(size)] for _ in range(size)]

    @staticmethod
    def from_string(str, dead_symbol=' ', live_symbol='x'):
        str_lattice = Lattice._input_str_to_str_lattice(str)
        Lattice._validate_str_lattice_sizes(str_lattice)
        return Lattice._create_lattice_from_str_lattice(
            str_lattice, dead_symbol, live_symbol)

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

    def __eq__(self, other):
        return self._lattice == other._lattice

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        result = ''
        for x in range(self.size):
            for y in range(self.size):
                result += self._get_cell_repr(x, y)
            result += '\n'
        return result

    def _get_cell_repr(self, x, y):
        return 'x' if self.is_live(x, y) else ' '

    def _get_cell(self, x, y):
        self._validate_position(x, y)
        return self._lattice[x][y]

    def _set_cell(self, x, y, live):
        self._validate_position(x, y)
        self._lattice[x][y] = live

    def _validate_position(self, x, y):
        if not (0 <= x < self.size) or not (0 <= y < self.size):
            raise OutOfBoundsError(x, y)

    def _validate_size(self, size):
        if size <= 0:
            raise InvalidSizeError(size)

    @staticmethod
    def _input_str_to_str_lattice(str):
        rows = str.rstrip('\n').split('\n')
        return [list(row) for row in rows]

    @staticmethod
    def _validate_str_lattice_sizes(str_lattice):
        expected_col_count = len(str_lattice)
        for row in str_lattice:
            if len(row) != expected_col_count:
                raise InvalidSizeError

    @staticmethod
    def _create_lattice_from_str_lattice(str_lattice, dead_symbol, live_symbol):
        lattice = Lattice(len(str_lattice))
        for x, row in enumerate(str_lattice):
            for y, symbol in enumerate(row):
                if symbol == live_symbol:
                    lattice.make_live(x, y)
                elif symbol == dead_symbol:
                    lattice.make_dead(x, y)
                else:
                    raise InvalidSymbolError(x, y, symbol)
        return lattice
