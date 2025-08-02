import numpy as np
def create_matrix(mc):
    print("\nARRAY " + str(mc) + " Elements:")
    array_1 = map(int, input().split())
    array_1 = np.array(list(array_1))  
    print("\nARRAY " + str(mc) + " ROW and COLUMN:")
    row, column = map(int, input().split()) 
    if len(array_1) != (row * column):
        print("\nRow and Column size does not match total elements! Retry.")
        return create_matrix(mc)
    array_1 = array_1.reshape(row, column)
    print("\nARRAY " + str(mc) + ":")
    print(array_1)
    
    print("\nTrace:")
    return array_1
matrix = create_matrix(1)
print(matrix.trace())
