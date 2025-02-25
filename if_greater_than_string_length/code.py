def checkIsDigit(j, y):
    return y.isdigit() and int(y) > j


def findNumber(x):
    x = x.split()  # split string by elements and convert it into list
    find_len = len(x)  # find length of x
    numbers_collector = [el for el in x if checkIsDigit(find_len, el)]  # calling function checkIsDigit
    # which returns true or false and then list comprehension adds element into list if el is digit and bigger than find len
    return numbers_collector


print(findNumber('sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'))
