class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i = j = 0                         
        while i < len(s) and j < len(t):     # find characters from 't' in 's':
            j += s[i] == t[j]                # - characters in 't' can't be skipped
            i += 1                           # - characters in 's' can be skipped

        return len(t) - j                    # return missing characters