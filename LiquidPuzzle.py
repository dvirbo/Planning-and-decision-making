from copy import deepcopy

class LiquidPuzzleState:
    def __init__(self, tubes):
        self.tubes = tubes
        self.num_tubes = len(tubes)
        self.tube_capacity = max(len(tube) for tube in tubes)

    def is_goal(self):
        for tube in self.tubes:
            if len(tube) > 0 and len(set(tube)) > 1:
                return False
        return True

    def get_valid_moves(self):
        moves = []
        for i in range(self.num_tubes):
            if not self.tubes[i]:
                continue
            for j in range(self.num_tubes):
                if i != j:
                    if not self.tubes[j]:
                        moves.append((i, j))  # Move to empty tube
                    elif len(self.tubes[j]) < self.tube_capacity and self.tubes[j][0] == self.tubes[i][0]:
                        moves.append((i, j))  # Move onto identical color

        # Check for merging tubes with identical colors
        color_counts = {}
        for tube in self.tubes:
            color = tube[0] if tube else None
            if color is not None:
                if color in color_counts:
                    color_counts[color] += len(tube)
                else:
                    color_counts[color] = len(tube)

        for color, count in color_counts.items():
            if count > self.tube_capacity:
                source_tubes = [i for i, tube in enumerate(self.tubes) if tube and tube[0] == color]
                for i in source_tubes[:-1]:
                    for j in source_tubes[1:]:
                        moves.append((i, j))

        return moves


    def is_goal(self):
        colors = {}
        for tube in self.tubes:
            if len(set(tube)) > 1:
                return False
            color = tube[0] if tube else None
            if color is not None:
                if color in colors:
                    colors[color] += len(tube)
                else:
                    colors[color] = len(tube)

        for count in colors.values():
            if count < self.tube_capacity:
                return False

        return True
    

    def merge_tubes(self):
        for i in range(self.num_tubes):
            for j in range(i + 1, self.num_tubes):
                while self.tubes[j] and len(self.tubes[i]) < self.tube_capacity:
                    self.tubes[i].append(self.tubes[j].pop(0))




    def apply_move(self, move):
        i, j = move
        new_state = deepcopy(self)
        new_state.tubes[j].insert(0, new_state.tubes[i].pop(0))  # Pop from the left and insert at the beginning
        return new_state
    



    def __eq__(self, other):
        return self.tubes == other.tubes

    def __hash__(self):
        return hash(str(self.tubes))

    def __str__(self):
        return ''.join(f'[{", ".join(str(color) for color in tube)}]\n' for tube in self.tubes)
    
    
    
    