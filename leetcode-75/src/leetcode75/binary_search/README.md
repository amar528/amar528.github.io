# Binary Search

The input array should normally be sorted for this to work as expected (an exception here is Find Peak Element).
This algorithm involves partitioning the input array into 2, around a mid point.
So we have `left, right, and mid` pointers.
Calculating the mid can be done with `mid = (left + right) // 2` however this can result in overflow.
To guard against overflow, we can use `mid = left + (right - left) // 2`
Our search will be narrowed down each time into one half of the partitioned array.
If the searched item is less than the item at `mid`, then we use the left portion of the array, by moving
the right pointer: `right = mid - 1`.
Likewise, if the searched for item is greater than that pointed to by `mid`, we will search the right
portion of the array, by moving the left pointer: `left = mid + 1`
We continue like this until the element is found.
This means rather than operating in a linear way O(n), we are able to process data in O(log n)  