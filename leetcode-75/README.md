# LeetCode 75 Study

https://leetcode.com/studyplan/leetcode-75/

## Array/String

### 1768 - Merge Strings Alternatively

Init result list to combined size, use while chars left with len1, len2 and i,j with str.join() result
`30ms beats 88%/93%`

### 605 - Can Place Flowers

base cases for n = 0, 1. iterate and check for i == start, end conditions, else check previous and next.
set val at i to 1, decrement count. at end of each loop check if count has reached zero
`135ms beats 35%/34%`

### 1071 - GCD of Strings

calculate GCD of both string lengths. check each string can be wholly divided by the prefix of length GCD
`41ms beats 30%/26%`

### 1431 - Kids with the Greatest Number of Candies

get max() of candies. for each i, kid in candies check if `kid + extra_candies` is `>=` to the max.
set `result[i]` to `True` if so
`35ms beats 85%/91%`

### 1657 - Determine if 2 Strings are Close

for operation 1, we can say that they must have the same set of characters. so test this by
checking that `set(word1) == set(word2)`

for operation 2, we can say that the frequencies of each character should relate, so we can
use `Counter` to map the character frequency, and then convert to a sorted list. if both lists match,
then it is possible to swap the characters so the strings match.
`122ms beats 89%/96%`

### 443 - String Compression

iterate through the string from a given start position (0) and find the ending index of the current
sequence (while the char remains the same), obtaining the count of the number of characters that are repeating.
if we have a count greater than 1, append each digit (per division of 10).
delete the remaining chars up to the end position.
update the new end position, given the resizing.
finally update the start position to the previous ending one.
`52ms beats 85%/30%`

### 345 - Reverse Vowels of a String

Use 2 pointers, left (0) and right(n - 1). Main loop while left < right
Move the 2 pointers towards the center, looking for a vowel. Check the bounds.
Reverse the chars at left,right if they are both vowels.
Also need to check if we have a vowel using .lower() on the character to be tested.
`35ms beats 99%/75%`

### 1512 - Reverse Words in a String

Using a stack, we can append each word from the input string by iterating via `.split()`
We also call `.strip()` on the input string before iteration.
We pop from the stack whilst it has elements, and append the stripped substring to a result array,
also appending a single whitespace character.
We `.pop()` the final whitespace character from the result array.
`31ms beats 87%/32%`

### 238 - Product of Array Except Self

We can make 2 passes through the array, forwards and backwards, to execute this in `O(n)`
Going forwards, calculate the prefix product for every `i` in `nums`, 
i.e. keep a `prefix` product total using `*=` for every element to the left: `i-1`. For the `0th` element,
we use a default prefix of 1. We store this `ith` result in a new `result` array.
Going backwards, calculate the postfix for every `i` in `nums` by keeping a `postfix` product total,
using `*=` for every element to the right `i+1`. For the `n-1th` element, we use a default postfix of 1.
We multiply the prefix previously stored at `result[i]` with the postfix sum, updating `result[i]`

`264ms beats 68%/77%`

## Backtracking

### 17 - Letter Combinations of a Phone Number

map digits 2-9 to their corresponding characters, using a dict set up in `__init__`
define `backtrack(i, s)` where i is `digits[i]` and s is the string we are building up
base case when i has reached the `len(digits)` it means the string is complete, so we append to result list
otherwise, we backtrack for each mapped char of `digits[i]`, we concat `s + c` mapping, and `i + 1`
`27ms beats 94%/10%`

### 216 - Combination Sum 3

Define backtrack function, taking arguments `current_combination, total, starting_number`
we start the backtracking with [], 0, 1
base case is reached when the len() of the combination reaches k.
if we have reached the target sum, then append the result to the outer result list.
for each remaining digit, we recurse with a copy of the combination list (with new number added),
the updated total, and the next starting digit.
`32ms beats 80%/79%`

## Binary Search

### 374 - Guess Number Higher or Lower

