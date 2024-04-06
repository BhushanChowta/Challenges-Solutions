class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        
        # Handle negative numbers
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        ans = 0
        
        while x != 0:
            dig = x % 10
            if ans < INT_MIN / 10 or ans > INT_MAX / 10:
                return 0
            ans = ans * 10 + dig
            x = x // 10
        
        return sign * ans
