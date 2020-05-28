### Backtracking DP

General template for solving backtrack/path/DP problems

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(path, remain, start):
            if remain < 0:
                # invalid path: discard
                return
            elif remain == 0:
                # valid path: add current path to final answer/backtrack
                ans.append(path)
                return
            for i in range(start, len(candidates)):
                # add next candidate to current path
                backtrack(path + [candidates[i]], remain - candidates[i], i)
        
        #candidates.sort()
        ans = []
        backtrack([], target, 0)
        return ans
```
