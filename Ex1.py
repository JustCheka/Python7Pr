"""
Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))
"""



def print_operation_table(op, num_rows, num_columns):
    if (num_rows <= 2):
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                if (i == 1):
                    print(j, end = " ")
                elif (j == 1):
                    print(i, end = " ")
                else:
                    print(op(i, j), end = " ")
            print()

print_operation_table(lambda x, y: x * y, 3, 3)
print()
print_operation_table(lambda x, y: x + y, 4, 4)
print()
print_operation_table(lambda x, y: x - y, 5, 5)
print()
print_operation_table(lambda x, y: x * y, 1, 2)
print()
print_operation_table(lambda x, y: x / y, 4, 4)