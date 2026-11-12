class Solution:
    import heapq
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            distance = -(x*x + y*y)
            heapq.heappush(heap, (distance, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for distance, point in heap]