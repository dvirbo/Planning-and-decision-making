from LiquidPuzzle import LiquidPuzzleState
from astar import astar


if __name__ == "__main__":
    initial_tubes = [[], [], [2, 3, 3, 2, 1], [1, 2, 4, 4, 2], [0, 0, 3, 3, 1], [1, 4, 2, 4, 0], [3, 4, 0, 1, 0]]

    initial_state = LiquidPuzzleState(initial_tubes)
    solution_path = astar(initial_state)
    if solution_path:
        print("Solution found:")
        for state in solution_path:
            print(state)
    else:
        print("No solution found.") 
        
     