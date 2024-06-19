# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.


def binary_array_to_number(arr):
    arr = arr[::-1]
    count = 0
    for i in range(len(arr)):
        count += arr[i] * 2**i
    return count


print(binary_array_to_number([0, 0, 0, 1]), 1)
print(binary_array_to_number([0, 0, 1, 0]), 2)
print(binary_array_to_number([1, 1, 1, 1]), 15)
print(binary_array_to_number([0, 1, 1, 0]), 6)
