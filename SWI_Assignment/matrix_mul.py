# input matrix
# matrix_A = [[1, 3, 4], [2, 5, 7], [5, 9, 6]]
#
# matrix_B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# matrix_A = [[1, 2], [3, 4]]
#
# matrix_B = [[1, 2, 3, 4, 5], [5, 6, 7, 8, 9]]

num_matrix = 2


def matrix_input():
    for j in range(num_matrix):
        rows = int(input(f'Enter number of rows for matrix {j + 1} : '))
        final_matrix = []
        for i in range(rows):
            ele_of_rows = input(f'Enter elements of row {i + 1}: ')
            individual_row = [int(i) for i in ele_of_rows.split(' ')]
            final_matrix.append(individual_row)

        return final_matrix


matrix_A = matrix_input()
matrix_B = matrix_input()

print(matrix_A)
print()
print(matrix_B)


num_columns_A = len(matrix_A[0])
num_row_B = len(matrix_B)
matrix_AB = []
print(num_columns_A)
print(num_row_B)
print()


def matrix_mul():
    if num_columns_A != num_row_B:
        return 'Invalid Matrix'
    for row in matrix_A:
        for idx_col, _ in enumerate(range(len(matrix_B[0]))):
            sum_of_rc = 0
            for idx_row, column in enumerate(matrix_B):
                print(f'{column[idx_col]} | {row[idx_row]}\n')
                sum_of_rc += row[idx_row] * column[idx_col]
            print("*******************", sum_of_rc)
            matrix_AB.append(sum_of_rc)
    print("*******************", matrix_AB)

    return matrix_AB


print('Matrix Multiplication is: ', matrix_mul())
