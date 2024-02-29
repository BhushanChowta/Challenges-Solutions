#409
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={}
        for c in s:
            freq[c]=freq.get(c,0)+1
        
        len=0
        hasOddFreq=False
        for count in freq.values():
            if count % 2 == 0:
                len+=count
            else:
                if not hasOddFreq:
                    len+=count
                    hasOddFreq=True
                else:
                    len+=count-1
        return len
