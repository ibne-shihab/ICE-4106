import math
# Example graph with edge weights
graph = {
    'A': {'B': 1, 'C': 2, 'D': 1},
    'B': {'A': 1, 'C': 1},
    'C': {'A': 2, 'B': 1, 'D': 1},
    'D': {'A': 1, 'C': 1}
}
def calculate_transition_probabilities(graph):
    transitions = {}
    for node, edges in graph.items():
        total_weight = sum(edges.values())  # Sum of edge weights for this node
        # For each neighbor, calculate the transition probability
        transitions[node] = {neighbor: weight / total_weight for neighbor, weight in edges.items()}
    return transitions
def entropy_rate(transitions):
    entropy = 0
    # Sum the entropy of the transition probabilities for each node
    for node, edges in transitions.items():
        for prob in edges.values():
            if prob > 0:
                # Add -P * log2(P) for each transition probability
                entropy += -prob * math.log2(prob)
    # Average entropy over all nodes
    return entropy / len(transitions)
# Example usage
transitions = calculate_transition_probabilities(graph)
rate = entropy_rate(transitions)
# Print the transition probabilities for each node
print("Transition Probabilities:")
for node, edges in transitions.items():
    print(f"{node}: {edges}")
# Print the entropy rate of the random walk
print("Entropy Rate of Random Walk:", rate)