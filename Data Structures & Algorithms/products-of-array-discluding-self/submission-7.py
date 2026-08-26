from copy import deepcopy

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        umbrella_prod = math.prod(nums)
        if umbrella_prod == 0:
            if nums.count(0) == 1:
                zero_index = nums.index(0)
                nums_without_zero = deepcopy(nums)
                nums_without_zero.pop(zero_index)
                print(nums_without_zero, zero_index)
                non_zero_prod = math.prod(nums_without_zero)
                
                return [umbrella_prod // x if x != 0 else non_zero_prod for x in nums]
            else:
                return [0] * len(nums)
        
        return [umbrella_prod // x for x in nums]