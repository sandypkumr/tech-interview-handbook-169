from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, current, res):
        if not nums:
            res.append(current)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], current + [nums[i]], res)
