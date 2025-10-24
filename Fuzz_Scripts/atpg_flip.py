def bit_flip_sequence(input_file, output_file):
    """Reads a sequence from a file, bit flips it, and writes to another file."""
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                flipped_line = ''.join(['1' if bit == '0' else '0' if bit == '1' else bit for bit in line.strip()])
                outfile.write(flipped_line + '\n')
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")

# Example usage (replace with your actual file names):

