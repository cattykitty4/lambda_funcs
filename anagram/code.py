def isAnagramm(x: [list], y: str) -> list:
    collector = []

    for el in x:
        if sorted(el) == sorted(y):  # for strings sorted() function sort in alphabetical order
            collector.append(el)

    return collector


print(isAnagramm(['bcda', 'abce', 'cbda', 'cbea', 'adcb'], 'abcd'))


# words = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# string = 'abcd'
# s = list(filter(lambda x: sorted(string) == sorted(x), words))
# print(s)
