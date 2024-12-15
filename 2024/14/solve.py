
import numpy as np
def calc_pos(x, y, xvel, yvel, xbound, ybound,  steps):
    return [(x + xvel * steps) % xbound, (y + yvel * steps) % ybound]

with open('input.txt') as inp:
    data = inp.read()

matrix = np.zeros((103, 101), int)

for line in data.splitlines():
    parts = line.split(" ")
    pos = [int(i) for i in parts[0].split("=")[1].split(",")][::-1] #reverse order to put y value (row) first
    vel = [int(i) for i in parts[1].split("=")[1].split(",")][::-1]
    proj = calc_pos(pos[0], pos[1], vel[0], vel[1], 103, 101, 100)
    matrix[proj[0]][proj[1]] += 1

top_left = matrix[:51, :50].copy()
top_left_total = np.sum(top_left)

top_right = matrix[:51, 51:].copy()
top_right_total = np.sum(top_right)

bottom_left = matrix[52:, :50].copy()
bottom_left_total = np.sum(bottom_left)

bottom_right = matrix[52:, 51:].copy()
bottom_right_total = np.sum(bottom_right)

print(top_left_total * top_right_total * bottom_left_total * bottom_right_total)

### Part 2

import matplotlib.pyplot as plt

def display_matrix(matrix):
    plt.clf()
    plt.imshow(matrix, cmap='gray')
    plt.axis('off')

plt.ion()

for state in range(93, 9301, 101): #Upon looking through these 1 by 1, a vague vertical pattern appears starting at 93, then once every 101 iterations afterwards 
    matrix = np.zeros((103, 101), int)
    for line in data.splitlines():
        parts = line.split(" ")
        pos = [int(i) for i in parts[0].split("=")[1].split(",")][::-1]
        vel = [int(i) for i in parts[1].split("=")[1].split(",")][::-1]
        proj = calc_pos(pos[0], pos[1], vel[0], vel[1], 103, 101, state)
        matrix[proj[0]][proj[1]] += 1
    matrix[matrix != 0] = 1
    display_matrix(matrix)
    input(state)

plt.ioff()

"""Alternative (perhaps better) automatic solution using noise calculation

from scipy.signal import convolve2d
from tqdm import trange
import math

#https://stackoverflow.com/a/25436112
def estimate_noise(I):

    H, W = I.shape

    M = [[1, -2, 1],
         [-2, 4, -2],
         [1, -2, 1]]

    sigma = np.sum(np.sum(np.absolute(convolve2d(I, M))))
    sigma = sigma * math.sqrt(0.5 * math.pi) / (6 * (W-2) * (H-2))

    return sigma

noises = []
for state in trange(10000):
    matrix = np.zeros((103, 101), int)
    for line in data.splitlines():
        parts = line.split(" ")
        pos = [int(i) for i in parts[0].split("=")[1].split(",")][::-1] #reverse order to put y value (row) first
        vel = [int(i) for i in parts[1].split("=")[1].split(",")][::-1]
        proj = calc_pos(pos[0], pos[1], vel[0], vel[1], 103, 101, state)
        matrix[proj[0]][proj[1]] += 1
    matrix[matrix != 0] = 1
    noises.append(estimate_noise(matrix))

print(noises.index(min(noises)))
"""
