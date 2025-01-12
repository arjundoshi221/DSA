class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        bool_check = False
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                bool_check = True
        
        return bool_check