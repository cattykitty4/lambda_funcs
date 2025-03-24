def numsSum(x: list[int]):  # this simple function adds positive numbers to positive numbers and negative numbers to negative numbers
    total_of_positive = 0
    total_of_negative = 0

    for el in x:
        if el < 0:
            total_of_negative += el
        else:
            total_of_positive += el

    return f'{total_of_positive}\n{total_of_negative}'


print(numsSum([2, 4, -6, -9, 11, -12, 14, -5, 17]))

# short function with iterator filter and lambda-function which doing the same as custom function

# nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
#
# sum_of_positive = sum(list(filter(lambda x: x > 0, nums)))
# sum_of_negative = sum(list(filter(lambda x: x < 0, nums)))
#
# print(f'Total of below zero numbers: {sum_of_positive}')
# print(f'Total of above zero numbers: {sum_of_negative}')

