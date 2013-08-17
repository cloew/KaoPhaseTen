import unittest

from Game.Test.round_test import suite as round_suite

suites = [round_suite]
suite = unittest.TestSuite(suites)