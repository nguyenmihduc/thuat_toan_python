def partition(nums, start=0, end=None):
    print("partition", nums, start, end)
    if end is None:
        end = len(nums) - 1

    # Initialize right and left pointers
    l, r = start, end - 1

    # Iterate while they're apart
    while r > l:
        print("  ", nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1

        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1

        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    print("  ", nums, l, r)
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end


def quicksort(nums, start=0, end=None):
    print("quicksort", nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot - 1)
        quicksort(nums, pivot + 1, end)

    return nums


# l1 = [1, 5, 6, 2, 0, 11, 3]
# pivot = partition(l1)
# print(l1, pivot)

# print(quicksort(l1))


class Notebook:
    def __init__(self, title, username, likes):
        self.title = title
        self.username = username
        self.likes = likes

    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(
            self.username, self.title, self.likes
        )


nb0 = Notebook("pytorch-basics", "aakashns", 373)
nb1 = Notebook("linear-regression", "siddhant", 532)
nb2 = Notebook("logistic-regression", "vikas", 31)
nb3 = Notebook("feedforward-nn", "sonaksh", 94)
nb4 = Notebook("cifar10-cnn", "biraj", 2)
nb5 = Notebook("cifar10-resnet", "tanya", 29)
nb6 = Notebook("anime-gans", "hemanth", 80)
nb7 = Notebook("python-fundamentals", "vishal", 136)
nb8 = Notebook("python-functions", "aakashns", 74)
nb9 = Notebook("python-numpy", "siddhant", 92)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]


def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return "lesser"
    elif nb1.likes == nb2.likes:
        return "equal"
    elif nb1.likes < nb2.likes:
        return "greater"


def default_compare(x, y):
    if x < y:
        return "less"
    elif x == y:
        return "equal"
    else:
        return "greater"


def merge_sort(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge(
        merge_sort(objs[:mid], compare), merge_sort(objs[mid:], compare), compare
    )


def merge(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == "lesser" or result == "equal":
            merged.append(left[i])
            i += 1

        else:
            merged.append(right[j])
            j += 1

    return merged + left[i:] + right[j:]


# sorted_notebooks = merge_sort(notebooks, compare_likes)
# print(sorted_notebooks)


def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1 + 1, idx2 + 1)
    else:
        option1 = lcs_recursive(seq1, seq2, idx1 + 1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2 + 1)
        return max(option1, option2)


print(lcs_recursive("serendipitous", "precipitation"))
# print(lcs_recursive([1, 3, 5, 6, 7, 2, 5, 2, 3], [6, 2, 4, 7, 1, 5, 6, 2, 3]))


def lcs_memo(seq1, seq2):
    memo = {}

    def recurse(idx1=0, idx2=0):
        key = (idx1, idx2)

        if key in memo:
            return memo[key]
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1 + 1, idx2 + 1)
        else:
            memo[key] = max(recurse(idx1 + 1, idx2), recurse(idx1, idx2 + 1))
        return memo[key]
    return recurse(0, 0)


print(lcs_memo("serendipitous", "precipitation"))
