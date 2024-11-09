import heapq
import numpy as np
import math
# Step 1: Define a class to create nodes for the Huffman tree
class HuffmanNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol     # Symbol (like 'A', 'B', etc.)
        self.freq = freq         # Frequency (or probability) of the symbol
        self.left = None         # Left child
        self.right = None        # Right child
    # This method is required by heapq to compare nodes based on frequency
    def __lt__(self, other):
        return self.freq < other.freq
# Step 2: Build the Huffman tree
def build_huffman_tree(symbols):
    # Initialize a heap with nodes for each symbol
    heap = [HuffmanNode(symbol, freq) for symbol, freq in symbols]
    heapq.heapify(heap)  # Create a min-heap based on frequencies
    # Combine nodes until only one tree remains
    while len(heap) > 1:
        # Remove the two nodes with the smallest frequencies
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        # Create a new node with the combined frequency
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left    # Set left and right children
        merged.right = right
        # Add the merged node back into the heap
        heapq.heappush(heap, merged)
    # The remaining node is the root of the Huffman tree
    return heap[0]

# Step 3: Generate Huffman codes by traversing the tree
def generate_huffman_codes(node, prefix="", codebook={}):
    # If the node is a leaf (has a symbol), add it to the codebook
    if node.symbol is not None:
        codebook[node.symbol] = prefix
    else:
        # Traverse left and right, adding '0' for left and '1' for right
        generate_huffman_codes(node.left, prefix + "1", codebook)
        generate_huffman_codes(node.right, prefix + "0", codebook)
    return codebook
# Example usage
symbols = [("F", 0.27),("E", 0.23),("D", 0.2),("C", 0.15),("B", 0.1),  ("A", 0.05) ]
root = build_huffman_tree(symbols)
huffman_codes = generate_huffman_codes(root)

# Display Huffman codes for each symbol
print("Huffman Codes for each symbol:")
for symbol, code in huffman_codes.items():
    print(f"{symbol}: {code}")
def calculate_entropy(symbols):
    return -sum(freq * math.log2(freq) for _, freq in symbols if freq > 0)
entropy = calculate_entropy(symbols)
avg_length = sum(freq * len(huffman_codes[symbol]) for symbol, freq in symbols)

print(f"\nEntropy: {entropy:.4f}")
print(f"Average Huffman Code Length: {avg_length:.4f}")
tolerance = 0.1  # Allow a small tolerance for practical overhead
print("Huffman Code is Optimal:", avg_length <= entropy + tolerance)