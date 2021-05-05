import unittest
from getTotalNumberOfLipsticks import getTotalNumberOfLipsticks 


class TestingGetTotalNumberOfLipsticks(unittest.TestCase):

    def testingGetTotalNumberOfLipsticksCase1(self):
        for inputArgs,inputArgs1, actualAnswer in [(5, 2, 9)]:
            self.assertEqual(getTotalNumberOfLipsticks (inputArgs,inputArgs1), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase2(self):
        for inputArgs,inputArgs1, actualAnswer in [(15, 5, 18)]:
            self.assertEqual(getTotalNumberOfLipsticks (inputArgs,inputArgs1), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase3(self):
        for inputArgs,inputArgs1, actualAnswer in [(2, 3, 2)]:
            self.assertEqual(getTotalNumberOfLipsticks (inputArgs,inputArgs1), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase4(self):
        for inputArgs,inputArgs1, actualAnswer in [(20, 5, 24)]:
            self.assertEqual(getTotalNumberOfLipsticks (inputArgs,inputArgs1), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase5(self):
        for inputArgs,inputArgs1, actualAnswer in [(13, 3, 19)]:
            self.assertEqual(getTotalNumberOfLipsticks (inputArgs,inputArgs1), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase6(self):
        for inputArgs,inputArgs1, actualAnswer in [(24, 6, 28)]:
            self.assertEqual(getTotalNumberOfLipsticks (inputArgs,inputArgs1), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase7(self):
        for inputArgs,inputArgs1, actualAnswer in [(10, 4, 13)]:
            self.assertEqual(getTotalNumberOfLipsticks (inputArgs,inputArgs1), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase8(self):
        for inputArgs,inputArgs1, actualAnswer in [(50, 3, 74)]:
            self.assertEqual(getTotalNumberOfLipsticks (inputArgs,inputArgs1), actualAnswer)


if __name__ == '__main__':
    unittest.main()
