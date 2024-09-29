import unittest
import runner_and_tournament as rt


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
        """Если создать пустой словарь, как в условии задачи, то получается решить только 
        через tearDown, чтобы этот словарь возвращался после каждого забега, если создать список, 
        то можно перебрать циклом for и получить нужный вывод"""

    def setUp(self):
        self.r1 = rt.Runner('Усейн', 10)
        self.r2 = rt.Runner('Андрей', 9)
        self.r3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # print(cls.all_results)
        for i in cls.all_results:
            print(i)

    # def tearDown(self):
    #     print(self.all_results)  # так работает, если оставить cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        t1 = rt.Tournament(90, self.r1, self.r3)
        a = t1.start()
        self.all_results.append(a)
        self.assertIs(a.get((max(a.keys()))), 'Ник', 'Программа не работает')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        t2 = rt.Tournament(90, self.r2, self.r3)
        b = t2.start()
        self.all_results.append(b)
        self.assertIs(b.get((max(b.keys()))), 'Ник', 'Программа не работает')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        t3 = rt.Tournament(90, self.r1, self.r2, self.r3)
        c = t3.start()
        self.all_results.append(c)
        self.assertIs(c.get((max(c.keys()))), 'Ник', 'Программа не работает')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run4(self):
        t4 = rt.Tournament(0.00000000000000001, self.r1, self.r2, self.r3)
        d = t4.start()
        self.all_results.append(d)
        self.assertIs(d.get((max(d.keys()))), 'Ник', 'Программа не работает')


if __name__ == "__main__":
    unittest.main()