Find mid = `l + (r - l) // 2` - use this to avoid integer overflow
Start at range 1,n. Too high, move `r = mid-1`,
too low, move `l = mid + 1`
`30 ms beats 83%/68%`

### 2300 - Pairs of Spells and Potions

Sort the potions list. for each spell s, partition potions array with left, right, mid.  
for each potion while left <= right, if >= success threshold,
store this leftmost pointer index, then we attempt smaller values with right = mid - 1.  
if the threshold is not met, we attempt greater values with left = mid + 1
the leftmost index is initially set to m (potion count). the result is m - leftmost idx,
which gives us the count of potions that are >= the success threshold.
`1196ms beats 58%/93%`

### 162 - Find Peak Element

use binary search without sorting the array. use l, r, mid as per usual, while l <= r.
if the value to the left of mid is higher, then we search there by moving the right
pointer to mid - 1. if the value to the right of mid is greater, then
we search the right side by setting left to mid + 1.
otherwise we can return mid, which is a peak.
we also need to perform bounds check as the peak could be at index 0, or n - 1.
in this case, when moving to the left we also need to check that mid is > 0.
likewise, if moving to the right, we need to check that mid is < n - 1
`41ms beats 87%/37%`

### 875 - Koko Eating Bananas

The brute force approach would be to try all possible eating speeds (k) and record the
minimum that works. Worst case that would be `O(max(p).n)` where `max(p)` is the largest pile,
and n the number of piles.
Given we want to find a k that works, we can use Binary Search on the k range `(1, max(p))`,
which will reduce the time complexity to `O(max(p).log n)`
So here `left = min speed`, whilst `right = max speed`. The max speed would be equal to the largest
pile of bananas, given `n <= h` - so we can eat all piles in n hours in the worst case.
So while `left <= right` we find the mid point, which is our possible k (current eating speed).
Given this eating speed, we divide each pile by it to find the total hours it would take to eat
each pile. We round up to the nearest hour using `ceil(pile / speed)`.
Summing all the hours, we have the total time to eat all piles.
If this is `<= h` then it means that this new k value is valid. As we want the minimum possible k,
we compare/swap it with the previous `min_k = min(min_k, new_valid_k)`.
As this speed worked, we want to next try a slower speed, so we will choose a new k from the
left portion of the k range, by moving the right (max speed) pointer to `mid - 1`.
If the hours it took to eat all piles exceeded input h (our target) then we want to try
a faster speed, so we choose a k from the right portion of the array by updating the left pointer
to `mid + 1`
When the iteration ends, we have our minimum k result.
`239ms beats 96%/57%`


## Binary Tree

### Binary Tree - DFS

### 104 - Max Depth

recursive DFS = base case if root is None return 0.
Return 1 + max of (recurse node.left , recurse node.right)
`35 ms beats 86%/10%`

### 1448 - Count Good Nodes

DFS using recursion - base case return 0 if node is null.
Use Pre Order traversal (process current node value before recursing left and right).
dfs helper method takes current, max_in_path.
we start recursion with root, root.val as the max so far.
for each pre order traversal, compare if the val at this node is <= max so far,
we add 1 to the total count if so, else 0.
we add this current node value to the recursive calls for .left and .right
`116ms beats 93%/27%`

### Path Sum 3

Using DFS with a running total and a cache of sums->frequency, we can traverse the tree
and count the number of times the prefix sum has been found in that branch.
The prefix sum is defined as `(current total - target sum)`
This means that `target sum == (current total - prefix sum)`
So for each branch, we count the number of times the prefix sum is encountered.
`41ms beats 89%/38%`

### Binary Tree - BFS

### 1161 - Max Level Sum Subtree

Use a deque with append and `popleft()`
Enqueue the level and node.
Use default dict to map levels to sum
Dequeue each node, add its sum to the dict
Return `max()` of dict with `key=dict.get` to return the key with max value
`164ms beats 39%/66%`

### 199 - Right Side View

