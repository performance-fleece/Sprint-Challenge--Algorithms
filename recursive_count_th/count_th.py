'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
thcount = 0


def count_th(word):
    global thcount
    if len(word) < 2:
        finalcount = thcount
        thcount = 0
        print(f'count is {finalcount}')
        return finalcount

    if (ord(word[0]) == 116) and (ord(word[1]) == 104):
        thcount += 1
        return count_th(word[2:])
    elif ord(word[1]) == 116:
        return count_th(word[1:])

    else:
        return count_th(word[2:])


# print(count_th("thaths"))
