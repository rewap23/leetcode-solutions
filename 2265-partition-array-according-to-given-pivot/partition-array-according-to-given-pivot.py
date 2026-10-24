class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        #section the solution into less than pivot, pivot and greater than pivot

        output = [] * len(nums)
        begin = []
        middle = []
        end = []

        for num in nums:
            if num < pivot:
                begin.append(num)
            elif num == pivot:
                middle.append(num)
            elif num > pivot:
                end.append(num)

        output = begin + middle + end

        return output

        

        
        