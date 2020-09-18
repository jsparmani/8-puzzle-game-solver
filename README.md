# 8PuzzleGameSovler
Using python to solve the eight puzzle game antomatically!

Initial State -> Goal State
## Introduction
8-Puzzle is a square board with 9 tiles. There are 8 of them have number on it which is through 1-8 and also a blank tile. The player can swap the blank tile with its adjacent (horizontally and vertically) tile each time. 

The objective in the game is to begin with an arbitrary configuration of tiles, and move them to get the target configuration of tiles as shown in the above figure.

## Environment
Language: Python3.8

Modules: time

## Implementation
8-Puzzle problem is actually a **state space search** which means to find a path from inital state to goal state.

In this python program, I implemented the following **search algorithms**:
* Breadth First Search (BFS)

The final report will give you a comparision between each algorithm based on different heuristic functions, which includes:
* Algorithm Name
* Heuristic Function
* Elapsed Time
* Number of Steps
* Solution Path

## Usage
###### step 1
Open the `input.txt`, and type in the initial state. e.g. 3 2 4 1 5 6 x 7 9 8

x represent the blank tile

###### step 2
Open the termianl, type in `python main.py`.

###### step 3
Open the output.txt, you can get the final report.