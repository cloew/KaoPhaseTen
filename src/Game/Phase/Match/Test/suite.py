import unittest

from Game.Phase.Match.Test.number_set_test import suite as number_set_suite

suites = [number_set_suite]
suite = unittest.TestSuite(suites)