class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        # Keep dividing n by 2 until it becomes odd
        while n % 2 == 0:
            n //= 2
        
        # After division, if n becomes 1, it's a power of two
        return n == 1

