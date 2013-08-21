import unittest

from Game.Player.Test.player_test import suite as player_suite
from Game.Player.Test.player_round_wrapper_test import suite as player_round_wrapper_suite

suites = [player_suite,
          player_round_wrapper_suite]
suite = unittest.TestSuite(suites)