def sort(my_array):
    if len(my_array) <= 1:
        return my_array
    middle = len(my_array) // 2
    left = sort(my_array[:middle])
    right = sort(my_array[middle:])


    return merge(left, right)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result

array = [ 4, 2, 6, 5, 7, 1]
sorted_array = sort(array)
print(sorted_array)