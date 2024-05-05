# cards = [14, 13, 13, 13, 13, 12, 6, 5, 3, 1]
# cards = [14, 13, 12, 6, 5, 3, 1]
cards = list(range(10, 0, -1))


def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return "left"
        else:
            return "found"
    elif cards[mid] < query:
        return "left"
    else:
        return "right"


def locate_card_1(cards, query):
    lo, hi = 0, len(cards)

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]

        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1

        # result = test_location(cards, query, mid)
        # if result == "found":
        #     return mid
        # elif result == "left":
        #     hi = mid - 1
        # elif result == "right":
        #     lo = mid + 1

    return -1


# print(locate_card(cards=cards, query=1))


def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        print("mid:", mid)
        result = condition(mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def locate_card(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return "left"
            else:
                return "found"
        elif cards[mid] < query:
            return "left"
        else:
            return "right"

    return binary_search(lo=0, hi=len(cards) - 1, condition=condition)


# print(locate_card(cards=cards, query=1))


def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return "left"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"

    return binary_search(0, len(nums) - 1, condition)


def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] == target:
                return "right"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"

    return binary_search(0, len(nums) - 1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 10, 11, 12, 13, 14]
lo = 0
hi = len(nums) - 1
mid = (lo + hi) // 2
mid_number = nums[mid]
print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)

# print(first_and_last_position(nums, 9))
