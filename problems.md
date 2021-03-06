# daily-coding-problem

### Checklist 

✅ = Done

⬜️ = Todo

❎ = Duplicate

|||||||
|---|---|---|---|---|---|
|✅day1|✅day2|✅day3|✅day4|✅day5|⬜️day6|
|✅day7|✅day8|✅day9|✅day10|⬜️day11|✅day12|
|✅day13|✅day14|✅day15|✅day16|✅day17|✅day18|
|✅day19|✅day20|❎day21|✅day22|✅day23|✅day24|
|⬜️day25|✅day26|✅day27|✅day28|✅day29|✅day30|
|✅day31|⬜️day32|✅day33|⬜️day34|✅day35|✅day36|
|✅day37|⬜️day38|⬜️day39|⬜️day40|⬜️day41|⬜️day42|
|✅day43|⬜️day44|✅day45|✅day46|✅day47|✅day48|
|✅day49|✅day50|⬜️day51|✅day52|✅day53|⬜️day54|
|✅day55|⬜️day56|✅day57|✅day58|⬜️day59|✅day60|
|✅day61|✅day62|✅day63|⬜️day64|✅day65|✅day66|
|✅day67|✅day68|✅day69|⬜️day70|❎day71|⬜️day72|
|✅day73|✅day74|⬜️day75|⬜️day76|⬜️day77|✅day78|
|⬜️day79|⬜️day80|


---

### Day 1 [Easy]

This problem was recently asked by Google.

Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.

For example, given `[10, 15, 3, 7]` and `k` of `17`, return true since `10 + 7` is `17`.

Bonus: Can you do this in one pass?

[Solution (naive + one pass)](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day1.py)

---
### Day 2 [Hard]

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index `i` of the new array is the product of all the numbers in the original array except the one at `i`.

For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be `[120, 60, 40, 30, 24]`. If our input was `[3, 2, 1]`, the expected output would be `[2, 3, 6]`.

Follow-up: what if you can't use division?

[Solution (naive + no division)](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day2.py)

---
### Day 3 [Medium]

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:
```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```
[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day3.py)

---
### Day 4 [Hard]
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give `3`.

You can modify the input array in-place.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day4.py)

[Solution (bucket sort)](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day4-bucket.py)

---
### Day 5 [Medium]
This problem was asked by Jane Street.

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair. For example, `car(cons(3, 4))` returns `3`, and `cdr(cons(3, 4))` returns `4`.

Given this implementation of cons:
```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```
Implement car and cdr.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day5.py)

---
### Day 6 [Hard]
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding `next` and `prev` fields, it holds a field named `both`, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an `add(element)` which adds the element to the end, and a `get(index)` which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to `get_pointer` and `dereference_pointer` functions that converts between nodes and memory addresses.

---
### Day 7 [Medium]
This problem was asked by Facebook.

Given the mapping `a = 1`, `b = 2`, ... `z = 26`, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day7.py)

---
### Day 8 [Easy]
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:
```
  0
 / \
1   0
   / \
  1   0
 / \
1   1
```

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day8.py)

---
### Day 9 [Hard]
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be `0` or negative.

For example, `[2, 4, 6, 2, 5]` should return `13`, since we pick `2`, `6`, and `5`. `[5, 1, 1, 5]` should return `10`, since we pick `5` and `5`.

Follow-up: Can you do this in O(N) time and constant space?

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day9.py)

---
### Day 10 [Medium]
This problem was asked by Apple.

Implement a job scheduler which takes in a function `f` and an integer `n`, and calls `f` after `n` milliseconds.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day10.py)

---
### Day 11 [Medium]
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string `de` and the set of strings `[dog, deer, deal]`, return `[deer, deal]`.

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

[Solution (Hashmap)](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day11.py)

**MISSING: TRIE SOLUTION**

---
### Day 12 [Hard]
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day12.py)

---
### Bonus: Finding The Smallest Interval Of K Sorted Lists
This interesting and difficult problem was asked by Google recently.

Given K sorted lists of integers, return the smallest interval (inclusive) that contains at least one element from each list. If there are multiple intervals of the same size, return the one that starts at the smallest number.

