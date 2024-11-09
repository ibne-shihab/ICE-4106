import numpy as np

# Joint probability matrix as shown in the image
matrix = np.array([
    [1/8, 1/16, 1/32, 1/32],
    [1/16, 1/8, 1/32, 1/32],
    [1/16, 1/16, 1/16, 1/16],
    [1/4, 0, 0, 0]
])
# Normalize the matrix to ensure the total sum is 1
matrix = matrix / np.sum(matrix)
# Marginal distribution of X and Y
px = np.sum(matrix, axis=0)  # Sum across rows for P(X)
py = np.sum(matrix, axis=1)  # Sum across columns for P(Y)
print("The Marginal distribution of X is",px)
print("The Marginal distribution of Y is",py)
def entropy(p):
    return -np.sum(p * np.log2(p, where=(p > 0)))
def joint_entropy(matrix):
    return -np.sum(matrix * np.log2(matrix, where=(matrix > 0)))
def conditional_entropy_X_given_Y(matrix, py):
    conditional_entropy_value = 0
    for j in range(len(py)):
        if py[j] > 0:
            # Calculate conditional distribution P(X|Y=j)
            px_given_y = matrix[:, j] / py[j]
            # Weight by P(Y=j) and add entropy for this distribution
            conditional_entropy_value += py[j] * entropy(px_given_y)
    return conditional_entropy_value
def conditional_entropy_Y_given_X(matrix, px):
    conditional_entropy_value = 0
    for i in range(len(px)):
        if px[i] > 0:
            # Calculate conditional distribution P(Y|X=i)
            py_given_x = matrix[:, i] / px[i]
            # Weight by P(X=i) and add entropy for this distribution
            conditional_entropy_value += px[i] * entropy(py_given_x)
    return conditional_entropy_value
def mutual_information(matrix, px, py):
    px_py = np.outer(py, px)  # Outer product for P(X) * P(Y)
    # Ensure no division by zero in log2 computation
    return np.sum(matrix * np.log2(matrix / px_py, where=(matrix > 0) & (px_py > 0)))
# Calculate Entropies
H_x = entropy(px)  # Entropy of X
H_y = entropy(py)  # Entropy of Y
H_xy = joint_entropy(matrix)  # Joint Entropy H(X, Y)
H_x_given_y = conditional_entropy_X_given_Y(matrix, py)  # Conditional Entropy H(X|Y)
H_y_given_x = conditional_entropy_Y_given_X(matrix, px)  # Conditional Entropy H(Y|X)
I_xy = mutual_information(matrix, px, py)  # Mutual Information I(X; Y)

# Print results
print("Entropy of X:", H_x)
print("Entropy of Y:", H_y)
print("Joint Entropy H(X, Y):", H_xy)
print("Conditional Entropy H(X|Y):", H_x_given_y)
print("Conditional Entropy H(Y|X):", H_y_given_x)
print("Mutual Information I(X; Y):", I_xy)
