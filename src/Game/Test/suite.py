import unittest

from src.Game.Card.Test.suite import suite as card_suite
from Game.Test.round_test import suite as round_suite

suites = [round_suite,
          card_suite]
suite = unittest.TestSuite(suites)