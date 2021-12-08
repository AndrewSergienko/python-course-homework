def get_data(path, line="all"):
    with open(path, 'r') as file:
        if line.isdigit():
            try:
                return file.readline(int(line))
            except EOFError:
                return
        elif line == "all":
            return file.read()
        elif line == "endline":
            length = sum(1 for _ in file)
            return file.read(length)


def set_data(path, mode, content):
    with open(path, mode) as file:
        file.write(content)
