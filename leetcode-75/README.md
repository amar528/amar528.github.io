# LeetCode 75 Study

https://leetcode.com/studyplan/leetcode-75/

## Array/String

### 1768 - Merge Strings Alternatively

Init result list to combined size, use while chars left with len1, len2 and i,j with str.join() result - 30ms beats
88%/93%

### 605 - Can Place Flowers

base cases for n = 0, 1. iterate and check for i == start, end conditions, else check previous and next.
set val at i to 1, decrement count. at end of each loop check if count has reached zero
135ms beats 35%/34%

### 1071 - GCD of Strings

calculate GCD of both string lengths. check each string can be wholly divided by the prefix of length GCD
41ms beats 30%/26%

### 1431 - Kids with the Greatest Number of Candies

get max() of candies. for each i, kid in candies check if kid + extra_candies is >= to the max.
set result[i] to True if so
35ms beats 85%/91%

## Backtracking

### 17 - Letter Combinations of a Phone Number

map digits 2-9 to their corresponding characters, using a dict set up in __init__
define backtrack(i, s) where i is digits[i] and s is the string we are building up
base case when i has reached the len(digits) it means the string is complete, so we append to result list
otherwise, we backtrack for each mapped char of digits[i], we concat s + c mapping, and i + 1
27ms beats 94%/10%

### 216 - Combination Sum 3
define backtrack function as current_combination, total, starting_number.
we start the backtracking with [], 0, 1
base case is reached when the len() of the combination reaches k.
if we have reached the target sum, then append the result to the outer result list.
for each remaining digit, we recurse with a copy of the combination list (with new number added),
the updated total, and the next starting digit.
32ms beats 80%/79%

## Binary Search

### 374 - Guess Number Higher or Lower

Find mid = l + (r - l) // 2 - use this to avoid integer overflow
Start at range 1,n. Too high, move r = mid-1, too low,
move l = mid + 1
30 ms beats 83%/68%

### 2300 - Pairs of Spells and Potions

sort the potions list. for each spell s, partition potions array with left, right, mid.  
for each potion while left <= right, if >= success threshold,
store this leftmost pointer index, then we attempt smaller values with right = mid - 1.  
if the threshold is not met, we attempt greater values with left = mid + 1
the leftmost index is initially set to m (potion count). the result is m - leftmost idx,
which gives us the count of potions that are >= the success threshold.
1196ms beats 58%/93%

## Binary Tree

### DFS

### 104 - Max Depth

Base case if root is None return 0.
Return 1 + max of (recurse node.left , recurse node.right)
35 ms beats 86%/10%

### BFS

### 1161 - Max Level Sum Subtree

Use a deque with append and popleft()
Enqueue the level and node.
Use default dict to map levels to sum
Dequeue each node, add its sum to the dict
Return max of dict with key=dict.get to return the key with max value
164ms beats 39%/66%

## Binary Search Tree

### 700 - Search in a BST

base case of root equal to None. base case of root.val matching search val.
otherwise, if val is smaller and we have a left subtree, recurse left,
or if val is greater and we have a right subtree, recurse right.
53ms beats 72%/84%

## DP - 1D

### 1137 - nth Tribonacci Number

initialise tribs as [0, 1, 1]
for i in range 3, n + 1 (to include tribs[n]) calculate tribs[i] as sum(tribs[i-3], tribs[i-2], tribs[i-1])
result is tribs[n]
25ms beats 96%/82%


## DP - nD

### 62 - Unique Paths

Using dp, we can calculate each 'current' row in reverse order, given the previous row.
The bottom row will only ever contain 1's (same as the rightmost column) as there is only always
one move to make (we can only move right, or down in these cases).
Working in reverse order, we calculate the current cell value to be the sum of the cells that are to
the right, and down. i.e. current_row[j] = current_row[j + 1] + previous_row[j]
we iterate not only in reverse order, but also starting at n - 2 as we know the rightmost column will
always be 1.
For each row in range m - 1, calculate the current row, update the previous row to the current one.
Finally we can return the value at current_row[0] as it will contain all the possible ways to reach
the bottom right cell.
32ms beats 79%/41%

## Binary Search Tree

### 700 - Search in a BST

base case of root equal to None. base case of root.val matching search val.
otherwise, if val is smaller and we have a left subtree, recurse left,
or if val is greater and we have a right subtree, recurse right.
53ms beats 72%/84%

## Graphs

### DFS

### 841 - Keys and Rooms

Keep track of visited rooms. Recurse for room and all_keys set
For each visited room, iterate recursively for each key
If key is not in all_keys for that room, exit
Base cases to exit are if room number is >=n or if the room is already visited
54ms beats 98%/22%

### 547 - Number of Provinces (DFS)

keep a region count and visited set. let n be the length of the n * n matrix
iterate city in range n, if city has not been visited, increment the region count and run dfs on the city.
inside dfs, add the city to the visited set. iterate each neighbour in range n, if there is a connection
at provinces[city][neighbour] == 1 AND the neighbour has not been visited, then call dfs on the neighbour
finally return the region/province count
174 ms beats 94%/8%

