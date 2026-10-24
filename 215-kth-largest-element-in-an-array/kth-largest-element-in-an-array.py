class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = [] # length of elements in queue (how many there are)
        for num in nums:
            heapq.heappush(h, num)
            if len(h) > k: 
                heapq.heappop(h) # dropping the smallest element
        return h[0]