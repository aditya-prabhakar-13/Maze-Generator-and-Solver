# 2D Maze Generator & Solver  

This Python program generates a random 2D maze using the **Recursive Backtracking (Depth-First Search)** algorithm  
and then solves it using the **Breadth-First Search (BFS)** algorithm. The maze is visualized using **Pygame**,  
where walls, paths, visited cells, and the solution path are displayed with different colors.  

## Features  
- ✅ **Random Maze Generation** – Creates a solvable maze using DFS.  
- ✅ **Breadth-First Search (BFS) Solver** – Finds the shortest path to the exit.  
- ✅ **Real-time Visualization** – Watch the solver dynamically explore and solve the maze.  
- ✅ **Color-Coded Representation:**  
  - 🏁 **Green** → Exit point  
  - 🛑 **Black** → Walls  
  - 🏃 **White** → Walkable paths  
  - 🔵 **Blue** → BFS visited cells  
  - 🔴 **Red** → Final solution path  

## Installation & Usage  
1. Install Pygame if you haven’t already:  
   ```bash
   pip install pygame
