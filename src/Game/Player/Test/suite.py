import unittest

from Game.Player.Test.player_test import suite as player_suite

suites = [player_suite]
suite = unittest.TestSuite(suites)