we use a deque as a queue, append to end and popleft() to dequeue.
while the queue has elements, we empty it for every iteration, processing all nodes at the current level,
from left to right. for each node popped from the queue, we append its left and right children, and
set a right-most pointer to the node. at the end of each emptying of the queue/level, we have a pointer
to the right most. so if it is valid, we can obtain its value.
`27ms beats 97%/8%`

## Binary Search Tree

### 700 - Search in a BST

base case of root equal to None. Using Pre order traversal, base case of root.val matching search val.
otherwise, if val is smaller and we have a left subtree, recurse left,
or if val is greater and we have a right subtree, recurse right.
`53ms beats 72%/84%`

## Bit Manipulation

### 338 - Counting Bits

initialise a result array of size n + 1
iterate from 0 to n, inclusive as val.
for this val, shift right and use this as the index
also bitwise and with 1, and add this to the value at the index
`56ms beats 86%/49%`

### 136 - Single Number

We can keep a cumulative XOR value for all numbers in the array.
The number which has no duplicate will not be cancelled out, so will be the remainder.
`96ms beats 98%/73%`

## DP - 1D

### 1137 - nth Tribonacci Number

initialise tribs as `[0, 1, 1]`
for i in range 3, n + 1 (to include `tribs[n]`) calculate `tribs[i]` as `sum(tribs[i-3], tribs[i-2], tribs[i-1])`
result is `tribs[n]`
`25ms beats 96%/82%`

### Min Cost of Climbing Stairs

use a dp list of length n + 2. set the cost of the out of bounds steps to 0.
now we go backwards from the first step, and calculate the cost of this step as
the ith cost, plus the minimum of the 2 steps above it, from the dp list.
the answer is the minimum of the 0, 1 steps
`51ms beats 79%/22%`

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
`32ms beats 79%/41%`

## Binary Search Tree

### 700 - Search in a BST

base case of root equal to None. base case of root.val matching search val.
otherwise, if val is smaller and we have a left subtree, recurse left,
or if val is greater and we have a right subtree, recurse right.
`53ms beats 72%/84%`

## Graphs

### Graphs - DFS

### 841 - Keys and Rooms

Keep track of visited rooms. Recurse for room and all_keys set
For each visited room, iterate recursively for each key
If key is not in all_keys for that room, exit
Base cases to exit are if room number is >=n or if the room is already visited
`54ms beats 98%/22%`

### 547 - Number of Provinces (DFS)

keep a region count and visited set. let n be the length of the n * n matrix
iterate city in range n, if city has not been visited, increment the region count and run dfs on the city.
inside dfs, add the city to the visited set. iterate each neighbour in range n, if there is a connection
at provinces[city][neighbour] == 1 AND the neighbour has not been visited, then call dfs on the neighbour
finally return the region/province count
`174 ms beats 94%/8%`

### 547 - Number of Provinces (Union Find)

maintain parent[] and rank[]. index is the node number. value is parent and rank.
result is initially the number of nodes
2 methods, find root parent (which also performs path compression) and union (merge)
we iterate through each city/neighbour n/n and for each connection, we attempt a union
and decrement this from the nodes count.
`191ms beats 33%/45%`

### 972 - Leaf Similar Trees

define recursive dfs() with base case of None/null return [], and case when node is a leaf - return [val]
add the left and right subtrees recursively, returning the joint arrays.
call dfs for both root nodes, and compare the resulting leaf arrays
`40ms beats 27%/94%`

### Graphs - BFS

### 1926 - Nearest Exit from Maze Entrance

Use deque as queue for BFS. mark visited as +
Logic for is valid step, boundaries, wall, entrance
Enqueue count, next valid steps once visited
`685ms beats 40%/64%`

### 994 - Rotting Oranges

get all rotten oranges, enqueue them. also keep track of all fresh oranges in a set.
using BFS, empty the queue, mark each as rotten. remove from fresh oranges set, keep track of each cell
so we can enqueue its neighbours if that neighbouring cell is a fresh orange
at each queue emptying, this represents 1 BFS level, so increment the minutes / count
if at the end there are still fresh oranges remaining, we return -1, otherwise the minute count
`44 ms beats 88%/65%`

