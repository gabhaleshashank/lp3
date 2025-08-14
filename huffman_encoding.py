import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define less than operator for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree
def build_huffman_tree(char_freq):
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]

# Function to generate Huffman codes
def generate_codes(root, current_code, codes):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        return

    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

# Huffman Encoding main function
def huffman_encoding(data):
    if not data:
        return "", {}

    # Calculate frequency of each character
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1

    # Build Huffman Tree
    root = build_huffman_tree(freq)

    # Generate Huffman Codes
    codes = {}
    generate_codes(root, "", codes)

    # Encode data
    encoded_data = "".join(codes[char] for char in data)
    return encoded_data, codes

# Example usage
if __name__ == "__main__":
    text = input("Enter text to encode: ")
    encoded_text, huffman_codes = huffman_encoding(text)

    print("\nCharacter Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{repr(char)}: {code}")

    print("\nEncoded Text:", encoded_text)
