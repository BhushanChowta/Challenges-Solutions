class Solution:
    def getSmallestString(self, s: str) -> str:
        strArr=[i for i in s]
        for i in range(1,len(s)):
            a,b = int(strArr[i]), int(strArr[i-1])
            if a < b and a % 2 == b % 2:
                strArr[i], strArr[i-1] = strArr[i-1], strArr[i]
                break
        return "".join(strArr)