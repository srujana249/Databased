import unittest
from leastFactorial import leastFactorial


class TestingLeastFactorial(unittest.TestCase):

    def testingLeastFactorialCase1(self):
        for inputArgs, actualAnswer in [(1, 1)]:
            self.assertEqual(leastFactorial(inputArgs), actualAnswer)

    def testingLeastFactorialCase2(self):
        for inputArgs, actualAnswer in [(2, 2)]:
            self.assertEqual(leastFactorial(inputArgs), actualAnswer)

    def testingLeastFactorialCase3(self):
        for inputArgs, actualAnswer in [(4, 6)]:
            self.assertEqual(leastFactorial(inputArgs), actualAnswer)

    def testingLeastFactorialCase4(self):
        for inputArgs, actualAnswer in [(6, 6)]:
            self.assertEqual(leastFactorial(inputArgs), actualAnswer)

    def testingLeastFactorialCase5(self):
        for inputArgs, actualAnswer in [(17, 24)]:
            self.assertEqual(leastFactorial(inputArgs), actualAnswer)

    def testingLeastFactorialCase6(self):
        for inputArgs, actualAnswer in [(24, 24)]:
            self.assertEqual(leastFactorial(inputArgs), actualAnswer)

    def testingLeastFactorialCase7(self):
        for inputArgs, actualAnswer in [(107, 120)]:
            self.assertEqual(leastFactorial(inputArgs), actualAnswer)

    def testingLeastFactorialCase8(self):
        for inputArgs, actualAnswer in [(120, 120)]:
            self.assertEqual(leastFactorial(inputArgs), actualAnswer)


if __name__ == '__main__':
    unittest.main()
