#!/usr/bin/env bash

BASE=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Brittle - TODO refactor into /src /test modules and fix imports
PYTHON=$BASE/.venv/bin/python3

for TEST_DIR in Array_String Backtracking Binary_Search Binary_Search_Tree Binary_Tree/BFS Binary_Tree/DFS Bit_Manipulation DP_1D DP_nD Graphs/BFS Graphs/DFS Hashmap_Set Heap Linked_List Prefix_Sum Queue Sliding_Window Stack Two_Pointers
do
cd $TEST_DIR || exit
$PYTHON -m unittest
cd $BASE || exit
done