## Hashmap / Set

### 2215 - Find the Difference of 2 Arrays

Using `set()` and `difference()` between the 2 lists
`127ms beats 98%/24%`

### 1207 - Unique Number of Occurrences

Use `collections.Counter`
Init a `set()` Iterate over `values()` and check if count exists in set. False if so.
True once iteration finishes.
`45ms beats 30%/7%`

### 2352 - Equal Row and Column Pairs

Iterate over each row, convert it to a tuple so we can hash it.
We store the count of each row hash in a default dict.
We also will keep an overall count of found matches.
Next, we iterate over each set of columns. We can do this neatly using `for cols in zip(*grid):`
Again, we convert the columns to a tuple, and hash it. If this hash exists in the row dict,
we add that row count value to the overall count.
`364ms beats 96%/53%`

## Heap

### 215 - 4th Largest Element in an Array

Using heaps - create negative elements list - heapify it and heap pop k times
Return the last popped val
`617ms beats 22%/85%`

### 2336 - Smallest Number in an Infinite Set

Use heapq and keep sequence, init to 1, on heap.
when popping smallest, if heap is not empty, pop and return. otherwise, return sequence + 1
when adding back, if number not currently in heap, and it is less than sequence, add it back
`87ms beats 86%/47%`

### 2542 - Maximum Subsequence Score

We need to maximize the choice from n2, and minimize the choice for removal from n1
when we exceed k.
We store the index-connected data in pairs, and sort this array in descending order by n2
(the second element of the pair).
We loop through these pairs of `n1, n2`. We keep an n1 sum, and append n1 to the min heap.
When we reach a length > k, we pop and subtract it from our n1 sum.
When k is reached, we calculate the sum, and retain the maximum sum seen so far.
`746ms beats 75%/93%`

## Linked List

### 2095 - Delete the Middle Node of a Linked List

Create dummy node that points to head
Use Fast/Slow pointer technique - `slow = next`, `fast = next.next`
Once fast reaches end, slow will point to the middle node.
Set `slow.next = slow.next.next`
return dummy.next
`576ms beats 92%/64%`

### 328 - Odd/Even Linked List

Maintain odd, even pointers and head pointers.
loop while current pointer is non-null, current = current.next at end of iteration.
Maintain is_even boolean switch, which flips each iteration.
if head nodes are not set, they are assigned. otherwise set the odd/even .next to current, and
update odd/even to same.
After iteration has finished, append the even head to the odd.next.
Ensure we set even.next to None to avoid a cycle.
`34ms beats 89%/98%`

### 206 - Reverse Linked List

We have 2 pointers, `curr (head)` and `prev (None)`.
while curr is valid, we traverse the list.
We store a temp pointer to the next node `curr.next`
Then reassign `curr.next` to prev (reversing the direction).
Finally we update our `prev` pointer to the current node, and `curr` to the temporary pointer,
which is the next node in the iteration.
When iteration ends, we return the `prev` pointer, which will point at the new head of the
reversed list.
`28ms beats 96%/98%`

## Prefix Sum

### 1732 - Find Highest Altitude

Sum previous += current. Keep track of max() which is initialised at 0, which is the starting point.
`38 ms beats 58%/43%`

### 724 - Find Pivot Index

get sum(nums). iterate thru nums, prefix sum += current nums[i]
postfix sum is total - prefix sum - nums[i]
if pre and postfix sums equal, return i
`121ms beats 68%/67%`

## Queue

### 933 - Number of Recent Calls

Use a deque to maintain queue of requests.
each time a ping is added, `while head q[0] is < (t - 3000)`  then `.popleft()`
this removes any older elements that exceed the threshold
return the new length of the queue
`187ms beats 82%/42%`

### 649 - Dota2Senate

