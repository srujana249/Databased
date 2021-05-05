# Databased
Take Home Assessment


How to run the Code:

Use the respective Test files for each of the problems. For example, for leastFactorial problem leastFactorialTest is the corresponding test file. Run the test file , in windows we run it using the following  command in the command prompt: python3 leastFactorialTest.py 
If all the testcases are passed in the testcase file OK is printed. In the similar way, we run the test files of other problems and check if it passes all the testcases.




Overview of the Solutions:

Problem 1: LeastFactorial : Created an array named factorial to store the factorial values 1!,2!,...5!, since 1<=n<=120 and k>=n. If the value of n is 1 returned 1. Iterated through the array to check for the value which is greater than n.

Problem 2: getTotalNumberOfLipsticks: Calculated the number of lipsticks which can be created from the leftovers and leftovers that are remaining after creating the lipsticks. Added the number of lipsticks sold to the result value and assigned the number of lipsticks created from leftovers to the numberOfLipsticks,since this is our new numberOfLipsticks that can be sold.  Used a while loop to iterate the above steps until the numberOfLipsticks is greater than zero. Returned the value of res variable in the end

Problem 2:getLastStudent: Calculated the chair number of the student who recieves the last treat by using number of treats and starting chair number. This value cannot be greater than the numberOfStudents. If this value is greater than numberofStudents ,I recalculated it by using lastStudent=lastStudent-(numberOfStudents*(lastStudent//numberOfStudents)) (dividin the obtained chair number by number os students and then multiplying it with numberOfStudents gives the correct value of lastStudent chair number within the correct). If the lastStudent is 0 I returned numberofStudents else returned lastStudent chair number.
