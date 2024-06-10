array_0 = [1, 7, 4, 2, 1, 3, 11, 5]
target = 10
output = 2, 6


def sub_array_sum(array, target):
    n = len(array)
    for i in range(0, n):
        for j in range(i, n):
            if sum(array[i:j]) == target:
                return i, j
    return None, None


num1, num2 = sub_array_sum(array_0, target)
print(num1, num2)
print(array_0[num1:num2])
