class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count=(-1)
        #i=0
        for i in range(0,len(nums)):
        #while i<len(nums)+1:
            if count!=(-1):
                if nums[count]+nums[i]==target:
                    return count,i
            if (target-nums[i]) in nums[i+1:] and count<0:
                    count = i
            #i+=1
                
        return
