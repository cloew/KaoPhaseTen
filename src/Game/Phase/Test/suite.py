import unittest

from Game.Phase.Match.Test.suite import suite as match_suite

suites = [match_suite]
suite = unittest.TestSuite(suites)