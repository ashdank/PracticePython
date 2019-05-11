#Determine whether an integer is a palindrome.
#An integer is a palindrome when it reads the same backward as forward
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        number = str(x)
        #print number
        pal = number [::-1]
        #print pal

        if number == pal:
            return True
        else:
            return False
