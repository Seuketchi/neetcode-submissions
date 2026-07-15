class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. create an empty dictionary
        count = {}
        
        # 2. count number frequency on that index (ex.: #1 which would be index 1 would add 1 if it appears)
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # 3. make a bucket which is basically a list of list for each number frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num,freq in count.items():
            buckets[freq].append(num)
        
        # 4. rank the number frequency
        result = []
        for freq in range(len(buckets) - 1, 0 , -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result