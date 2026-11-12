n = [3, 5, 7]


def double_list(n):
    for i in range(0, len(n)):
        n[i] = n[i] * 4
# Don't forget to return your new list!
    return n


print(double_list(n))