Use 2 queues, one for each 'team'.  
Enqueue the associated index of each element in the senate string, so we retain the ordering.
whilst both queues have elements, pop left (dequeue).
the smallest element has priority, so it is appended to the back of its queue, plus n,
the total number of senators.
One queue will be emptied first, the queue which still has remaining senators wins.
`50ms beats 64%/48%`

## Sliding Window

### 643 - Maximum Average Subarray

Sliding window (fixed) - get initial window sum 0 - k.
Keep pre_sum and post_sum total until greater max is found.
Remember to reset the pre/post sum totals if we find a greater value
shift left and right pointers of the window by 1
`848ms beats 96%/99%`

### 1456 - Max Num of Vowels in Given Substring Length

Left and right window (fixed), create initial substring window and use Counter with map function to only return
vowel counts.
Then check l and r moving the window at end of the loop, -/+ max count so far
`102ms beats 86%/19%`

### 1004 - Max Consecutive Ones 3

Dynamic sliding window. 2 pointers. right iterates through array O(n)
For each iteration, try always take k from the current value at the right pointer.
If k goes below 0, we need to make up for it by taking from the left pointer value, and shifting left by 1.
For each iteration, calculate the longest so far, which is right - left + 1.
`444 ms beats 52%/68%`

### 1492 - Longest Subarray after Deleting a Single Element

Dynamic sliding window. Left and Right pointer, also keep track of the 0 count, and the maximum
subarray length found so far.
Right moves constantly +1 element each iteration.
We only allow maximum of 1 zero in the sliding window.
if the right element is a zero, add 1 to zero count.
move the left pointer while the zero count is greater than 1.
For each move of the window, update the maximum length so far.
`450ms beats 67%/76%`

## Stack

### 2390 - Remove Stars from String

Using deque was slower. Also iterating with index of string was slower.
Use simple list [] with append(char) and pop() return str join the stack (list)
`117ms beats 98%/62%`

### 735 - Asteroid Collision

Use a stack [] iterate through the asteroids O(n) - for each a
loop while a is moving left (<0) and top of stack[-1] is moving right (>0)
this means a collision, so get the diff and handle each case, setting a to 0, or pop the stack
if a is non zero at the end of the while loop, add it to the stack
`71ms beats 97%/24%`

### 394 - Decode String

Using a stack, iterate character by character.
We push to the stack until we reach a closing bracket ']'
This case means we want to process a sub-problem, expand it out, pushing the result back to the stack.
We pop until we reach the opening bracket '['. Pop that, and then pop all the digits until either the
stack is empty, or we reach a non-numeric character.
Expand the sub string, and push this back to the stack.
The result is the stack contents, so we convert to a string.
`30ms beats 84%/92%`

## Two Pointers

### 283 - Move Zeros

use 2 pointer approach. iterate through list with i, also maintain an index that points to
the last non-zero element (initially at index 0). for each i value, if it is non zero,
swap current and last non-zero positions and increment the non-zero index.
`120 ms beats 86%/78%`

### 11 - Container With Most Water

2 pointer approach left (0), right (n - 1) with max volume found so far (0).
while left < right, we calculate the volume based on distance and the min() of
the left and right heights. conditionally update the max found so far.
we only move the pointer which has the smallest height
i.e. move left idx if left height is < right height, else move right idx
`514ms beats 77%/95%`

### 392 - Is Subsequence

iterate through string to be checked (O(n)) keep another pointer for the target string, only
incrementing when a match is found, also decrementing a count. when the count reaches 0 at the
end of an iteration, we can return True. if we do not reach this point, then the result must be False
`32ms beats 79%/40%`

### 1679 - Max Number of K Sum Pairs

2 pointer approach, `left = 0, right = n - 1`, `while left < right`
Sort the integer array.
For each iteration, see if the sum the 2 pointer values == k. If so, we increment count and move both
pointers towards each other,
If the sum is greater, we move the right pointer towards the middle.
If the sum is smaller, we move the left pointer towards the middle.
`482ms beats 85%/49%`