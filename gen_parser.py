def line_parser(file):
    file = open(file, "r")
    lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')

    file.close()
    return lines


def dual_line_parser(file):
    file = open(file, "r")
    lines = file.readlines()
    parsed_lines = []

    for i in range(0, len(lines), 2):
        parsed_lines.append(lines[i].strip('\n') + ', ' + lines[i + 1].strip('\n'))

    file.close()
    return parsed_lines
