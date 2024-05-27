from collections import deque
from LiquidPuzzle import LiquidPuzzleState

def astar(initial_state: LiquidPuzzleState):
    """
    A* search algorithm for the Liquid Puzzle game.
    Returns the path to the solution if one exists, None otherwise.
    """
    frontier = deque([(heuristic(initial_state), initial_state, None)])
    explored = set()

    while frontier:
        priority, current_state, parent_state = frontier.popleft()

        if current_state.is_goal():
             
            #TODO: add method that check if we have 2 or more colors in seperate tubes
            path = [current_state]
            while parent_state:
                path.append(parent_state[1])
                parent_state = parent_state[2]
            path = path[::-1] # Return the path in reverse order
            return path

        explored.add(current_state)

        for move in current_state.get_valid_moves():
            next_state = current_state.apply_move(move)

            if next_state not in explored:
                next_priority = heuristic(next_state)
                frontier.append(
                    (next_priority, next_state, (priority, current_state, parent_state))
                )

        frontier = deque(sorted(frontier, key=lambda x: x[0]))

    return None

def heuristic(state: LiquidPuzzleState) -> int:
    """
    Calculates the heuristic value for the given state in the Liquid Puzzle problem.

    The heuristic value represents the estimated number of moves required to separate all colors in the state.

    Args:
        state (LiquidPuzzleState): The current state of the Liquid Puzzle problem.

    Returns:
        int: The heuristic value for the given state.
    """
    total_moves = 0
    color_counts = {}

    # Count the number of each color in the state
    for tube in state.tubes:
        for color in tube:
            color_counts[color] = color_counts.get(color, 0) + 1

    # For each color, calculate the minimum number of moves required to separate it
    for color, count in color_counts.items():
        # If the color is already separated, no moves are required
        if count == len(state.tubes):
            continue

        # Otherwise, the minimum number of moves is the count minus the number of empty tubes
        empty_tubes = len([tube for tube in state.tubes if not tube])
        total_moves += max(0, count - empty_tubes)

    return total_moves



