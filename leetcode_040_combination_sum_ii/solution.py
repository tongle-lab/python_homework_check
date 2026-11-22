class Solution:
    def combinationSum2(self, candidates, target):
        def backtrack(start, current_sum, path):
            if current_sum == target:
                result.append(path[:])
                return

            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i], path)
                path.pop()

        candidates.sort()
        result = []
        backtrack(0, 0, [])
        return result
