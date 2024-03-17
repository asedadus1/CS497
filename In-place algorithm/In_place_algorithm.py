import numpy as np

#grid passed the matrix argument
#g = gama value
#i = row length
#m = col length
#theta = change in value from the old matrix value to new matrix value
def dp_matrix(grid, g ,i, m, theta):
    while(True):
        max_change = 0
        for r in range(i):
            for c in range(m):
                if (r, c) in [(0, 0), (i - 1, m - 1)]:
                    continue
                up = grid[max(r - 1, 0), c]
                down = grid[min(r + 1, i - 1), c]
                left = grid[r, max(c - 1, 0)]
                right = grid[r, min(c + 1, m - 1)]
                new_value = (-1+(g*up)) + (-1+(g*down)) + (-1+(g*right)) + (-1+(g*left))  
                new_value = round(new_value / 4, 4)                 
        
                # Calculate change in value
                change = abs(grid[r][c] - new_value)
                if change > max_change:
                    max_change = change

                # Update grid value
                grid[r][c] = new_value
        if max_change < theta:
                break


def main():
    matrix = np.array([
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0]
    ])
  
    gama = 1
    row , col = matrix.shape
    theta = 0.00001
    dp_matrix(matrix, gama, row, col, theta)
    print(matrix)


if __name__ == "__main__":
    main()
