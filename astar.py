from collections import deque

def astar(initial_state):
    """
    A* search algorithm for the Liquid Puzzle game.
    Returns the path to the solution if one exists, None otherwise.
    """
    frontier = deque([(heuristic(initial_state), initial_state, None)])
    explored = set()

    while frontier:
        priority, current_state, parent_state = frontier.popleft()

        if current_state.is_goal():
            path = [current_state]
            while parent_state:
                path.append(parent_state[1])
                parent_state = parent_state[2]
            return path[::-1]

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


def heuristic(state):
    """
    Heuristic function to estimate the cost of reaching the goal state
    from the current state.
    """
    cost = 0
    colors = {}
    for tube in state.tubes:
        for color in tube:
            if color not in colors:
                colors[color] = 0
            colors[color] += 1

    for count in colors.values():
        cost += count - 1

    return cost



