import unittest
from module_12_1_endurance_test import RunnerTest
from module_12_2_endurance_test_2 import TournamentTest

suite = unittest.TestSuite()
suite.addTests(unittest.makeSuite(RunnerTest))
suite.addTests(unittest.makeSuite(TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)