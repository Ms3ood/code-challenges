#Code Challenge 1: REVERSE STRING
def reverseString(s):
    s = str(s)
    result = s[::-1]
    return result
        
#Code Challenge 2: TWO SUM
def twoSum(num, target):
    length = len(num)
    for i in range(len(num)):
            if num[i] + num[i+1] == target:
                return [i, i+1]
            
        
#Code Challenge 3: Sum of integers from 1 to an number
def sumOfInts(num):
    total = 0
    for i in range(1,num+1):
      total+=i
    print("The total is: ", total)
      