class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        tentimes = 10
        newNum = 0

        org = x

        while org != 0:
            numDigit = org%10
            newNum = newNum * 10 + numDigit
            org //= 10
        
        if newNum == x:
            return True
        else:
            return False