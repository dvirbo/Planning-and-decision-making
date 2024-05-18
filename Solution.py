class Solution:
    def __init__(self):
        self.num_new_states = 0
        self.route = []

    def add_move(self, move):
        self.route.append(move)

    def increment_states(self):
        self.num_new_states += 1

    def __str__(self):
        return f"Number of new states: {self.num_new_states}\nRoute: {self.route}"
