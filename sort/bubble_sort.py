nums0 = [4, 2, 6, 3, 4, 6, 2, 1]
# nums0 = [4, 2, 6, 3, 1]
nums1 = [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
nums2 = [3, 5, 6, 8, 9, 10, 99]
nums3 = [99, 10, 9, 8, 6, 5, 3]
nums4 = [42, 42, 42, 42, 42, 42, 42]


def bubble_sort(nums):
    # print(1)
    # print(">>> nums:", nums)
    # Create a copy of the list, to avoid changing it
    nums = list(nums)
    # print(2)
    # print(">>> nums:", nums)

    # 4. Repeat the process n-1 times
    for _ in range(len(nums) - 1):
        # print(3)
        # print(">>> nums:", nums)
        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):
            # print(4)
            # print(">>> nums:", nums)
            # 2. Compare the number with
            if nums[i] > nums[i + 1]:
                # print(5)
                # print(">>> nums:", nums)
                # print(">>> nums[i]:", nums[i])
                # 3. Swap the two elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        #         print(6)
        #         print(">>> nums:", nums)
        #     print("================================================================")
        # print("--------------------------------")
    # Return the sorted list
    # print(7)
    return nums


result0 = bubble_sort(nums4)
print(result0)
