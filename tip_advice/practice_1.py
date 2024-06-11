array_0 = [1, 7, 4, 2, 1, 3, 11, 5]
target = 10
output = 2, 6


def sub_array_sum(array, target):
    n = len(array)
    for i in range(0, n):
        for j in range(i, n + 1):
            if sum(array[i:j]) == target:
                return i, j
    return None, None


# num1, num2 = sub_array_sum(array_0, 16)
# print(num1, num2)
# print(array_0[num1:num2])


def sub_array_sum_2(array, target):
    n = len(array)
    for i in range(0, n):
        s = 0
        for j in range(i, n + 1):
            if s == target:
                return i, j
            elif s > target:
                break
            if j < n:
                s += array[j]
    return None, None

# num1, num2 = sub_array_sum_2(array_0, 55)
# print(num1, num2)
# print(array_0[num1:num2])

def sub_array_sum_3(array, target):
    n = len(array)
    i, j,  s = 0, 0, 0
    while i < n and j < n + 1:
        if s == target:
            return i, j
        elif s < target:
            if j < n :
                s += array[j]
            j += 1
        elif s > target:
            s -= array[i]
            i += 1
    return None, None

num1, num2 = sub_array_sum_3(array_0, 10)
print(num1, num2)
print(array_0[num1:num2])