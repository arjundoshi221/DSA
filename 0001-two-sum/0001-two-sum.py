class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        target_list = list()
        len_num = len(nums)

        for i in range(len_num):
            for j in range(i+1, len_num):
                temp_sum = nums[i] + nums[j]
                if temp_sum == target:
                    target_list.append(i)
                    target_list.append(j)
                    target_list.sort()

        return target_list


        