### 547 - Number of Provinces (Union Find)

maintain parent[] and rank[]. index is the node number. value is parent and rank.
result is initially the number of nodes
2 methods, find root parent (which also performs path compression) and union (merge)
we iterate through each city/neighbour n/n and for each connection, we attempt a union
and decrement this from the nodes count.
191ms beats 33%/45%

### 972 - Leaf Similar Trees

define recursive dfs() with base case of None/null return [], and case when node is a leaf - return [val]
add the left and right subtrees recursively, returning the joint arrays.
call dfs for both root nodes, and compare the resulting leaf arrays
40ms beats 27%/94%

### BFS

### 1926 - Nearest Exit from Maze Entrance

Use deque as queue for BFS. mark visited as +
Logic for is valid step, boundaries, wall, entrance
Enqueue count, next valid steps once visited
685ms beats 40%/64%

### 994 - Rotting Oranges

get all rotten oranges, enqueue them. also keep track of all fresh oranges in a set.
using BFS, empty the queue, mark each as rotten. remove from fresh oranges set, keep track of each cell
so we can enqueue its neighbours if that neighbouring cell is a fresh orange
at each queue emptying, this represents 1 BFS level, so increment the minutes / count
if at the end there are still fresh oranges remaining, we return -1, otherwise the minute count
44 ms beats 88%/65%

## Hashmap / Set

### 2215 - Find the Difference of 2 Arrays

Using set() and difference() between the 2
127ms beats 98%/24%

### 1207 - Unique Number of Occurrences

Use collections.Counter.
Init a set() Iterate over values() and check if count exists in set. False if so. True once iteration finishes.
45ms beats 30%/7%

## Heap

### 215 - 4th Largest Element in an Array

Using heaps - create negative elements list - heapify it and heap pop k times
Return the last popped val
617ms beats 22%/85%

### 2336 - Smallest Number in an Infinite Set

Use heapq and keep sequence, init to 1, on heap.
when popping smallest, if heap is not empty, pop and return. otherwise, return sequence + 1
when adding back, if number not currently in heap, and it is less than sequence, add it back
87ms beats 86%/47%

## Linked List

### 2095 - Delete the Middle Node of a Linked List

Create dummy node that points to head
Use Fast/Slow pointer - slow goes next, fast next.next
Once fast reaches end, set slow.next = slow.next.next
return dummy.next
576ms beats 92%/64%

## Prefix Sum

### 1732 - Find Highest Altitude

Sum previous += current. Keep track of max() which is initialised at 0, which is the starting point.
38 ms beats 58%/43%

### 724 - Find Pivot Index

get sum(nums). iterate thru nums, prefix sum += current nums[i]
postfix sum is total - prefix sum - nums[i]
if pre and postfix sums equal, return i
121ms beats 68%/67%

## Queue

### 933 - Number of Recent Calls

Use a deque to maintain queue of requests.
each time a ping is added, while head q[0] is < (t - 3000) popleft()
this removes any older elements that exceed the threshold
return the new length of the queue
187ms beats 82%/42%

## Queue

### 933 - Number of Recent Calls

Use a deque to maintain queue of requests.
each time a ping is added, while head q[0] is < (t - 3000) popleft()
this removes any older elements that exceed the threshold
return the new length of the queue
187ms beats 82%/42%

## Sliding Window

### 643 - Maximum Average Subarray

Initial try brute force While loop with max so far sliding window times out - O(n * k)
Sliding window - get sum 0 - k. Keep presum and postsum total until greater max is found. Remember to reset the pre/post
sum totals
900ms beats 41%/97%

### 1456 - Max Num of Vowels in Given Substring Length

Left and right window, create initial substring window and use Counter with map function to only return vowel counts.
Sum these together.
Then check l and r moving the window at end of the loop, -/+ max count so far
102ms beats 86%/19%

## Stack

### 2390 - Remove Stars from String

Using deque was slower. Also iterating with index of string was slower.
Use simple list [] with append(char) and pop() return str join the stack (list)
117ms beats 98%/62%

### 735 - Asteroid Collision

Use a stack [] iterate through the asteroids O(n) - for each a
loop while a is moving left (<0) and top of stack[-1] is moving right (>0)
this means a collision, so get the diff and handle each case, setting a to 0, or pop the stack
if a is non zero at the end of the while loop, add it to the stack
71ms beats 97%/24%

## Two Pointers

### 283 - Move Zeros

Use i, j. i is main O(n) loop. Only increment j if it is a zero, use pop and append
130ms beats 45%/78%

### 11 - Container With Most Water

2 pointer approach left, right with max so far.
Instead of full iteration, can move pointers conditionally.
i.e. move left idx if left height is < right height, else move right idx
528ms beats 50%/89%

### 392 - Is Subsequence

iterate through string to be checked (O(n)) keep another pointer for the target string, only
incrementing when a match is found, also decrementing a count. when the count reaches 0 at the
end of an iteration, we can return True. if we do not reach this point, then the result must be False
32ms beats 79%/40%