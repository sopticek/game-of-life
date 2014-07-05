#!/usr/bin/env python
# vim:fileencoding=utf8
#
# Author:   Daniela Ďuričeková, daniela.duricekova@gmail.com
# Date:     2014-07-05
#

"""Tests for the lattice module."""

import unittest

from life.lattice import Lattice


class LatticeTests(unittest.TestCase):
    def test_create_lattice_with_size_and_get_size(self):
        lattice = Lattice(4)
        self.assertEqual(lattice.size, 4)

    def test_size_cannot_be_changed_after_creation(self):
        lattice = Lattice(4)
        with self.assertRaises(AttributeError):
            lattice.size = 5
