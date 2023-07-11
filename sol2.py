def calculate_complete_rows(n):
    row = 1  # Current row number
    coins_required = row  # Number of coins required for the current row

    while coins_required <= n:
        n -= coins_required
        row += 1
        coins_required = row

    return row - 1  # Return the number of complete rows

#Driver code
n = 15
result = calculate_complete_rows(n)
print(result)
