def leastFactorial(n):
    #factorials array is used to store the values of 1!,2!,3!,4!,5!, since 1<=n<=120 and k>=n we do not store 6! value in array
    factorials = [1, 2, 6, 24, 120]
    if n == 1: return 1
    for idx in range(1, 5):
	#checking for value k in array which is greater than or equal to n
        if factorials[idx - 1] <= n <= factorials[idx]:
            return factorials[idx]
    return 120
	