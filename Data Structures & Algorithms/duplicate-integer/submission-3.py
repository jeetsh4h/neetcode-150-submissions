class Solution:
    # easiest way to do this would be
    # `return len(nums) != len(set(nums))`
    def hasDuplicate(self, nums: List[int]) -> bool:
        # this is essentially building the set(nums)
        count: dict[int, int] = {}
        for n in nums:
            if count.get(n) == None:
                count[n] = 1
            else:
                return True
        
        return False
