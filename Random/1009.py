class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_n = bin(n)[2:]  # Convert n to binary (removing '0b' prefix)
        complement = ''.join(['1' if bit == '0' else '0' for bit in binary_n])  # Create complement
        retaurn int(complement, 2)  # Convert complement back to integer
