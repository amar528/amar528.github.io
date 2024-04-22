# LeetCode 75 Study

https://leetcode.com/studyplan/leetcode-75/

## Array/String

### 1768 - Merge Strings Alternatively
Init result list to combined size, use while chars left with len1, len2 and i,j with str.join() result - 30ms beats 88%/93%

### 605 Can Place Flowers
base cases for n = 0, 1. iterate and check for i == start, end conditions, else check previous and next.
set val at i to 1, decrement count. at end of each loop check if count has reached zero
135ms beats 35%/34%

## Two Pointers

### 283 - Move Zeros
Use I, J. I is main O(n) loop. Only increment J if it is a zero, use pop and append
130ms beats 45%/78%

### 11 - Container With Most Water
2 pointer approach left, right with max so far.
Instead of full iteration, can move pointers conditionally.
i.e. move left idx if left height is < right height, else move right idx
528ms beats 50%/89%

## Sliding Window

### 643 - Maximum Average Subarray
Initial try brute force While loop with max so far sliding window times out - O(n * k)
Sliding window - get sum 0 - k.  Keep presum and postsum total until greater max is found.  Remember to reset the pre/post sum totals
900ms beats 41%/97%

### 1456 - Max Num of Vowels in Given Substring Length
Left and right window, create initial substring window and use Counter with map function to only return vowel counts. Sum these together.
Then check l and r moving the window at end of the loop, -/+ max count so far
102ms beats 86%/19%
## Stack

### 2390 - Remove Stars from String
Using deque was slower. Also iterating with index of string was slower.
Use simple list [] with append(char) and pop() return str join the stack (list)
117ms beats 98%/62%

## Binary Search

### 374 - Guess Number Higher or Lower
Find mid = l + (r - l) // 2 - use this to avoid integer overflow
Start at range 1,n. Too high, move r = mid-1, too low,
move l = mid + 1
30 ms beats 83%/68%

## Binary Tree

### DFS

### 104 Max Depth
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

## Heap

### 215 - 4th Largest Element in an Array
Using heaps - create negative elements list - heapify it and heap pop k times
Return the last popped val
617ms beats 22%/85%

### 2336 Smallest Number in an Infinite Set
Use heapq and keep sequence, init to 1, on heap.
when popping smallest, if heap is not empty, pop and return. otherwise, return sequence + 1
when adding back, if number not currently in heap, and it is less than sequence, add it back
87ms beats 86%/47%

## Prefix Sum

### 1732 - Find Highest Altitude
Sum previous += current.  Keep track of max() which is initialised at 0, which is the starting point.
38 ms beats 58%/43%

## Graphs

### DFS

### 841 - Keys and Rooms
Keep track of visited rooms.  Recurse for room and all_keys set
For each visited room, iterate recursively for each key
If key is not in all_keys for that room, exit
Base cases to exit are if room number is >=n or if the room is already visited
54ms beats 98%/22%

### 547 - Number of Provinces
keep a region count and visited set. let n be the length of the n * n matrix
iterate city in range n, if city has not been visited, increment the region count and run dfs on the city.
inside dfs, add the city to the visited set. iterate each neighbour in range n, if there is a connection 
at provinces[city][neighbour] == 1 AND the neighbour has not been visited, then call dfs on the neighbour
finally return the region/province count
175 ms beats 92%/18%

### BFS

### 1926 - Nearest Exit from Maze Entrance
Use deque as queue for BFS. mark visited as +
Logic for is valid step, boundaries, wall, entrance
Enqueue count, next valid steps once visited
685ms beats 40%/64%

## Hashmap / Set

### 2215 Find the Difference of 2 Arrays
Using set() and difference() between the 2
127ms beats 98%/24%

### 1207 Unique Number of Occurrences
Use collections.Counter.
Init a set() Iterate over values() and check if count exists in set. False if so. True once iteration finishes.
45ms beats 30%/7%

## Linked List

### 2095 - Delete the Middle Node of a Linked List
Create dummy node that points to head
Use Fast/Slow pointer - slow goes next, fast next.next
Once fast reaches end, set slow.next = slow.next.next
return dummy.next
576ms beats 92%/64%