class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: Count occurrences using a dictionary
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        # Step 2: Find numbers that appear exactly once
        result = []
        for num, cnt in count.items():
            if cnt == 1:
                result.append(num)
        
        return result