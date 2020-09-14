# Author : Hosna Qasmei
# Created: 09/05/2020
# Description: Top 10 String manipulation algorithms with data integrity checks and logs

				
# class algorithms():


# 	def _init_(self, , ):
# 		self.

## String Manipulation

# Reverse an integer
# Prints the integer with resersed digits *** Note: Can be either a positive or negative number
# Also have data check on weither it is an int or any other data type. Will gracefully fail.
def reverse_integer(inputVal):
	try:
		string = str(inputVal)
		if string[0] == '-':
			return int('-'+string[:0:-1])
		else:
			return int(string[::-1])
	except ValueError:
		return -1 
	
	

# Average Words Length
def avg_words_len(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words),2)
		

# # Adding strings
# def (num1,num2):
#     eval(num1) + eval(num2)
#     return str(eval(num1) + eval(num2))

# # First unique character
# def solution(s):
#     frequency = {}
#     for i in s:
#         if i not in frequency:
#             frequency[i] = 1
#         else:
#             frequency[i] +=1
#     for i in range(len(s)):
#         if frequency[s[i]] == 1:
#             return i
#     return -1

# # Valid Palindrome
# def solution(s):
#     for i in range(len(s)):
#         t = s[:i] + s[i+1:]
#         if t == t[::-1]: return True

#     return s == s[::-1]

# ## Array
# # Monotonic Array
# def solution(nums): 
#     return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or 
#             all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))) 


# #  Move Zeroes
# def solution(nums):
#     for i in nums:
#         if 0 in nums:
#             nums.remove(0)
#             nums.append(0)
#     return nums


# # Fill in the Blanks
# def solution(array):
#     valid = 0            
#     res = []                 
#     for i in nums: 
#         if i is not None:    
#             res.append(i)
#             valid = i
#         else:
#             res.append(valid)
#     return res


# # Matched & Mismatched Words
# def solution(sentence1, sentence2):
#     set1 = set(sentence1.split())
#     set2 = set(sentence2.split())
    
#     return sorted(list(set1^set2)), sorted(list(set1&set2))


# # Prime Number Array
# def solution(n):
#     prime_nums = []
#     for num in range(n):
#         if num > 1: # all prime numbers are greater than 1
#             for i in range(2, num):
#                 if (num % i) == 0: # if the modulus == 0 is means that the number can be divided by a number preceding it
#                     break
#             else:
#                 prime_nums.append(num)
#     return prime_nums

