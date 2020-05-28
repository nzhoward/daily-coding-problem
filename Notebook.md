### Backtracking DP

General template for solving backtrack/path/DP problems

Examples:
* https://leetcode.com/problems/subsets/
* https://leetcode.com/problems/subsets-ii/
* https://leetcode.com/problems/permutations/
* https://leetcode.com/problems/permutations-ii/
* https://leetcode.com/problems/combination-sum/
* https://leetcode.com/problems/combination-sum-ii/
* https://leetcode.com/problems/palindrome-partitioning/

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(path, start):
            ans.append(path)
            for i in range(start, len(nums)):
                backtrack(path + [nums[i]], i + 1)
        
        ans = []
        backtrack([], 0)
        
        return ans
```

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(path, start):
            ans.append(path)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                backtrack(path + [nums[i]], i + 1)
        
        ans = []
        nums.sort()
        backtrack([], 0)
        
        return ans
```

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path)
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                backtrack(path + [nums[i]])
        
        ans = []
        backtrack([])
        
        return ans
```

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path)
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                backtrack(path + [nums[i]])
                used[i] = False
        
        ans = []
        nums.sort()
        used = [False for _ in range(len(nums))]
        backtrack([])
        
        return ans
```


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
