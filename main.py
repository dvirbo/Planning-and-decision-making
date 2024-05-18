from LiquidPuzzle import LiquidPuzzleState
from astar import astar


if __name__ == "__main__":
    initial_tubes = [[2, 1, 3], [3, 2, 1], [2, 3, 1], []]
    initial_state = LiquidPuzzleState(initial_tubes)
    solution_path = astar(initial_state)
    if solution_path:
        print("Solution found:")
        for state in solution_path:
            print(state)
    else:
        print("No solution found.") 