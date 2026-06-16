class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev_sum = 0
        for i in range(len(nums)):
            nums[i] = nums[i] + prev_sum
            prev_sum = nums[i]

        return nums 