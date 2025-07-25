print("By 22IT460")
rows = int(input("Enter the rows: "))
cols = int(input("Enter the columns: "))
matrix = []
for i in range(rows):
    row = list()
    for j in range(cols):
        temp = int(input())
        row.append(temp)
    matrix.append(row)
transpose_matrix = [[matrix[j][i] for j in range(cols)] for i in range(rows)]
print(f"The transpose matrix of {matrix} is {transpose_matrix}")