# Always ask the breaking conditions.
class Solution(object):
    def isPalindrome(self, x):
        # If negative number not a palindrom
        if x < 0:
            return False
	# if a single digit number is a palindrome
        if(x < 10 ):
            return True
	# By rule any number ending in 0 cannot be a palindrome.
        if (x%10 == 0):
            return False
        second_half = 0
        while(second_half < x):
            second_half = second_half * 10 + x%10
            x = x/10
        print (x , second_half)
        if((x == second_half) or (second_half/10 == x)):
            return True
        else:
            return False
