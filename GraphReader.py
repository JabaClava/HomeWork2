#enter input graph
def GraphReader(file):
    return list(map(lambda x: [int(x[0]), list(map(int, x[1:]))], list(map(lambda x: x.split(), open(file).readlines()))))
