# 2384. Largest Palindromic Number
from collections import deque
class Solution:
    def largestPalindromic(self, num: str) -> str:

        digits_occurrences = {digit:0 for digit in num}

        for digit in num:
            digits_occurrences[digit] +=1
        
        if set([d for d in digits_occurrences.keys()]) == {'0'}:
            return "0"
        
        digits = sorted(list(digits_occurrences.keys()))

        palindrome_queue = deque()
        while len(digits) > 0:
            digit = digits.pop()
            if digits_occurrences[digit] > 1:
                if len(palindrome_queue) == 0 and digit == '0':
                    continue
                remainder = 0
                remainder = digits_occurrences[str(digit)] %2
                to_string =  digits_occurrences[str(digit)] - remainder #only take divisible by 2
                palindrome_queue.append((str(digit), to_string))
                digits_occurrences[str(digit)] = remainder # update
        
        #create palindrome string
        # initialize palindrome center with the highest number having occurrence 1
        occurences_1 = [k for k,v in digits_occurrences.items() if v ==1]
        if len(occurences_1)>0:
            string = sorted(occurences_1).pop()
        else:
            string = ''
            
        while len(palindrome_queue) > 0:
            digit, n = palindrome_queue.pop()
            digit_string = ''
            while n >0:
                digit_string += digit
                n -= 2
            string = digit_string + string + digit_string
        return string
