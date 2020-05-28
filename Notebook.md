### Backtracking DP

General template for solving backtrack/path/DP problems

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(path, remain, start):
            if remain < 0:
                return
            elif remain == 0:
                ans.append(path) # add current path to final answer/backtrack 
                return
            for i in range(start, len(candidates)):
                backtrack(path + [candidates[i]], remain - candidates[i], i) # add current candidate to current path
        
        #candidates.sort()
        ans = []
        backtrack([], target, 0)
        return ans
```
