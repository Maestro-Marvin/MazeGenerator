from DfsMaze import DfsMaze
from Interface import Interface
from FindPath import FindPath
from HandleFindPath import HandleFindPath
from KruskalMaze import KruskalMaze
from Maze import Maze
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    algo, control, rows, cols = args
    rows, cols = int(rows), int(cols)
    interface = Interface(rows, cols)
    if algo == "dfs":
        maze = DfsMaze(interface, rows, cols)
    else:
        maze = KruskalMaze(interface, rows, cols)
    if control == "auto":
        path = FindPath(maze, interface)
    else:
        path = HandleFindPath(maze, interface)
    interface.main(maze, path)
