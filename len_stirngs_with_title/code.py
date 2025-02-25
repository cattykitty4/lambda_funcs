def totalLenNames(x):  # this simple code is checking elements whether the element starts with a capital letter
    collector = []

    for el in x:
        if el.istitle():
            collector.extend(el)

    return len(collector)


print(totalLenNames(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))

# short function with iterator filter and lambda-function which doing the same as custom function
#
# names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
#
# y = list(filter(lambda x: x.istitle(), names))
# j = sum(list(map(lambda x: len(x), y)))
#
# print(j)
