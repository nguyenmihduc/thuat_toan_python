# parents = [3, 7, 5, 2, 3, 6, None, 2, 4]
# parents = [None, 0, 0, 4, 2, 3]
# nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8]


# def handle_short_path(start, end, parents):
#     result = []
#     result.append(end)
#     parent = parents[end]
#     for _ in range(len(parents)):
#         if parents[parent] == None:
#             return result

#         if parent not in result:
#             result.append(parent)

#         parent = parents[parent]

#         if parent not in result:
#             result.append(parent)

#     result = result.reverse()
#     return result

# result = handle_short_path(0, 5, parents)
# result.reverse()
# print(result)


# def handle_short_path(start, end, parents):
#     result = []
#     result.append(end)
#     idx = parents[end]
#     result.append(idx)

#     while idx is not None:
#         next = parents[idx]
#         result.append(next)
#         idx = next

#     return result


# result = handle_short_path(7, 8, [3, 7, 5, 2, 3, 6, None, 2, 4])

# print(result)


