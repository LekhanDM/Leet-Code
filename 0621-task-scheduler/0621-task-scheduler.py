class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task,0)+1
        max_freq = max(freq.values())

        count = list(freq.values()).count(max_freq)

        return max(len(tasks),(max_freq-1)*(n+1)+count)