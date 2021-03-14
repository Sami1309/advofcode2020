filepath = "input.in"
lines = []
with open(filepath) as fp:
    line = fp.readline().split('\n')[0]
    while line:
        lines.append(line)
        line = fp.readline().split('\n')[0]


def algo(mut):

    slope = 0
    hit = 0
    for line in lines:
        if (slope*mut + 0.0).is_integer() and line[(int(slope*mut))%len(line)] == "#":
            hit += 1
        slope += 1
    return hit



def run():
    return algo(1) * algo(3) * algo(5) * algo(7) * algo(0.5)

print(run())