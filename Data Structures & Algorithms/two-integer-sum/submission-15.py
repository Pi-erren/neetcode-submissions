class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        d[nums[0]] = [0]
        for i in range(1, len(nums)):
            d.setdefault(nums[i], []).append(i)
            if not (d.get(target - nums[i]) is None) and not (d.get(target - nums[i])[0] == i):
                return [d.get(target - nums[i])[0], i]
