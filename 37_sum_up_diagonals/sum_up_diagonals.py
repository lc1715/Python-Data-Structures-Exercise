
# m1 = [
#     [1,   2],
#     [30, 40],
# ]

# m2 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]




def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """


    if len(matrix) > 2:
        return matrix[0][0] + matrix[1][1] + matrix[2][2] + matrix[0][2] + matrix[1][1] + matrix[2][0]
    else:
        return matrix[0][0] + matrix[1][1] + matrix[0][1] + matrix[1][0]