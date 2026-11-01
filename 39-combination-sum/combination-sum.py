
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        path = []

        def backtrack(start, remaining):

            if remaining == 0:
                result.append(path.copy())
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                path.append(candidates[i])

                # Same index allows reuse of the number
                backtrack(i, remaining - candidates[i])

                path.pop()

        backtrack(0, target)

        return result
