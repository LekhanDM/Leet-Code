class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix * answer[i]
            prefix = nums[i] * prefix
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * suffix
            suffix = nums[i] * suffix
        return answer