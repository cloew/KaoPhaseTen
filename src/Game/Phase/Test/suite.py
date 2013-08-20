import unittest

from Game.Phase.Test.phase_list_test import suite as phase_list_suite
from Game.Phase.Test.phase_test import suite as phase_suite
from Game.Phase.Match.Test.suite import suite as match_suite

suites = [match_suite,
          phase_suite,
          phase_list_suite]
suite = unittest.TestSuite(suites)