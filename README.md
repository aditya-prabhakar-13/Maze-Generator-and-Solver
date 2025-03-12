# Maze-Generator-and-Solver
This Python program generates a random 2D maze using the Recursive Backtracking (Depth-First Search) algorithm and then solves it using the Breadth-First Search (BFS) algorithm. The maze is visualized using Pygame, where walls, paths, visited cells, and the solution path are displayed with different colors.

#Features
✅ Random Maze Generation – The program creates a maze with a grid-based structure, ensuring a solvable path.
✅ Breadth-First Search (BFS) Solver – The solver finds the shortest path from the start to the end of the maze.
✅ Real-time Visualization – Watch the solver explore the maze and find the path dynamically.
✅ Color-Coded Representation

🏁 Green → Exit point
🛑 Black → Walls
🏃 White → Walkable paths
🔵 Blue → BFS visited cells
🔴 Red → Final solution path

#Installation & Usage
Install Pygame if you haven’t already:

'''pip install pygame'''

Run the program:
python maze_solver.py

#How It Works
Maze Generation

A grid is initialized with walls.
A randomized DFS carves out paths while ensuring a valid maze structure.
Maze Solving (BFS)

The solver explores neighbors using a queue, marking visited cells.
Once the exit is reached, it reconstructs the shortest path and displays it.
Controls
🚀 The program starts automatically upon execution. Close the window to exit.
