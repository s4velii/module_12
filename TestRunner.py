from main import Runner
import unittest


class TestRunner(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        boy = Runner('boy')
        for _ in range(1, 11):
            boy.walk()
        self.assertEqual(boy.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        men = Runner('men')
        for _ in range(1, 11):
            men.run()
        self.assertEqual(men.distance, 100)  # FAILED (failures=1) 101 != 100

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        child = Runner('child')
        runner = Runner('runner')
        for _ in range(1, 11):
            child.walk()
            runner.run()
        self.assertNotEqual(child.distance, runner.distance)
