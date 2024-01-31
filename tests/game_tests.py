#!/usr/bin/env python
# vim:fileencoding=utf8
#
# Author:   Daniela Ďuričeková, daniela.duricekova@protonmail.com
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


class GameMakeStepTests(unittest.TestCase):
    def scenario_validate_make_step(self, original_game, expected_game):
        original_game.make_step()
        self.assertTrue(original_game == expected_game,
            "\noriginal_game:\n{}expected_game:\n{}".format(
            original_game, expected_game))

    def test_live_cell_with_no_live_neighbours_dies(self):
        game = Game.from_string(
            "   \n"
            " x \n"
            "   \n"
        )
        expected_game = Game.from_string(
            "   \n"
            "   \n"
            "   \n"
        )
        self.scenario_validate_make_step(game, expected_game)

    def test_live_cell_with_one_live_neighbour_dies(self):
        game = Game.from_string(
            "   \n"
            "xx \n"
            "   \n"
        )
        expected_game = Game.from_string(
            "   \n"
            "   \n"
            "   \n"
        )
        self.scenario_validate_make_step(game, expected_game)

    def test_live_cell_with_two_live_neighbours_lives(self):
        game = Game.from_string(
            "x  \n"
            " x \n"
            "  x\n"
        )
        expected_game = Game.from_string(
            "   \n"
            " x \n"
            "   \n"
        )
        self.scenario_validate_make_step(game, expected_game)

    def test_live_cell_with_three_live_neighbours_lives(self):
        game = Game.from_string(
            "x x\n"
            " x \n"
            "  x\n"
        )
        expected_game = Game.from_string(
            " x \n"
            " xx\n"
            "   \n"
        )
        self.scenario_validate_make_step(game, expected_game)

    def test_live_cell_with_four_live_neighbours_dies(self):
        game = Game.from_string(
            "x x\n"
            " x \n"
            "x x\n"
        )
        expected_game = Game.from_string(
            " x \n"
            "x x\n"
            " x \n"
        )
        self.scenario_validate_make_step(game, expected_game)

    def test_live_cell_with_five_live_neighbours_dies(self):
        game = Game.from_string(
            "xxx\n"
            " x \n"
            "x x\n"
        )
        expected_game = Game.from_string(
            "xxx\n"
            "   \n"
            " x \n"
        )
        self.scenario_validate_make_step(game, expected_game)

    def test_live_cell_with_six_live_neighbours_dies(self):
        game = Game.from_string(
            "xxx\n"
            " x \n"
            "xxx\n"
        )
        expected_game = Game.from_string(
            "xxx\n"
            "   \n"
            "xxx\n"
        )
        self.scenario_validate_make_step(game, expected_game)

    def test_dead_cell_with_three_live_neighbours_lives(self):
        game = Game.from_string(
            " x \n"
            "   \n"
            "xx \n"
        )
        expected_game = Game.from_string(
            "   \n"
            "xx \n"
            "   \n"
        )
        self.scenario_validate_make_step(game, expected_game)

class GameDelegationTests(unittest.TestCase):
    def setUp(self):
        self.game = Game.from_string(
            " x \n"
            "   \n"
            "xx \n"
        )

    def test_size_is_delegated_to_lattice(self):
        self.assertEqual(self.game.size, 3)

    def test_is_dead_is_delegated_to_lattice(self):
        self.assertTrue(self.game.is_dead(0, 0))

    def test_is_live_is_delegated_to_lattice(self):
        self.assertTrue(self.game.is_live(0, 1))

    def test_make_dead_is_delegated_to_lattice(self):
        self.game.make_dead(0, 1)
        self.assertTrue(self.game.is_dead(0, 1))

    def test_make_live_is_delegated_to_lattice(self):
        self.game.make_live(0, 0)
        self.assertTrue(self.game.is_live(0, 0))

    def test_toggle_liveness_is_delegated_to_lattice(self):
        self.game.toggle_liveness(0, 0)
        self.assertTrue(self.game.is_live(0, 0))
        self.game.toggle_liveness(0, 0)
        self.assertTrue(self.game.is_dead(0, 0))

    def test_lattice_does_not_appear_in_attribute_error_messages(self):
        with self.assertRaises(AttributeError) as cm:
            self.game.nonexisting
        self.assertRegex(str(cm.exception), r"^.*Game.*$")


class GameComparisonTests(unittest.TestCase):
    def test_two_games_with_equal_lattices_are_equal(self):
        game1 = Game.from_string("x")
        game2 = Game.from_string("x")
        self.assertEqual(game1, game2)

    def test_two_games_with_different_lattices_are_not_equal(self):
        game1 = Game.from_string(" ")
        game2 = Game.from_string("x")
        self.assertNotEqual(game1, game2)
