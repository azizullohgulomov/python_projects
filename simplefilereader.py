def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

file_path = 'example.txt'
print(read_file(file_path))