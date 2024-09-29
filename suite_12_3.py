import tests_12_2
import TestRunner
import unittest

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestRunner.TestRunner))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)


