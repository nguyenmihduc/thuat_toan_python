def insertion_sort(nums):
    nums = list(nums)
    print("insertion_sort:", nums)

    for i in range(len(nums)):
        print("i:", i)
        cur = nums.pop(i)
        print("cur:", cur)
        print(">>> nums pop:", nums)

        j = i - 1
        print("j:", j)
        print("nums[j]:", nums[j])
        while j >= 0 and nums[j] > cur:
            j -= 1
            print(" j in loop:", j)
        nums.insert(j + 1, cur)
        print(">>> nums insert:", nums)
        print()
    return nums


nums = [4, 2, 6, 3, 4, 6, 2, 1]
nums2 = insertion_sort(nums)

print(nums2)
