import math
def channel_capacity(matrix):
    # Extract the error probability `p` from the matrix
    p = matrix[0][1]  # `p` is the off-diagonal element in the first row
    if p == 0 or p == 1:
        return 0  # Capacity is zero when there's no uncertainty
    return 1 + p * math.log2(p) + (1 - p) * math.log2(1 - p)
def conditional_entropy(matrix):
    p = matrix[0][1]
    if p == 0 or p == 1:
        return 0  # No entropy when probability is 0 or 1
    return - (p * math.log2(p) + (1 - p) * math.log2(1 - p))
def get_probability_input(prompt):
    while True:
        try:
            value = eval(input(prompt))
            if 0 <= value <= 1:
                return value
            else:
                print("Please enter a number between 0 and 1.")
        except (ValueError, SyntaxError, NameError):
            print("Invalid input. Please enter a valid number or fraction (e.g., 0.5 or 2/3).")
print("Enter the values for the binary symmetric channel noise matrix P(Y|X)")

One_one = get_probability_input("Enter P(Y=0|X=0): ")
One_two = get_probability_input("Enter P(Y=0|X=1): ")
two_one = get_probability_input("Enter P(Y=1|X=0): ")
two_two = get_probability_input("Enter P(Y=1|X=1): ")
matrix = [
    [One_one, One_two],
    [two_one, two_two]
]
print("The Matrix is:", matrix)

# Calculate and display Channel Capacity
capacity = channel_capacity(matrix)
print("Channel Capacity C:", capacity)

# Calculate and display Conditional Entropy
cond_entropy = conditional_entropy(matrix)
print("Conditional Entropy H(Y|X):", cond_entropy)