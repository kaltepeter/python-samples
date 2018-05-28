#!/usr/bin/env python3

import random


def get_new_color(n_rows, n_cols):
    grid_size = n_rows * n_cols
    threshold_h = 255 - grid_size
    new_r = random.randint(grid_size, threshold_h)
    new_g = random.randint(grid_size, threshold_h)
    new_b = random.randint(grid_size, threshold_h)
    print("new_color:", new_r, new_g, new_b)

    return [new_r, new_g, new_b]


def main():
    initial_color = [0, 0, 0]

    matrix = [initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color,
              initial_color, initial_color]

    increment = 8
    n_rows = increment
    n_cols = increment

    color = get_new_color(n_rows, n_cols)

    multiplier = 0

    for col in range(len(matrix)):

        if multiplier > 8:
            multiplier = 0

        new_r = color[0]
        new_g = color[1]
        new_b = color[2]

        new_color = [(new_r + (increment * multiplier)),
                     (new_g + (increment * multiplier)),
                     (new_b + (increment * multiplier))
                     ]

        matrix[col] = new_color
        multiplier += 1

    for row in matrix:
        print(row)


main()
