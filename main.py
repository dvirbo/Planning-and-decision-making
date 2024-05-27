from LiquidPuzzle import LiquidPuzzleState
from astar import astar
import time


if __name__ == "__main__":
    initial_tubes = [[1,3,5,4,4,7,6,1],[2,2,0,0,4,3,6,7],
        [2,1,1,4,5,6,0,2],[0,6,6,5,4,7,7,3],
        [3,4,1,0,5,7,4,4],[7,6,2,2,3,1,0,0],
        [7,3,3,1,2,5,5,6],[7,6,5,5,3,2,1,0],[],[]]

    initial_state = LiquidPuzzleState(initial_tubes)
    start_time = time.time()
    solution_path, moves= astar(initial_state)
    end_time = time.time()
    if solution_path:
        print("Solution found:")
        for state in solution_path:
            print(state)
    else:
        print("No solution found.")

    
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
    print("moves: ", moves)   
     