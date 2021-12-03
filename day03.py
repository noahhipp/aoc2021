#!/home/hipp/anaconda3/bin/python

import numpy as np
import os

def read_data():
    file = __file__
    dir = os.path.dirname(os.path.abspath(file))
    filename = os.path.join(dir, 'day03.txt')
    # credits to lneugebauer
    with open(filename, "r") as f:
            data = np.array([
                [int(digit) for digit in line] for line in f.read().split()
            ])
    return data

def get_power_consumption(data):
    gamma = (data.sum(axis=0) > data.shape[0] / 2)
    epsilon = np.logical_not(gamma)
    gamma = bin2dec(gamma.astype(int))
    epsilon = bin2dec(epsilon.astype(int))
    return gamma * epsilon

def bin2dec(array):
    string = "".join([str(x) for x in array])
    return (int(string,2))

def get_oxygen_rating(data):
    n_cols = data.shape[2];
    for i in range(n_cols):
        col 
    
    
    
if __name__ == '__main__':
    data = read_data()
    power = get_power_consumption(data)
    print(f'Power consumption: {power}')

