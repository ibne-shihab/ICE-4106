def calculate_parity_bits(data_bits):
    p1 = data_bits[0] ^ data_bits[1] ^ data_bits[3]  # Parity bit for positions 1, 3, 5, 7
    p2 = data_bits[0] ^ data_bits[2] ^ data_bits[3]  # Parity bit for positions 2, 3, 6, 7
    p3 = data_bits[1] ^ data_bits[2] ^ data_bits[3]  # Parity bit for positions 4, 5, 6, 7
    return [p1, p2, p3]
def encode_hamming(data_bits):
    # Calculate parity bits
    p1, p2, p3 = calculate_parity_bits(data_bits)
    # Arrange parity and data bits as follows: p1, p2, d1, p3, d2, d3, d4
    # Positions:       1   2   3   4   5   6   7
    codeword = [p1, p2] + [data_bits[0]] + [p3] + data_bits[1:]
    return codeword
# Input 4 data bits to transmit
data_bits = list(map(int, input("Enter 4 data bits separated by spaces: ").split()))
# Encode the data bits into a Hamming codeword
encoded_codeword = encode_hamming(data_bits)
print("Encoded Hamming Codeword to Transmit:", encoded_codeword)
def decode_hamming(received_codeword):
    # Extract bits from the received codeword
    p1, p2, d1, p3, d2, d3, d4 = received_codeword

    # Recalculate parity bits to check for errors
    c1 = p1 ^ d1 ^ d2 ^ d4  # Checks parity for positions 1, 3, 5, 7
    c2 = p2 ^ d1 ^ d3 ^ d4  # Checks parity for positions 2, 3, 6, 7
    c3 = p3 ^ d2 ^ d3 ^ d4  # Checks parity for positions 4, 5, 6, 7

    # Determine error position (0 means no error)
    error_position = (c3 << 2) | (c2 << 1) | c1

    # Correct error if detected
    corrected_codeword = received_codeword.copy()
    if error_position != 0:
        corrected_codeword[error_position - 1] ^= 1  # Flip the erroneous bit

    # Extract original data bits (d1, d2, d3, d4) from the corrected codeword
    corrected_data_bits = [corrected_codeword[2], corrected_codeword[4], corrected_codeword[5], corrected_codeword[6]]
    return corrected_data_bits, error_position

# Simulate receiving bits (with or without errors)
received_codeword = list(map(int, input("Enter received 7-bit codeword separated by spaces: ").split()))
# Decode and correct the received codeword
corrected_data, error_position = decode_hamming(received_codeword)
print("Corrected Data Bits:", corrected_data)
print("Error Position (1-7, 0 means no error):", error_position)

# Display correction result
if error_position == 0:
    print("No error detected in the received codeword.")
else:
    print(f"Error detected and corrected at position {error_position}.")