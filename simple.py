def bubble_sort(array):
    n = len(array)
    
    for i in range(n):
        set_flag = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # array[j], array[j + 1] = array[j + 1], array[j]
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                
                set_flag = False
                
        if set_flag:
            break
    
    return array


if __name__ == '__main__':    
    A = [3, 6, 1, 5, 8, 2, 11, 7]
    bubble_sort(A)

print("hello world")
