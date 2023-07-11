def convert_to_2d_array(original, m, n):
    if m * n != len(original):
        return []  # Return an empty 2D array if it is impossible

    result = [[0] * n for _ in range(m)]
    for i in range(len(original)):
        row = i // n
        col = i % n
        result[row][col] = original[i]

    return result
#Driver code
original = [1, 2, 3, 4, 5, 6]
m = 2
n = 3

result = convert_to_2d_array(original, m, n)
print(result)
