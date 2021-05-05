import unittest
from getLastStudent import getLastStudent 


class TestingGetLastStudent (unittest.TestCase):

    def testingGetLastStudentCase1(self):
        for numberOfStudents,treats,startingChair, actualAnswer in [(5, 2, 1, 2)]:
            self.assertEqual(getLastStudent  (numberOfStudents,treats,startingChair), actualAnswer)

    def testingGetLastStudentCase2(self):
        for numberOfStudents,treats,startingChair, actualAnswer in [(5, 2, 2, 3)]:
            self.assertEqual(getLastStudent (numberOfStudents,treats,startingChair), actualAnswer)

    def testingGetLastStudentCase3(self):
        for numberOfStudents,treats,startingChair, actualAnswer in [(7, 19, 2, 6)]:
            self.assertEqual(getLastStudent (numberOfStudents,treats,startingChair), actualAnswer)

    def testingGetLastStudentCase4(self):
        for numberOfStudents,treats,startingChair, actualAnswer in [(10000,2000,7888,9887)]:
            self.assertEqual(getLastStudent (numberOfStudents,treats,startingChair), actualAnswer)

    def testingGetLastStudentCase5(self):
        for numberOfStudents,treats,startingChair, actualAnswer in [(20000,23,2600, 2622)]:
            self.assertEqual(getLastStudent(numberOfStudents,treats,startingChair), actualAnswer)

    def testingGetLastStudentCase6(self):
        for numberOfStudents,treats,startingChair, actualAnswer in [(10000000,25000,500000,524999)]:
            self.assertEqual(getLastStudent (numberOfStudents,treats,startingChair), actualAnswer)

    def testingGetLastStudentCase7(self):
        for numberOfStudents,treats,startingChair, actualAnswer in [(100, 10, 32, 41)]:
            self.assertEqual(getLastStudent (numberOfStudents,treats,startingChair), actualAnswer)

    def testingGetLastStudentCase8(self):
        for numberOfStudents,treats,startingChair, actualAnswer in [(20000000,23000,3600000,3622999)]:
            self.assertEqual(getLastStudent (numberOfStudents,treats,startingChair), actualAnswer)


if __name__ == '__main__':
    unittest.main()
