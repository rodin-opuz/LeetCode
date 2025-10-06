class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i, nums in enumerate(nums):
            complement = target - nums
            if complement in checked:
                return [checked[complement], i]
            checked[nums] = i
        return []
