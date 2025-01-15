from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        
        # Calculate the total product and count zeroes
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                prod *= num
        
        prod_list = []
        
        for i in range(len(nums)):
            if zero_count > 1:
                # If there are more than one zero, all products will be zero
                prod_list.append(0)
            elif zero_count == 1:
                # If there's exactly one zero, only the position with the zero will have a non-zero product
                if nums[i] == 0:
                    prod_list.append(prod)
                else:
                    prod_list.append(0)
            else:
                # No zeroes in the array, use division
                prod_list.append(prod // nums[i])
        
        return prod_list
