class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod=1
        sum=0

        while n!=0:
            d=n%10
            prod=prod*d
            sum=sum+d
            n=n/10
        
        return prod-sum
        