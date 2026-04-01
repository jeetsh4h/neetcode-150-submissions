class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # range is slower than enumerate????
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target: 
                    return [i, j]

        # should never reach here because of the
        # constraints defined by the problem
        return [-1, -1]