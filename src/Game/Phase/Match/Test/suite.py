import unittest

from Game.Phase.Match.Test.colored_set_test import suite as colored_set_suite
from Game.Phase.Match.Test.run_test import suite as run_suite
from Game.Phase.Match.Test.number_set_test import suite as number_set_suite

suites = [number_set_suite,
          run_suite,
          colored_set_suite]
suite = unittest.TestSuite(suites)