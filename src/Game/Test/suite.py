import unittest

from Game.Player.Test.suite import suite as player_suite
from Game.Phase.Test.suite import suite as phase_suite
from Game.Card.Test.suite import suite as card_suite
from Game.Test.round_test import suite as round_suite

suites = [round_suite,
          card_suite,
          phase_suite,
          player_suite]
suite = unittest.TestSuite(suites)