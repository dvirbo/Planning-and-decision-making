class LiquidPuzzleState:
    def __init__(self, tubes):
        self.tubes = tubes
        self.num_tubes = len(tubes)
        self.tube_capacity = max(len(tube) for tube in tubes)

    def merge_tubes(self):
        for i in range(self.num_tubes):
            for j in range(i + 1, self.num_tubes):
                while self.tubes[j] and len(self.tubes[i]) < self.tube_capacity:
                    self.tubes[i].append(self.tubes[j].pop(0))

# Example usage:
tubes = [[3, 3, 3], [1, 1], [1], [2, 2, 2]]
puzzle = LiquidPuzzleState(tubes)
puzzle.merge_tubes()
print(puzzle.tubes)
