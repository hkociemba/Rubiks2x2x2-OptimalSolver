# Rubiks2x2x2-OptimalSolver
## Overview
This project presents an optimal solver for the 2x2x2 Rubik's cube, computing all optimal (shortest) solving maneuvers. The computation time is negligible. The solver exclusively utilizes moves of the U, R, and F faces, as the DBL-corner remains fixed. The cube's color scheme is automatically detected.   
## Usage
Upon the initial run, a pruning table is created, requiring approximately 4 MB of disk space. The creation process takes anywhere from less than a minute to a couple of minutes, contingent on the hardware. Typically, you initiate the cube-solving server, which listens on a port of your choice, accepting the cube definition string and returning the solving maneuver. The module example.py provides detailed examples on how to commence the server and utilize a simple GUI interface that interacts seamlessly with the server.   
Execute the example file using "python example.py" or eventually "python3 example.py"

Ensure that you are using Python 3.

![](gui_client.jpg "")


