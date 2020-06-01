### Merge Sort Singly Linked List
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head
        end = None # the end of the first half
        while fast and fast.next:
            end = slow
            slow = slow.next
            fast = fast.next.next
        
        end.next = None
        
        left = self.sortList(head)
        right = self.sortList(slow)
        
        return self.merge(left, right)
    
    
    def merge(self, left, right):
        cur = ListNode()
        ans = cur

        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        if left:
            cur.next = left

        if right:
            cur.next = right

        return ans.next
```


### Singly Linked List Reversal
```python
cur = head
prev = None

while cur:
    third = cur.next
    cur.next = prev
    prev = cur
    cur = third
```


### Iterative DP
https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.


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

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(path, remain, start):
            if remain < 0:
                # invalid path: discard
                return
            elif remain == 0:
                # valid path: add current path to final answer/backtrack
                ans.append(path)
                return
            for i in range(start, len(candidates)):
                if used[i]:
                    continue
                if i > 0 and candidates[i] == candidates[i - 1] and not used[i - 1]:
                    continue
                # add next candidate to current path
                used[i] = True
                backtrack(path + [candidates[i]], remain - candidates[i], i + 1)
                used[i] = False
        
        ans = []
        candidates.sort()
        used = [False for _ in range(len(candidates))]
        backtrack([], target, 0)
        
        return ans
```
