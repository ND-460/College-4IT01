print("By 22IT460")
data = [(3, 5), (1, 9), (8, 2), (4, 7)]
flat_list = [item for tup in data for item in tup]
min_val = min(flat_list)
max_val = max(flat_list)
print("Minimum value:", min_val)
print("Maximum value:", max_val)