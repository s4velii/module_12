from main import Runner
import unittest


class TestRunner(unittest.TestCase):
    def test_walk(self):
        boy = Runner('boy')
        for _ in range(1, 11):
            boy.walk()
        self.assertEqual(boy.distance, 50)

    def test_run(self):
        men = Runner('men')
        for _ in range(1, 11):
            men.run()
        self.assertEqual(men.distance, 101)  # FAILED (failures=1) 101 != 100

    def test_challenge(self):
        child = Runner('child')
        runner = Runner('runner')
        for _ in range(1, 11):
            child.walk()
            runner.run()
        self.assertNotEqual(child.distance, runner.distance)
