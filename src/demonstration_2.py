"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
from  typing import List

def plus_one(digits: List[int]) -> List[int]:
    # Your code here
    #given a list of single-digit numbers that together represent a single number
    #increment the number by 1
    #case 1: the right-most digit is not 9
    #just increment the right-most digit by 1
    #case 2: right-most digit is 9
    #change the 9 to 0, then we need to add one to the digit to the left
    #note that change might cascade if we have more than one 9 to the left
    #if all digits are 9, then we need to add an additional digit to the list

    for i in range(len(digits) - 1, -1, -1):
      #start at end, up to -1 index(lands on index 0), decrement by 1
    	if digits[i] == 9:
        	digits[i] = 0
      else:
        digits[i] += 1
        return digits
      
      #if we reach here, we had the situation where every digit was a 9
      #we need to 1 to the front of the `digits` list
    return [1] + digits
    # digits.insert(0, 1)
    # return digits


print(plus_one([9,9,9]))
print(plus_one([3,2,1,9]))