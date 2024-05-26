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
        empty_tubes = []
        non_empty_tubes = []

        for i in range(self.num_tubes):
            if not self.tubes[i]:
                empty_tubes.append(i)
            else:
                non_empty_tubes.append(i)

        for i in non_empty_tubes:
            for j in empty_tubes:
                moves.append((i, j))  # Move to empty tube

            for j in non_empty_tubes:
                if i != j and len(self.tubes[j]) < self.tube_capacity and self.tubes[j][0] == self.tubes[i][0]:
                    moves.append((i, j))  # Move onto identical color

        return moves

    def is_goal(self):
        return all(len(set(tube)) == 1 for tube in self.tubes if tube)

    def merge_tubes(self):
        for i in range(self.num_tubes):
            for j in range(i + 1, self.num_tubes):
                while self.tubes[j] and len(self.tubes[i]) < self.tube_capacity:
                    self.tubes[i].append(self.tubes[j].pop(0))

    def apply_move(self, move):
        i, j = move
        new_state = deepcopy(self)
        new_state.tubes[j].insert(
            0, new_state.tubes[i].pop(0)
        )  # Pop from the left and insert at the beginning
        return new_state

    def __eq__(self, other):
        return self.tubes == other.tubes

    def __hash__(self):
        return hash(str(self.tubes))

    def __str__(self):
        return "".join(
            f'[{", ".join(str(color) for color in tube)}]\n' for tube in self.tubes
        )
