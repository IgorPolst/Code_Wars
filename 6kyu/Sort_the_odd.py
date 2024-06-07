# Task
# You will be given an array of numbers. 
# You have to sort the odd numbers in ascending order while 
# leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


def sort_array(source_array):
    new_source =[]
    indexes = []
    for i in range(len(source_array)):
        if source_array[i]%2 == 1:
            new_source.append(source_array[i])
            indexes.append(i)
    print (new_source, indexes) 
    new_source.sort()
    data = list(zip(new_source, indexes))
    for i in data: 
        source_array[i[1]] = i[0]
    return source_array

print (sort_array([5, 3, 2, 8, 1, 4]))

