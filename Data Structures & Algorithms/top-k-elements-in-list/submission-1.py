class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        import heapq

        table = dict()
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1

        heap = []
        for key, value in table.items():
            ele = (value, key)
            if len(heap) < k:
                heapq.heappush(heap, ele)
            else:
                heapq.heappushpop(heap, ele)

        answer = []
        for keys, value in heap:
            answer.append(value)
            
        return answer


        