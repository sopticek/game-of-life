#!/usr/bin/env python
# vim:fileencoding=utf8
#
# Author:   Daniela Ďuričeková, daniela.duricekova@gmail.com
# Date:     2014-07-05
#

"""Tests for the lattice module."""

import unittest

from life.lattice import OutOfBoundsError
from life.lattice import Lattice


class LatticeCreationTests(unittest.TestCase):
    def test_create_lattice_with_size_and_get_size(self):
        lattice = Lattice(4)
        self.assertEqual(lattice.size, 4)

    def test_size_cannot_be_changed_after_creation(self):
        lattice = Lattice(4)
        with self.assertRaises(AttributeError):
            lattice.size = 5

    def test_create_lattice_from_string(self):
        lattice = Lattice.from_string(
            "x x\n"
            " x \n"
            "x x\n"
        )
        self.assertEqual(lattice.size, 3)
        self.assertTrue(lattice.is_live(0, 0))
        self.assertTrue(lattice.is_dead(0, 1))
        self.assertTrue(lattice.is_live(0, 2))
        self.assertTrue(lattice.is_dead(1, 0))
        self.assertTrue(lattice.is_live(1, 1))
        self.assertTrue(lattice.is_dead(1, 2))
        self.assertTrue(lattice.is_live(2, 0))
        self.assertTrue(lattice.is_dead(2, 1))
        self.assertTrue(lattice.is_live(2, 2))


class LatticeLivenessTests(unittest.TestCase):
    def setUp(self):
        self.lattice = Lattice(4)

    def test_cells_are_dead_by_default(self):
        for x in range(self.lattice.size):
            for y in range(self.lattice.size):
                self.assertTrue(self.lattice.is_dead(x, y),
                    "x = {}, y = {}".format(x, y))

    def test_cell_is_live_after_make_live(self):
        self.lattice.make_live(2, 3)
        self.assertTrue(self.lattice.is_live(2, 3))

    def test_cell_is_dead_after_making_live_cell_dead(self):
        self.lattice.make_live(2, 3)
        self.lattice.make_dead(2, 3)
        self.assertTrue(self.lattice.is_dead(2, 3))

    def test_dead_cell_becomes_live_after_toggle(self):
        self.lattice.make_dead(1, 2)
        self.lattice.toggle_liveness(1, 2)
        self.assertTrue(self.lattice.is_live(1, 2))

    def test_live_cell_becomes_dead_after_toggle(self):
        self.lattice.make_live(1, 2)
        self.lattice.toggle_liveness(1, 2)
        self.assertTrue(self.lattice.is_dead(1, 2))


class LatticeOutOfBoundsTests(unittest.TestCase):
    def setUp(self):
        self.lattice = Lattice(4)

    def scenario_error_is_raised(self, method, x, y):
        with self.assertRaises(OutOfBoundsError) as cm:
            method(x, y)
        self.assertRegex(str(cm.exception), r"^.*{}.*{}.*$".format(x, y))

    def scenario_errors_are_raised(self, method):
        self.scenario_error_is_raised(method, self.lattice.size, 0)
        self.scenario_error_is_raised(method, 0, self.lattice.size)
        self.scenario_error_is_raised(method, -1, 0)
        self.scenario_error_is_raised(method, 0, -1)

    def test_error_is_raised_is_live(self):
        self.scenario_errors_are_raised(self.lattice.is_live)

    def test_error_is_raised_is_dead(self):
        self.scenario_errors_are_raised(self.lattice.is_dead)

    def test_error_is_raised_make_live(self):
        self.scenario_errors_are_raised(self.lattice.make_live)

    def test_error_is_raised_make_dead(self):
        self.scenario_errors_are_raised(self.lattice.make_dead)

    def test_error_is_raised_toggle_liveness(self):
        self.scenario_errors_are_raised(self.lattice.toggle_liveness)
