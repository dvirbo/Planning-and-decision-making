from LiquidPuzzle import LiquidPuzzleState
from astar import astar


if __name__ == "__main__":
    initial_tubes = [[], [], [2, 2, 0, 3, 4], [4, 2, 2, 0, 1], [1, 0, 4, 3, 2], [4, 0, 1, 3, 1], [3, 4, 1, 0, 3]]

    initial_state = LiquidPuzzleState(initial_tubes)
    solution_path = astar(initial_state)
    if solution_path:
        print("Solution found:")
        for state in solution_path:
            print(state)
    else:
        print("No solution found.") 
        
     