def lz78_compress(data):
    dictionary = {}
    compressed_data = []
    current_string = ""
    dict_size = 1  # Start dictionary indexing from 1
    print("Num Pos\tSubsequence\tNum Represent")
    for i, char in enumerate(data):
        current_string += char
        if current_string not in dictionary:
            # Add the current string to the dictionary
            dictionary[current_string] = dict_size
            previous_index = dictionary.get(current_string[:-1], 0)
            dict_size += 1
            # Record the compressed pair (index of prefix, next character)
            compressed_data.append((previous_index, char))
            # Print the details
            print(f"{dict_size-1}\t\t{current_string}\t\t({previous_index}, '{char}')")
            # Reset current_string for the next sequence
            current_string = ""
    return compressed_data

def lz78_decompress(compressed_data):
    dictionary = {0: ""}  # Initialize dictionary with an empty prefix at index 0
    decompressed_data = []
    dict_size = 1
    for index, char in compressed_data:
        entry = dictionary[index] + char
        decompressed_data.append(entry)
        # Add new entry to the dictionary
        dictionary[dict_size] = entry
        dict_size += 1
    return ''.join(decompressed_data)
# Main program with user input
input_data = input("Enter data (binary or characters): ")
# Compress
compressed = lz78_compress(input_data)
print("\nCompressed:", compressed)
# Decompress
decompressed = lz78_decompress(compressed)
print("Decompressed:", decompressed)
# Verify correctness
if decompressed == input_data:
    print("Decompression successful! The data matches the original input.")
else:
    print("Decompression failed! The data does not match the original input.")
