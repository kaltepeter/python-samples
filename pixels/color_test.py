#!/usr/bin/env python3
# from sense_hat import SenseHat

# sense = SenseHat()

# 248 is highest num evenly divided
matrix = [[0, num, 0] for num in range(50, 255)]
matrix = matrix[:205]

# sense.set_pixels(matrix)

print(len(matrix))
for col in matrix:
    # print(col)
