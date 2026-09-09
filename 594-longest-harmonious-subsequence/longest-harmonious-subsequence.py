class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        max_length = 0
        
        # Check each unique number
        for num in freq:
            # This line must be indented exactly 8 spaces
            if num + 1 in freq:
                max_length = max(max_length, freq[num] + freq[num + 1])
                
        return max_length