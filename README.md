<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2D Maze Generator & Solver</title>
</head>
<body>

    <h1>2D Maze Generator & Solver</h1>
    
    <p>This Python program generates a random 2D maze using the <strong>Recursive Backtracking (Depth-First Search)</strong> algorithm 
    and then solves it using the <strong>Breadth-First Search (BFS)</strong> algorithm. The maze is visualized using <strong>Pygame</strong>, 
    where walls, paths, visited cells, and the solution path are displayed with different colors.</p>

    <h2>Features</h2>
    <ul>
        <li>✅ <strong>Random Maze Generation</strong> – Creates a solvable maze using DFS.</li>
        <li>✅ <strong>Breadth-First Search (BFS) Solver</strong> – Finds the shortest path to the exit.</li>
        <li>✅ <strong>Real-time Visualization</strong> – Watch the solver dynamically explore and solve the maze.</li>
        <li>✅ <strong>Color-Coded Representation:</strong>
            <ul>
                <li>🏁 <span style="color: green;"><strong>Green</strong></span> → Exit point</li>
                <li>🛑 <span style="color: black;"><strong>Black</strong></span> → Walls</li>
                <li>🏃 <span style="color: white;"><strong>White</strong></span> → Walkable paths</li>
                <li>🔵 <span style="color: blue;"><strong>Blue</strong></span> → BFS visited cells</li>
                <li>🔴 <span style="color: red;"><strong>Red</strong></span> → Final solution path</li>
            </ul>
        </li>
    </ul>

    <h2>Installation & Usage</h2>
    <ol>
        <li>Install Pygame if you haven’t already:
            <pre><code>pip install pygame</code></pre>
        </li>
        <li>Run the program:
            <pre><code>python maze_solver.py</code></pre>
        </li>
    </ol>

    <h2>How It Works</h2>
    <ol>
        <li><strong>Maze Generation</strong>
            <ul>
                <li>A grid is initialized with walls.</li>
                <li>A randomized DFS carves out paths while ensuring a valid maze structure.</li>
            </ul>
        </li>
        <li><strong>Maze Solving (BFS)</strong>
            <ul>
                <li>The solver explores neighbors using a queue, marking visited cells.</li>
                <li>Once the exit is reached, it reconstructs the shortest path and displays it.</li>
            </ul>
        </li>
    </ol>

    <h2>Controls</h2>
    <p>🚀 The program starts automatically upon execution. Close the window to exit.</p>

    <h2>Screenshot</h2>
    <p>(Add a screenshot of your running program here)</p>

</body>
</html>
