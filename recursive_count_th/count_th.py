'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2:
        return 0
    test = word[:2]
    rest = word[1:]
    if test == 'th':
        return 1 + count_th(rest)
    else:
        return count_th(rest)
    # print(test, rest)


# print(count_th('Thanksgiveth'))
