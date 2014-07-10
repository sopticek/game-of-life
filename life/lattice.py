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
        # Do not require the presence of trailing spaces as dead symbols.
        if dead_symbol == ' ':
            str_lattice = Lattice._add_missing_dead_cells(
                str_lattice, dead_symbol)
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

    def get_num_of_live_neighbours(self, x, y):
        self._validate_position(x, y)
        neighbours = [
            (x - 1, y - 1),
            (x - 1, y    ),
            (x - 1, y + 1),
            (x    , y - 1),
            (x    , y + 1),
            (x + 1, y - 1),
            (x + 1, y    ),
            (x + 1, y + 1)
        ]

        return len(list(filter(self._is_valid_neighbour_and_live,
            neighbours)))

    def _is_valid_neighbour_and_live(self, neighbour):
        return (self._is_valid_position(*neighbour) and
                self.is_live(*neighbour))

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
        if not self._is_valid_position(x, y):
            raise OutOfBoundsError(x, y)

    def _validate_size(self, size):
        if size <= 0:
            raise InvalidSizeError(size)

    def _is_valid_position(self, x, y):
        return (0 <= x < self.size) and (0 <= y < self.size)

    @staticmethod
    def _input_str_to_str_lattice(str):
        if str and str[-1] == '\n':
            str = str[:-1]
        rows = str.split('\n')
        return [list(row) for row in rows]

    @staticmethod
    def _add_missing_dead_cells(str_lattice, dead_symbol):
        max_cols = Lattice._get_max_cols_from_str_lattice(str_lattice)
        for row in str_lattice:
            num_of_missing_dead_cells = max_cols - len(row)
            row.extend(dead_symbol * num_of_missing_dead_cells)
        return str_lattice

    @staticmethod
    def _get_max_cols_from_str_lattice(str_lattice):
        return max(len(row) for row in str_lattice)

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
