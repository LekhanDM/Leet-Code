class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # a = {}
        # for i in range(len(nums)):
        #     a[nums[i]] = a.get(nums[i], 0) + 1
        # for x in a:
        #     if a[x] > len(nums)//2:
        #         return x
        # return -1

        candidate = 0
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
            if x == candidate:
                count += 1
            else:
                count -= 1
        return candidate