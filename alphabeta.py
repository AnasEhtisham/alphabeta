import time

class MinimaxWithAlphaBeta:
    def __init__(self):
        self.nodes_visited = 0  # To count the number of nodes visited

    def minimax(self, depth, node_index, maximizing_player, values, alpha, beta):
        self.nodes_visited += 1  # Increment the count of nodes visited

        # Terminating condition (leaf node is reached)
        if depth == 3:
            return values[node_index]

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(2):  # Two possible children
                eval = self.minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cut-off
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(2):  # Two possible children
                eval = self.minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cut-off
            return min_eval

# Sample input values for a game tree of height 3 (depth 0 to 3)
values = [3, 5, 6, 9, 1, 2, 0, -1]

minimax_ab = MinimaxWithAlphaBeta()

start_time = time.time()

# Start the Minimax algorithm with Alpha-Beta pruning
optimal_value = minimax_ab.minimax(0, 0, True, values, float('-inf'), float('inf'))

end_time = time.time()

print(f"Optimal Value: {optimal_value}")
print(f"Time taken: {end_time - start_time:.6f} seconds")
print(f"Number of nodes visited: {minimax_ab.nodes_visited}")
