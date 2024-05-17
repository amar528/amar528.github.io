#!/usr/bin/env bash

BASE=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Brittle - TODO refactor into /src /test modules and fix imports
PYTHON=$BASE/.venv/bin/python3

cd Array_String || exit
$PYTHON -m unittest
cd $BASE || exit

cd Backtracking || exit
$PYTHON -m unittest
cd $BASE || exit

cd Binary_Search || exit
$PYTHON -m unittest
cd $BASE || exit

cd Binary_Search_Tree || exit
$PYTHON -m unittest
cd $BASE || exit

cd Binary_Tree/DFS || exit
$PYTHON -m unittest
cd $BASE || exit

cd Binary_Tree/BFS || exit
$PYTHON -m unittest
cd $BASE || exit
