from unittest import TestCase

from src.ProjectEuler.Problem1 import Problem1


class TestProblem1(TestCase):
    def test_Example_Solve(self):
        p = Problem1()
        self.assertEquals(p.Solve(10), 23)

    def test_Final_Solve(self):
        p = Problem1()
        self.assertEquals(p.Solve(1000), 233168)

