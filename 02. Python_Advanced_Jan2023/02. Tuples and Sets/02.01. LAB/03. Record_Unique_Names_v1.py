list_names = [input() for x in range(int(input()))]
[print(x) for x in set(list_names)]

# ###########
# Input_1:
# 8
# Lee
# Joey
# Lee
# Joe
# Alan
# Alan
# Peter
# Joey
# -----------
# Output_1:
# Alan
# Joey
# Lee
# Joe
# Peter
# ###########
# Input_2:
# 7
# Lyle
# Bruce
# Alice
# Easton
# Shawn
# Alice
# Shawn
# -----------
# Output_2:
# Easton
# Lyle
# Alice
# Bruce
# Shawn
# ###########
# Input_3:
# 6
# Adam
# Adam
# Adam
# Adam
# Adam
# Adam
# -----------
# Output_3:
# Adam
# ###########
