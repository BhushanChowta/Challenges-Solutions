#125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strg=''.join(filter(str.isalnum,s)).lower()
        rev_string=''.join(reversed(strg))

        return strg==rev_string