filepath = 'input.txt'
lines = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        lines.append(int(line))
        line = fp.readline()
print(len(lines))

##lines is a list containing every individual input

