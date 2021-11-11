class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if '-' in str(x):
            return False
        z=0
        temp=x
        while x!=0:
            y=x%10
            x=x//10
            z=(z*10)+y
            
        if z==temp:
            return True
        
        return False
            
