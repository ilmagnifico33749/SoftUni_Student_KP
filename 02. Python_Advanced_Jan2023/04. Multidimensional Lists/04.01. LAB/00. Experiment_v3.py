number_rows_columns = int(input())

# matrix = [[int(ord(x)) for x in input()] for rows in range(number_rows_columns)]

matrix = [[x for x in input()] for rows in range(number_rows_columns)]

print(matrix)

symbol_to_find = input()
print(symbol_to_find)

for rows in range(number_rows_columns):
    print(f"Row: {rows}")
    for indexes in range(len(matrix[rows])):
        print(f"Index: {indexes}")
        current_symbol = matrix[rows][indexes]
        print(current_symbol)
        if current_symbol == symbol_to_find:
            print(f"({rows}, {indexes})")
            break


    #
    # if symbol_to_find in matrix:
    #     print(f"YES!")
    # else:
    #     print(f"NO!")

# ##############################
# Input_1:
# 3
# ABC
# DEF
# X!@
# !
# ------------------------------
# Output_1:
# (2, 1)
# ##############################
# Input_2:
# 4
# asdd
# xczc
# qwee
# qefw
# 4
# ------------------------------
# Output_2:
# 4 does not occur in the matrix
# ##############################