class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        
        for i in range(n):
            xor = 0
            for j in range(i, n):
                xor ^= arr[j]
                if xor == 0 and j > i:
                    count += j - i
        
        return count