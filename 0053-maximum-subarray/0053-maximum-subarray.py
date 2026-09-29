class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # kadane's algorithm
        current = nums[0]
        maximum = nums[0]
        for x in nums[1:]:
            current = max(x,current+x)
            maximum = max(maximum,current)
        return maximum