For example, given:
```python
[[0, 1, 4, 17, 20, 25, 31],
 [5, 6, 10],
 [0, 3, 7, 8, 12]]
```
The smallest range here is `[3, 5]`, since it contains `4` from the first list, `5` from the second list, and `3` from the third list.

Before we dive into the solution, you should take a moment to think of a solution yourself!

https://www.dailycodingproblem.com/blog/smallest-interval-of-k-sorted-lists/

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/min-interval-klist.py)

---
### Day 13 [Hard]
This problem was asked by Amazon.

Given an integer `k` and a string `s`, find the length of the longest substring that contains at most `k` distinct characters.

For example, given `s = "abcba"` and `k = 2`, the longest substring with `k` distinct characters is `"bcb"`.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day13.py)

---
### Day 14 [Medium]
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day14.py)

---
### Day 15 [Medium]
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probibility.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day15.py)

---
### Day 16 [Easy]
This problem was asked by Twitter.

You run an e-commerce website and want to record the last `N` `order` ids in a log. Implement a data structure to accomplish this, with the following API:

`record(order_id)`: adds the `order_id` to the log
`get_last(i)`: gets the `i`th last element from the log. `i` is guaranteed to be smaller than or equal to `N`.

You should be as efficient with time and space as possible.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day16.py)

---
### Day 17 [Hard]
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` represents:
```
dir
    subdir1
    subdir2
        file.ext
```
The directory `dir` contains an empty sub-directory `subdir1` and a sub-directory `subdir2` containing a file `file.ext`.

The string `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"` represents:
```
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```
The directory `dir` contains two sub-directories `subdir1` and `subdir2`. `subdir1` contains a file `file1.ext` and an empty second-level sub-directory `subsubdir1`. `subdir2` contains a second-level sub-directory `subsubdir2` containing a file `file2.ext`.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is `"dir/subdir2/subsubdir2/file2.ext"`, and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day17.py)

---
### Day 18 [Hard]
This problem was asked by Google.

Given an array of integers and a number `k`, where 1 <= k <= length of the array, compute the maximum values of each subarray of length `k`.

For example, given `array = [10, 5, 2, 7, 8, 7]` and `k = 3`, we should get: `[10, 7, 8, 8]`, since:

* `10 = max(10, 5, 2)`
* `7 = max(5, 2, 7)`
* `8 = max(2, 7, 8)`
* `8 = max(7, 8, 7)`

Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

[Solution (Deque)](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day18.py)

---
### Bonus: Anagram Indices
Given a `word` and a string `S`, find all starting indices in `S` which are anagrams of `word`.

For example, given that `word` is “ab”, and `S` is “abxaba”, return 0, 3, and 4.

https://www.dailycodingproblem.com/blog/anagram-indices/

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/anagram-indices.py)

---
### Day 19 [Medium]
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day19.py)

---
### Day 20 [Easy]
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day20.py)

---
### Day 21 [Easy]
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

---
### Day 22 [Medium]
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day22.py)

---
### Day 23 [Easy]
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

```
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
```

and start = `(3, 0)` (bottom left) and end = `(0, 0)` (top left), the minimum number of steps required to reach the end is `7`, since we would need to go through `(1, 2)` because there is a wall everywhere else on the second row.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day23.py)

---
### Day 24 [Medium]
This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

* `is_locked`, which returns whether the node is locked
* `lock`, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
* `unlock`, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.

[Solution (O(m+h) + O(h))](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day24.py)

---
### Day 25 [Hard]
This problem was asked by Facebook.

Implement regular expression matching with the following special characters:
* `.` (period) which matches any single character
* `*` (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

---
### Day 26 [Medium]
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

[Solution (Naive + Dict + Two Pointers)](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day26.py)

---
### Day 27 [Easy]
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day27.py)

---
### Bonus: Longest Increasing Subsequence

This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

https://www.dailycodingproblem.com/blog/longest-increasing-subsequence/

[Solution (naive + dp)](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/longest-increasing-subsequence.py)

---
### Day 28 [Medium]
This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

```
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
```

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day28.py)

---
### Day 29 [Easy]
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day29.py)

