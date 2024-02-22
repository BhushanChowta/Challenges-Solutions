#383
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag={}

        for char in magazine:
            mag[char]=mag.get(char,0)+1

        for r in ransomNote:
            if r not in mag or mag[r] == 0 :
                return False
            
            mag[r]=mag[r]-1
            
        return True
