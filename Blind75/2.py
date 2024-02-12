#20
class Solution:
    def isValid(self, s: str) -> bool:
       stack=[]
       dict={'(':')','{': '}','[': ']'}
       for i in range(len(s)):
        if s[i] in dict.keys():
            stack.append(s[i])
        elif s[i] in dict.values():
            if stack == [] or dict[stack.pop()]!=s[i]:
                return False
        else:
            return False

       return stack == []