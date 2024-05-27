from collections import deque
from LiquidPuzzle import LiquidPuzzleState


def astar(initial_state: LiquidPuzzleState):
    """
    A* search algorithm for the Liquid Puzzle game.

    Args:
        initial_state (LiquidPuzzleState): The initial state of the game.

    Returns:
        tuple: A tuple containing the path to the solution and the number of moves taken.
               The path is a list of states from the initial state to the goal state.
               If a solution does not exist, None is returned.
    """
    frontier = deque([(heuristic(initial_state), initial_state, None)])
    explored = set()
    explored_states = {}
    moves = 0

    while frontier:
        priority, current_state, parent_state = frontier.popleft()
        current_state_hash = hash(current_state)

        if current_state.is_goal():
            path = [current_state]
            while parent_state:
                path.append(parent_state[1])
                parent_state = parent_state[2]
            path.reverse() # Return the path in reverse order
            return path, moves

        if current_state_hash not in explored:
            explored.add(current_state_hash)
            explored_states[current_state_hash] = current_state

            for move in current_state.get_valid_moves():
                next_state = current_state.apply_move(move)
                next_state_hash = hash(next_state)

                if next_state_hash not in explored:
                    moves += 1
                    next_priority = heuristic(next_state)
                    frontier.append(
                        (
                            next_priority,
                            next_state,
                            (priority, current_state, parent_state),
                        )
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

    """
    
            for move in current_state.get_valid_moves():
                if move not in explored:
                    next_state = current_state.apply_move(move)
                        next_priority = heuristic(next_state)
                        frontier.append(
                            (next_priority, next_state, (priority, current_state, parent_state))
                        )
    

    
    """
