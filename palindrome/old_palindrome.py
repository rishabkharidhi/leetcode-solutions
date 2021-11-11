class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        temp = x[::-1]
        
        if x == temp:
            return True
        else:
            return False
