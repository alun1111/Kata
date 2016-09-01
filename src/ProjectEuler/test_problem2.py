from unittest import TestCase

from src.ProjectEuler.Problem2 import Problem2


class TestProblem2(TestCase):
    def test_Solve(self):
        p = Problem2()

        self.assertEquals(p.Solve(30), 10)

    def test_Final_Solve(self):
        p = Problem2()

        self.assertEquals(p.Solve(4000000), 4613732)
