class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums_len = len(nums)
        for x in range(nums_len + 1):
            # Count how many numbers are greater than or equal to x
            cnt = sum(1 for num in nums if num >= x)
            if cnt == x:
                return x
        return -1 