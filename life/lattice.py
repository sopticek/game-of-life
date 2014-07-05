#!/usr/bin/env python
# vim:fileencoding=utf8
#
# Author:   Daniela Ďuričeková, daniela.duricekova@gmail.com
# Date:     2014-07-05
#

"""Representation of a lattice."""

class Lattice:
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size
