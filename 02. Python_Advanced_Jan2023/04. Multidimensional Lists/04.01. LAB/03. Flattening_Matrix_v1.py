matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]

flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)

# #########################################
# Input_1:
# 2
# 1, 2, 3
# 4, 5, 6
# -----------------------------------------
# Output_1:
# [1, 2, 3, 4, 5, 6]
# #########################################
# Input_2:
# 3
# 10, 2, 21, 4
# 5, 20, 41, 9
# 6, 2, 4, 99
# -----------------------------------------
# Output_2:
# [10, 2, 21, 4, 5, 20, 41, 9, 6, 2, 4, 99]
# #########################################
