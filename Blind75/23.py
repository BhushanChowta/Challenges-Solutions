#217
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ns=set()
        for n in nums:
            if n in ns:
                return True
            ns.add(n)

        return False