## Graph/Tree

[Iterative BFS of Graph/Tree (queue)](#Iterative-BFS-of-Graph-queue)

[Iterative DFS of Graph/Tree (stack)](#Iterative-DFS-of-Graph-stack)

[DFS Matrix Traversal (recursive)](#DFS-Matrix-Traversal-recursive)

[DFS Matrix Traversal (iterative)](#DFS-Matrix-Traversal-iterative)

[Eliminating Leaves to Find Roots of MHTs](#Eliminating-Leaves-to-Find-Roots-of-MHTs)

## Lists/Pointers

[Sliding Window/Two Pointers](#Sliding-WindowTwo-Pointers)

[Merge Sort Singly Linked List](#Merge-Sort-Singly-Linked-List)

[Singly Linked List Reversal](#Singly-Linked-List-Reversal)

## Dynamic Programming

[Recursive DP (with memo)](#Recursive-DP-with-memo)

[Iterative DP](#Iterative-DP)

[Backtracking DP](#Backtracking-DP)

[Prefix/Range Sum](#PrefixRange-Sum)

[0-1 Knapsack](#0-1-Knapsack)

[Unbounded Knapsack](#Unbounded-Knapsack)

[Subsequence](#Subsequence)

[Paint Fence/House](#Paint-FenceHouse)

---

### Sliding Window/Two Pointers
* LC 76 - https://leetcode.com/problems/minimum-window-substring/
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        tdict = Counter(t)
        required = len(tdict)
        formed = 0
        wdict = Counter()
        ans = float('inf'), 0, 0
        
        for j in range(len(s)):
            # expand window to the right while conditions are not yet met
            wdict[s[j]] += 1
            if s[j] in tdict and wdict[s[j]] == tdict[s[j]]:
                formed += 1
            
            # condition is met
            while i <= j and formed == required:
                # contract window from the left up to the point conditions are no longer satisfied
                # update best result seen so far
                if j - i + 1 < ans[0]:
                    ans = j - i + 1, i, j
                wdict[s[i]] -= 1
                if s[i] in tdict and wdict[s[i]] < tdict[s[i]]:
                    formed -= 1
                i += 1
        
        return "" if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]
```

* LC 487 - https://leetcode.com/problems/max-consecutive-ones-ii/
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        zeros = 1
        ans = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeros -= 1
            while zeros < 0:
                if nums[i] == 0:
                    zeros += 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans
```

* LC 930 - https://leetcode.com/problems/binary-subarrays-with-sum/
```python
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        
        def atMost(S):
            if S < 0:
                return 0
            ans = 0
            i = 0
            for j in range(len(A)):
                if A[j] == 1:
                    S -= 1
                while S < 0:
                    if A[i] == 1:
                        S += 1
                    i += 1
                ans += j - i + 1
            return ans
        
        return atMost(S) - atMost(S - 1)
```

* LC 992 - https://leetcode.com/problems/subarrays-with-k-different-integers/
```python
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        def atMostK(K):
            count = Counter()
            ans = 0
            i = 0
            for j in range(len(A)):
                if count[A[j]] == 0:
                    K -= 1
                count[A[j]] += 1
                while K < 0:
                    count[A[i]] -= 1
                    if count[A[i]] == 0:
                        K += 1
                    i += 1
                ans += j - i + 1
            
            return ans
        
        return atMostK(K) - atMostK(K - 1)
```


* LC 1248 - https://leetcode.com/problems/count-number-of-nice-subarrays/
```python
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def atMostK(k):
            ans = 0
            i = 0
            for j in range(len(nums)):
                if nums[j] % 2 == 1:
                    k -= 1
                while k < 0:
                    if nums[i] % 2 == 1:
                        k += 1
                    i += 1
                ans += j - i + 1
            return ans
            
            
        return atMostK(k) - atMostK(k - 1)
```

### Eliminating Leaves to Find Roots of MHTs

![](https://assets.leetcode.com/static_assets/discuss/uploads/files/1469152741497-1463645059503_1214297289.jpg)
* LC 310 - https://leetcode.com/problems/minimum-height-trees/

```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        
        while n > 2:
            n -= len(leaves)
            newleaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newleaves.append(j)
            leaves = newleaves
        
        return leaves
```

### Iterative BFS of Graph (queue)
```python
def bfs(self, root):
    visited = set([root])
    queue = deque([(root, 0)])
    
    while queue:
        node, depth = queue.popleft()
        if node == target:
            return node
        for nei in neighbors(node):
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, depth + 1))
                
    return -1
```

* LC 429 - https://leetcode.com/problems/n-ary-tree-level-order-traversal/
```python
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        res = []
        
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                for nei in node.children:
                    queue.append(nei)
            res.append(tmp)
        
        return res
```

* LC 513 - https://leetcode.com/problems/find-bottom-left-tree-value/
```python
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque([root])
        res = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i == 0:
                    res = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res
```

* LC 515 - https://leetcode.com/problems/find-largest-value-in-each-tree-row/
```python
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            maxtmp = float('-inf')
            for i in range(len(queue)):
                node = queue.popleft()
                maxtmp = max(maxtmp, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(maxtmp)
    
        return ans
```

* LC 490 - https://leetcode.com/problems/the-maze/
```python
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([start])
        
        while queue:
            i, j = queue.popleft()
            
            if i == destination[0] and j == destination[1]:
                return True
            
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                while 0 <= x < m and 0 <= y < n and maze[x][y] != 1:
                    x += dx
                    y += dy
                x -= dx
                y -= dy
                if maze[x][y] == 0:
                    queue.append([x, y])
                    maze[x][y] = 2
        
        return False
```

### Iterative DFS of Graph (stack)
* LC 559 - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
```python
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        depth = 0
        while stack:
            root, curdepth = stack.pop()
            depth = max(depth, curdepth)
            for c in root.children:
                stack.append((c, curdepth + 1))
                    
        return depth
```

* LC 98 - https://leetcode.com/problems/validate-binary-search-tree/
```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            if node.val <= lower or node.val >= upper:
                return False
            stack.append((node.left, lower, node.val))
            stack.append((node.right, node.val, upper))
        
        return True
```

### DFS Matrix Traversal (recursive)
```python
def dfs(self, i, j, matrix, visited, m, n):
    if visited[i][j]:
        # return or return a value
    for d in self.directions:
        x, y = i + d[0], j + d[1]
        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
        # (or a condition you want to skip this round)
            continue
        # do something like
        visited[i][j] = True
        # explore the next level like
        self.dfs(x, y, matrix, visited, m, n)
```

### DFS Matrix Traversal (iterative)
* LC 200 - https://leetcode.com/problems/number-of-islands/
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        n = len(grid)
        m = len(grid[0])
        
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans += 1
                    queue = deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        if grid[x][y] == '1':
                            grid[x][y] = '0'
                            for dx, dy in directions:
                                tx = x + dx
                                ty = y + dy
                                if tx < 0 or tx >= n or ty < 0 or ty >= m or grid[tx][ty] == '0':
                                    continue
                                queue.append((tx, ty))
        
        return ans
```


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

### Recursive DP (with memo)

* LC 1155 - https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
```python
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        
        def dp(d, target):
            if d == 0:
                return 1 if target == 0 else 0
            if (d, target) in memo:
                return memo[(d, target)]
            res = 0
            for k in range(max(0, target - f), target):
                res += dp(d - 1, k)
            memo[(d, target)] = res
            return res
            
        return dp(d, target) % (10 ** 9 + 7)
```


### Iterative DP
https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.


### Backtracking DP

General template for solving backtrack/path/DP problems

Examples:
* LC 77 - https://leetcode.com/problems/combinations/
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(path, start):
            if len(path) == k:
                ans.append(path)
            for i in range(start, n + 1):
                backtrack(path + [i], i + 1)
        
        ans = []
        backtrack([], 1)
        
        return ans
```
* LC 78 - https://leetcode.com/problems/subsets/
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

* LC 90 - https://leetcode.com/problems/subsets-ii/
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

* LC 46 - https://leetcode.com/problems/permutations/
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

* LC 47 - https://leetcode.com/problems/permutations-ii/
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

* LC 39 - https://leetcode.com/problems/combination-sum/
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

* LC 40 - https://leetcode.com/problems/combination-sum-ii/
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

* LC 216 - https://leetcode.com/problems/combination-sum-iii/
```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(path, remain, start):
            if remain < 0:
                return
            elif len(path) == k and remain == 0:
                ans.append(path)
                return
            for i in range(start, len(candidates)):
                if used[i]:
                    continue
                used[i] = True
                backtrack(path + [candidates[i]], remain - candidates[i], i + 1)
                used[i] = False
        
        
        ans = []
        candidates = list(range(1, 10))
        used = [False for _ in range(len(candidates))]
        backtrack([], n, 0)
        
        return ans
```

* LC 131 - https://leetcode.com/problems/palindrome-partitioning/
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def backtrack(s, path):
            if not s:
                ans.append(path)
                return
            for i in range(1, len(s) + 1):
                if ispal(s[:i]):
                    backtrack(s[i:], path + [s[:i]])
        
        def ispal(s):
            return s == s[::-1]
        
        ans = []
        backtrack(s, [])
        
        return ans
```

* LC 784 - https://leetcode.com/problems/letter-case-permutation/
```python
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        def backtrack(path, i):
            if len(path) == len(S):
                ans.append(''.join(path))
                return
            if S[i].isnumeric():
                backtrack(path + [S[i]], i + 1)
            else:
                backtrack(path + [S[i].upper()], i + 1)
                backtrack(path + [S[i].lower()], i + 1)
        
        ans = []
        backtrack([], 0)
        
        return ans
```

* LC 1079 - https://leetcode.com/problems/letter-tile-possibilities/
```python
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def backtrack(count):
            res = 0
            for k in count:
                if count[k] == 0:
                    continue
                res += 1
                count[k] -= 1
                res += backtrack(count)
                count[k] += 1
            return res
        
        count = Counter(tiles)
        
        return backtrack(count)
```

* LC 310 - https://leetcode.com/problems/generalized-abbreviation/
```python
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        # i is current position
        # k is count of consecutive abbreviated characters
        def backtrack(path, i, k):
            if i == len(word):
                if k != 0:
                    ans.append(''.join(path + [str(k)]))
                else:
                    ans.append(''.join(path))
            else:
                backtrack(path, i + 1, k + 1)
                
                if k != 0:
                    backtrack(path + [str(k)] + [word[i]], i + 1, 0)
                else:
                    backtrack(path + [word[i]], i + 1, 0)
                
        ans = []
        backtrack([], 0, 0)
        return ans
```

### Prefix/Range Sum

```
+-----+-+------+      +-------+------+     +-----+--------+     +-----+--------+
|     | |      |      |       |      |     |     |        |     |     |        |
|     | |      |      |       |      |     |     |        |     |     |        |
+-----+-+      |      +-------+      |     |     |        |     +-----+        |
|     | |      |   =  |              |  +  |     |        |  -  |              | + mat[i][j]
+-----+-+      |      |              |     +-----+        |     |              |
|              |      |              |     |              |     |              |
|              |      |              |     |              |     |              |
+--------------+      +--------------+     +--------------+     +--------------+
rangeSum[i+1][j+1] =  rangeSum[i][j+1]  +  rangeSum[i+1][j]  -  rangeSum[i][j]   + mat[i][j]

+---------------+   +--------------+   +---------------+   +--------------+   +--------------+
|               |   |         |    |   |   |           |   |         |    |   |   |          |
|   (r1,c1)     |   |         |    |   |   |           |   |         |    |   |   |          |
|   +------+    |   |         |    |   |   |           |   +---------+    |   +---+          |
|   |      |    | = |         |    | - |   |           | - |      (r1,c2) | + |   (r1,c1)    |
|   |      |    |   |         |    |   |   |           |   |              |   |              |
|   +------+    |   +---------+    |   +---+           |   |              |   |              |
|        (r2,c2)|   |       (r2,c2)|   |   (r2,c1)     |   |              |   |              |
+---------------+   +--------------+   +---------------+   +--------------+   +--------------+
```

* LC 1314 - https://leetcode.com/problems/matrix-block-sum/
```python
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] - dp[i][j] + mat[i][j]
        
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = min(m, i + K + 1)
                c1 = min(n, j + K + 1)
                r2 = max(0, i - K)
                c2 = max(0, j - K)
                ans[i][j] = dp[r1][c1] + dp[r2][c2] - dp[r1][c2] - dp[r2][c1]
        
        return ans
```

* LC 304 - https://leetcode.com/problems/range-sum-query-2d-immutable
* LC 307 - https://leetcode.com/problems/range-sum-query-mutable
* LC 308 - https://leetcode.com/problems/range-sum-query-2d-mutable

### 0-1 Knapsack

Is it possible to sum up to a certain target using elements from a list? Each element can only be used once.

* LC 416 - https://leetcode.com/problems/partition-equal-subset-sum/
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2
        
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        
        for num in nums:
            for i in range(target, -1, -1):
                if num <= i:
                    dp[i] = dp[i] or dp[i - num]
        
        return dp[-1]
```

* LC 474 - https://leetcode.com/problems/ones-and-zeroes/
```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for st in strs:
            c = Counter(st)
            zeroes = c['0']
            ones = c['1']
            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(1 + dp[i - zeroes][j - ones], dp[i][j])
        
        return dp[-1][-1]
```

### Unbounded Knapsack

Is it possible to sum up to a certain target using elements from a list? Each element can be use unlimited number of times.

* LC 377 - https://leetcode.com/problems/combination-sum-iv
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
                
        
        return dp[-1]
```

### Subsequence
* LC 1027 - https://leetcode.com/problems/longest-arithmetic-sequence/
```python
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        
        # Iterate forward through every pair
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                # key = (idx of second in pair, diff between second and first)
                #    -> (idx of first in pair, diff between second and first) + 1
                # value = length of subsequence with this diff
                dp[(j, A[j] - A[i])] = dp.get((i, A[j] - A[i]), 1) + 1
        
        return max(dp.values())
```

### Paint Fence/House
* LC 276 - https://leetcode.com/problems/paint-fence/
```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k ** 2
        
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = k
        dp[2] = k ** 2
        
        for i in range(3, n + 1):
            # num_ways(i) = num_ways_diff(i) + num_ways_same(i)
            #             = num_ways(i-1) * (k-1) + num_ways_diff(i-1)
            #             = num_ways(i-1) * (k-1) + num_ways(i-2) * (k-1)
            #             = (num_ways(i-1) + num_ways(i-2)) * (k-1)
            dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)
        
        return dp[-1]
```
