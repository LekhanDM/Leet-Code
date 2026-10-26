class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numbers = set(nums)
        longest = 0
        for num in numbers:
            if num - 1 not in numbers:
                current = num
                count = 1
                while current + 1 in numbers:
                    current += 1
                    count += 1
                longest = max(longest, count)
        return longest