class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myset = set(nums)
        unique = defaultdict(int)
       
        # Initialization
        for element in myset:
            unique[element] = 0

        for element in nums:
            if element in unique.keys():
                unique[element] += 1

        frequency_map = unique.items()
        sorted_frequency_map = sorted(frequency_map, key=lambda tup: tup[1],reverse=True)

        return([num[0] for num in sorted_frequency_map[0:k]])
