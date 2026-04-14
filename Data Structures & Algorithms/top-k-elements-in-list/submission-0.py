class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # index represents the frequency

        #frequency map
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)


        #building buckets (index = frequency)
        freq = []
        for i in range(len(nums)+1):
            freq.append([])
        
        for n , c in count.items():
            freq[c].append(n)
        
        # read from right, collect k elements
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        