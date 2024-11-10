# Define generator polynomials (rate 1/2 code)
G1 = [1, 1, 1]  # Polynomial: 111
G2 = [1, 0, 1]  # Polynomial: 101
# Encoding function
def encode_data(data):
    state = [0, 0, 0]  # Initialize shift register state with three bits
    encoded_data = []
    for bit in data:
        # Shift the register and add the new bit at the start
        state = [bit] + state[:-1]

        # Calculate output bits by XORing the state with the generator polynomials
        out1 = state[0] ^ state[1] ^ state[2]  # XOR for G1
        out2 = state[0] ^ state[2]             # XOR for G2

        # Append the output bits to the encoded data
        encoded_data.append(out1)
        encoded_data.append(out2)
    return encoded_data
# Main program
input_data = list(map(int, input("Enter binary data (e.g., 1011): ")))
# Encode the data
encoded_data = encode_data(input_data)
print("Encoded Data:", encoded_data)