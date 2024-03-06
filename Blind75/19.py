#67
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res=""
        carry=0

        maxLen=max(len(a),len(b))
        a=a.zfill(maxLen)
        b=b.zfill(maxLen)

        for i in range(maxLen-1,-1,-1):
            bit_sum=int(a[i])+int(b[i])+carry
            res=str(bit_sum % 2)+res
            carry=bit_sum//2

        if carry:
            res="1"+res

        return res