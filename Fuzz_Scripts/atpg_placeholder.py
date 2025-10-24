
def seed_holder(source_file, destination_file):
    """Copies the contents of one file to another.

    Args:
        source_file: Path to the source file.
        destination_file: Path to the destination file.
    """
    try:
        with open(source_file, 'r') as infile, open(destination_file, 'w') as outfile:
            for line in infile:
                outfile.write(line)
        print(f"File '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: Source file '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage (replace with your actual file paths)
