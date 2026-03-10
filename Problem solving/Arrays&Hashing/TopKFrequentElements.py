nums = [1,2,2,3,3,3]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {key:nums.count(key) for key in nums}
        sorted_items_desc = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        result = [item[0] for item in sorted_items_desc[:k]]
        return result