#!/usr/bin/env python
# vim:fileencoding=utf8
#
# Author:   Daniela Ďuričeková, daniela.duricekova@gmail.com
# Date:     2014-07-08
#

"""Tests for the game module."""

import unittest

from life.game import Game


class GameCreationTests(unittest.TestCase):
    def test_create_game_with_size(self):
        game = Game(3)
        self.assertEqual(game.size, 3)

    def test_size_cannot_be_modified_after_creation(self):
        game = Game(3)
        with self.assertRaises(AttributeError):
            game.size = 4

    def test_all_cells_are_dead_after_creation_with_size(self):
        game = Game(3)
        for x in range(game.size):
            for y in range(game.size):
                self.assertTrue(game.is_dead(x, y))

    def test_create_game_from_string(self):
        game = Game.from_string(
            "xx\n"
            "  \n"
        )
        self.assertTrue(game.is_live(0, 0))
        self.assertTrue(game.is_live(0, 1))
        self.assertTrue(game.is_dead(1, 0))
        self.assertTrue(game.is_dead(1, 1))
