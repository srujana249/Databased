import unittest
from getTotalNumberOfLipsticks import getTotalNumberOfLipsticks 


class TestingGetTotalNumberOfLipsticks(unittest.TestCase):

    def testingGetTotalNumberOfLipsticksCase1(self):
        for numberOfLipsticks,numberOfLeftoversNeeded, actualAnswer in [(5, 2, 9)]:
            self.assertEqual(getTotalNumberOfLipsticks (numberOfLipsticks,numberOfLeftoversNeeded), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase2(self):
        for numberOfLipsticks,numberOfLeftoversNeeded, actualAnswer in [(15, 5, 18)]:
            self.assertEqual(getTotalNumberOfLipsticks (numberOfLipsticks,numberOfLeftoversNeeded), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase3(self):
        for numberOfLipsticks,numberOfLeftoversNeeded, actualAnswer in [(2, 3, 2)]:
            self.assertEqual(getTotalNumberOfLipsticks (numberOfLipsticks,numberOfLeftoversNeeded), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase4(self):
        for numberOfLipsticks,numberOfLeftoversNeeded, actualAnswer in [(20, 5, 24)]:
            self.assertEqual(getTotalNumberOfLipsticks (numberOfLipsticks,numberOfLeftoversNeeded), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase5(self):
        for numberOfLipsticks,numberOfLeftoversNeeded, actualAnswer in [(13, 3, 19)]:
            self.assertEqual(getTotalNumberOfLipsticks (numberOfLipsticks,numberOfLeftoversNeeded), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase6(self):
        for numberOfLipsticks,numberOfLeftoversNeeded, actualAnswer in [(24, 6, 28)]:
            self.assertEqual(getTotalNumberOfLipsticks (numberOfLipsticks,numberOfLeftoversNeeded), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase7(self):
        for numberOfLipsticks,numberOfLeftoversNeeded, actualAnswer in [(10, 4, 13)]:
            self.assertEqual(getTotalNumberOfLipsticks (numberOfLipsticks,numberOfLeftoversNeeded), actualAnswer)

    def testingGetTotalNumberOfLipsticksCase8(self):
        for numberOfLipsticks,numberOfLeftoversNeeded, actualAnswer in [(50, 3, 74)]:
            self.assertEqual(getTotalNumberOfLipsticks (numberOfLipsticks,numberOfLeftoversNeeded), actualAnswer)


if __name__ == '__main__':
    unittest.main()