---
### Day 30 [Medium]
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input `[2, 1, 2]`, we can hold 1 unit of water in the middle.

Given the input `[3, 0, 1, 3, 0, 5]`, we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day30.py)

---
### Day 31 [Easy]
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day31.py)

---
### Day 32 [Hard]
This problem was asked by Jane Street.

Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.

---
### Day 33 [Easy]
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence `[2, 1, 5, 7, 2, 0, 5]`, your algorithm should print out:
```
2
1.5
2
3.5
2
2
2
```

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day33.py)

---
### Day 34 [Medium]
This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".

---
### Day 35 [Hard]
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day35.py)

---
### Day 36 [Medium]
This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day36.py)

---
### Day 37 [Easy]
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set `{1, 2, 3}`, it should return `{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}`.

You may also use a list or array to represent a set.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day37.py)

---
### Day 38 [Hard]
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

---
### Day 39 [Medium]
This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.
You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).

---
### Day 40 [Hard]
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given `[6, 1, 3, 3, 3, 6, 6]`, return `1`. Given `[13, 19, 13, 13]`, return `19`.

Do this in O(N) time and O(1) space.

---
### Day 41 [Medium]
This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights `[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]` and starting airport `'YUL'`, you should return the list `['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']`.

Given the list of flights `[('SFO', 'COM'), ('COM', 'YYZ')]` and starting airport `'COM'`, you should return null.

Given the list of flights `[('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]` and starting airport `'A'`, you should return the list `['A', 'B', 'C', 'A', 'C']` even though `['A', 'C', 'A', 'B', 'C']` is also a valid itinerary. However, the first one is lexicographically smaller.

---
### Day 42 [Hard]
This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given `S = [12, 1, 61, 5, 9, 2]` and `k = 24`, return `[12, 9, 2, 1]` since it sums up to 24.

---
### Day 43 [Easy]
This problem was asked by Amazon.

Implement a stack that has the following methods:

* `push(val)`, which pushes an element onto the stack
* `pop()`, which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
* `max()`, which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day43.py)

---
### Day 44 [Medium]
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements `A[i]` and `A[j]` form an inversion if `A[i] > A[j]` but `i < j`. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array `[2, 4, 1, 3, 5]` has three inversions: (2, 1), (4, 1), and (4, 3). The array `[5, 4, 3, 2, 1]` has ten inversions: every distinct pair forms an inversion.

---
### Day 45 [Easy]
This problem was asked by Two Sigma.

Using a function `rand5()` that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function `rand7()` that returns an integer from 1 to 7 (inclusive).

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day45.py)

---
### Day 46 [Hard]
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day46.py)

---
### Day 47 [Easy]
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given `[9, 11, 8, 5, 7, 10]`, you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

[Solution (naive + one pass)](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day47.py)

---
### Day 48 [Medium]
This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:
`[a, b, d, e, c, f, g]`

And the following inorder traversal:
`[d, b, e, a, f, c, g]`

You should return the following tree:
```
    a
   / \
  b   c
 / \ / \
d  e f  g
```

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day48.py)

---
### Day 49 [Medium]
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array `[34, -50, 42, 14, -5, 86]`, the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array `[-5, -1, -8, -9]`, the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day49.py)

---
### Day 50 [Easy]
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:
```
    *
   / \
  +    +
 / \  / \
3  2  4  5
```
You should return 45, as it is (3 + 2) * (4 + 5).

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day50.py)

---
### Day 51 [Medium]
This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.

---
### Day 52 [Hard]
This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

`set(key, value)`: sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.

`get(key)`: gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day52.py)

---
### Day 53 [Medium]
This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day53.py)

---
### Day 54 [Hard]
This problem was asked by Dropbox.

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.

---
### Day 55 [Easy]
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:
* `shorten(url)`, which shortens the url into a six-character alphanumeric string, such as zLg6wl.
* `restore(short)`, which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day55.py)

---
### Day 56 [Medium]

This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.

---
### Day 57 [Medium]
This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day57.py)

---
### Day 58 [Medium]
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array `[13, 18, 25, 2, 8, 10]` and the element `8`, return `4` (the index of 8 in the array).

