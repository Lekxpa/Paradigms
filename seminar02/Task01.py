# Контекст
# След матрицы - это сумма чисел на её главной диагонали. 
# След определён только для квадратных матриц 
# (количество столбцов = количеству строк).
# ● Задача
# Реализовать чисто структурную реализацию вычисления следа для любой матрицы NxN.

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

n = len(my_matrix)

if not all(isinstance(i, list) for i in my_matrix) or n != len(my_matrix[0]):
    raise ValueError('Fail to get trail sum! Matrix is not square!')

trail_sum = 0

for i in range(n):
    trail_sum += my_matrix[i][i]

print(trail_sum)




init_matrix =   [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
d_sum = 0
size = len(init_matrix)

for diag in range(size):
    d_sum += init_matrix[diag][diag]
print(d_sum)

# процедурный

def func(init_matrix):

    d_sum = 0
    size = len(init_matrix)

    for diag in range(size):
        d_sum += init_matrix[diag][diag]
    
    return d_sum

init_matrix =   [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]