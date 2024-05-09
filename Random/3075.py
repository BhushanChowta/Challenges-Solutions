class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        total = 0
        for i in range(k):
            if happiness[i] - i > 0:
                total += happiness[i] - i
        return total
        