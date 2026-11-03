
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_reach = 0

        for i in range(len(nums)):

            # Cannot reach this position
            if i > max_reach:
                return False

            # Update maximum reachable index
            max_reach = max(max_reach, i + nums[i])

            # Last index is reachable
            if max_reach >= len(nums) - 1:
                return True

        return True
