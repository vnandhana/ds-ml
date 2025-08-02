import numpy as np
def create_matrix(mc):
    print("\n ARRAY" + str(mc) + " Elements")
    array_1 = map(int, input().split())
    array_1 = np.array(list(array_1))

    print("\n ARRAY" + str(mc) + ", ROW COLUMN:")
    row, column = map(int, input().split())
    if len(array_1) != (row * column):
        print("\n Row and Column not match with total element!! retry")
        return create_matrix(mc)
    array_1 = array_1.reshape(row, column)
    print("\n ARRAY" + str(mc))
    print(array_1)
    return array_1

arr1 = create_matrix(1)
arr2 = create_matrix(2)
if arr1.shape == arr2.shape:
    print("\n Dot product")
    print(np.dot(arr1, arr2))
else:
    print("\n Dimensions are not matching!")


