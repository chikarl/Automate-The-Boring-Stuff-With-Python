spam = []


def commaCode(array):
    arrayLen = len(array)
    if arrayLen == 0:
        print("Array is empty")
    else:
        for i in range(arrayLen-1):
            print(array[i], end=', ')
        print(f"and {array[arrayLen-1]}")


commaCode(spam)
