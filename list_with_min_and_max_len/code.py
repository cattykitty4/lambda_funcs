def minMaxLen(x: list[list[int]]):
    max_el = []                             # initiate two lists which will be collect result
    min_el = []

    max_len = 0
    min_len = float('inf')                  # initiate min len with 'inf' value to correct comparison with nested lists
                                            # which not in ascending order
    for el in x:
        if len(el) > max_len:
            max_len = len(el)
            if len(el) > len(max_el):
                max_el.clear()              # clear list to del previous correct result
                max_el.append(el)

        if len(el) < min_len:
            min_len = len(el)
            if len(el) > len(min_el):
                min_el.clear()              # clear list to del previous correct result
                min_el.append(el)

    return (min_len, *min_el), (max_len, *max_el)


print(minMaxLen([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))
print(minMaxLen([[1, 1, 3], [5, 7], [9, 11], [13, 15, 0, 17], [13, 15, 17]]))


# short function with iterator filter and lambda-function which doing the same as custom function

# massive = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
#
#
# minimum_length = list(map(lambda x: (len(min(massive)), min(massive)), massive))[0]
# maximum_length = list(map(lambda x: (len(max(massive)), max(massive)), massive))[0]
#
# print(minimum_length)
# print(maximum_length)
