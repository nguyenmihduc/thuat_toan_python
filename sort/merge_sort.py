# def merge(nums1, nums2):
#     # List to store the results
#     merged = []

#     # Indices for iteration
#     i, j = 0, 0

#     # Loop over the two lists
#     while i < len(nums1) and j < len(nums2):
#         # Include the smaller element in the result and move to next element
#         if nums1[i] <= nums2[j]:
#             merged.append(nums1[i])
#             i += 1
#         else:
#             merged.append(nums2[j])
#             j += 1

#     # Get the remaining parts
#     nums1_tail = nums1[i:]

#     nums2_tail = nums2[j:]

#     # Return the final merged array
#     return merged + nums1_tail + nums2_tail


# def merge_sort(nums):
#     # Terminating condition (list of 0 or 1 elements)
#     if len(nums) <= 1:
#         return nums

#     # Get the midpoint
#     mid = len(nums) // 2

#     # Split the list into two halves
#     left = nums[:mid]
#     right = nums[mid:]

#     # Solve the problem for each half recursively
#     left_sorted, right_sorted = merge_sort(left), merge_sort(right)
#     print("left_sorted", left_sorted)
#     print("right_sorted", right_sorted)
#     # Combine the results of the two halves
#     sorted_nums = merge(left_sorted, right_sorted)

#     return sorted_nums


# print(merge_sort([38, 27, 43, 3, 9, 82, 10]))


def merge(nums1, nums2, depth=0):
    print("  " * depth, "merge:", nums1, nums2)
    i, j, merged = 0, 0, []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    return merged + nums1[i:] + nums2[j:]


def merge_sort(nums, depth=0):
    print("  " * depth, "merge_sort:", nums)
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2

    return merge(
        merge_sort(nums[:mid], depth + 1), merge_sort(nums[mid:], depth + 1), depth + 1
    )


print(merge_sort([5, -12, 2, 6, 1, 23, 7, 7, -12]))
