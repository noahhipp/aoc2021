import pandas as pd

# get data
data = pd.read_csv('day02.txt', sep=' ', names=('direction','amount'))

# part one
hp = sum(data.amount[data.direction == 'forward']) 
depth = sum(data.amount[data.direction == 'down']) - sum(data.amount[data.direction == 'up'])

print(hp*depth)

# part two
aim = 0
depth = 0
hp = 0
for idx,row in data.iterrows():
    if row.direction == 'forward':
        hp = hp + row.amount
        depth += aim * row.amount
    elif row.direction == 'down':
        aim += row.amount
    elif row.direction == 'up':
        aim -= row.amount

print(depth * hp)