You can assume all the integers in the array are unique.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day58.py)

---
### Day 59 [Hard]
This problem was asked by Google.

Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?

---
### Day 60 [Medium]
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset `{15, 5, 20, 10, 35, 15, 10}`, it would return true, since we can split it up into `{15, 5, 10, 15, 10}` and `{20, 35}`, which both add up to `55`.

Given the multiset `{15, 5, 20, 10, 35}`, it would return false, since we can't split it up into two subsets that add up to the same sum.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day60.py)

---
### Day 61 [Medium]
This problem was asked by Google.

Implement integer exponentiation. That is, implement the `pow(x, y)` function, where `x` and `y` are integers and returns `x^y`.

Do this faster than the naive method of repeated multiplication.

For example, `pow(2, 10)` should return `1024`.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day61.py)

---
### Day 62 [Medium]
This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

* Right, then down
* Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day62.py)

---
### Day 63 [Easy]
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:
```
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
```
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day63.py)

---
### Day 64 [Hard]
This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.

---
### Day 65 [Easy]
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:
```
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
```
You should print out the following:
```
1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
```

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day65.py)

---
### Day 66 [Medium]
This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day66.py)

---
### Day 67 [Hard]
This problem was asked by Google.

Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

* `set(key, value)`: sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.

* `get(key)`: gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day67.py)

---
### Day 68 [Medium]
This problem was asked by Google.

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

* (0, 0)
* (1, 2)
* (2, 2)
* (4, 0)

The board would look like this:
```
[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
```
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day68.py)

---
### Day 69 [Easy]
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is `[-10, -10, 5, 2]`, we should return `500`, since that's `-10 * -10 * 5`.

You can assume the list has at least three integers.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day69.py)

---
### Day 70 [Easy]
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.

---
### Day 71 [Easy]
Good morning! Here's your coding interview problem for today.

This problem was asked by Two Sigma.

Using a function `rand7()` that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function `rand5()` that returns an integer from 1 to 5 (inclusive).

---
### Day 72 [Hard]
This problem was asked by Google.

In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with `n` nodes and `m` directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.

The graph is represented with a string and an edge list. The `i`-th character represents the uppercase letter of the `i`-th node. Each tuple in the edge list `(i, j)` means there is a directed edge from the `i`-th node to the `j`-th node. Self-edges are possible, as well as multi-edges.

For example, the following input graph:
```
ABACA
```
```
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
```
Would have maximum value 3 using the path of vertices `[0, 2, 3, 4]`, `(A, A, C, A)`.

The following input graph:
```
A
```
```
[(0, 0)]
```
Should return null, since we have an infinite loop.

---
### Day 73 [Easy]
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day73.py)

---
### Day 74 [Medium]
This problem was asked by Apple.

Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the `i`-th row and `j`-th column is `(i + 1) * (j + 1)` (if 0-indexed) or `i * j` (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:
```
| 1 | 2  | 3  | 4  | 5  | 6  |

| 2 | 4  | 6  | 8  | 10 | 12 |

| 3 | 6  | 9  | 12 | 15 | 18 |

| 4 | 8  | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |
```
And there are 4 12's in the table.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day74.py)

---
### Day 75 [Hard]
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

---
### Day 76 [Medium]
This problem was asked by Google.

You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:
```
cba
daf
ghi
```
This is not ordered because of the a in the center. We can remove the second column to make it ordered:
```
ca
df
gi
```
So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:
```
abcdef
```
Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:
```
zyx
wvu
tsr
```
Your function should return 3, since we would need to remove all the columns to order it.

---
### Day 77 [Easy]
This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given `[(1, 3), (5, 8), (4, 10), (20, 25)]`, you should return `[(1, 3), (4, 10), (20, 25)]`.

---
### Day 78 [Medium]
This problem was asked by Google.

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

[Solution](https://github.com/nzhoward/daily-coding-problem/blob/master/solutions/day78.py)

---
### Day 79 [Medium]
This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array `[10, 5, 7]`, you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array `[10, 5, 1]`, you should return false, since we can't modify any one element to get a non-decreasing array.

---
### Day 80 [Easy]
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
```
    a
   / \
  b   c
 /
d
```

---
