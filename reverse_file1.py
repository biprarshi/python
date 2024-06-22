def reverse_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    with open(output_file, 'w') as f:
        for line in reversed(lines):
            f.write(line)

if __name__ == "__main__":
    input_filename = input("Enter the input file name: ")
    output_filename = input("Enter the output file name: ")
    reverse_file(input_filename, output_filename)
    print("File reversed successfully!")