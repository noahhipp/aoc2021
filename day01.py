import numpy as np

# get data
data = np.genfromtxt("day01.txt")

# part one
result = sum(np.diff(data) > 0)
print(result)

# part two
windows = data[:-2] + data[1:-1] + data[2:]
result = sum(np.diff(windows) > 0)
print(result)
