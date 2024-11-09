def lz78_compress(data):
    dictionary = {}
    compressed_data = []
    current_string = ""
    dict_size = 1  # Start dictionary indexing from 1
    print("Subsequences and Dictionary Entries:")

    for char in data:
        current_string += char
        if current_string not in dictionary:
            # Add the current string to the dictionary
            dictionary[current_string] = dict_size
            dict_size += 1

            # Output a tuple (index of previous string, new character)
            if len(current_string) == 1:
                compressed_data.append((0, current_string))
                print(f"Added '{current_string}' as (0, '{current_string}')")
            else:
                compressed_data.append((dictionary[current_string[:-1]], current_string[-1]))
                print(f"Added '{current_string}' as ({dictionary[current_string[:-1]]}, '{current_string[-1]}')")

            # Reset current_string for the next sequence
            current_string = ""

    # If there's any leftover in current_string, add it
    if current_string:
        compressed_data.append((dictionary[current_string[:-1]], current_string[-1]))
        print(f"Added leftover '{current_string}' as ({dictionary[current_string[:-1]]}, '{current_string[-1]}')")

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