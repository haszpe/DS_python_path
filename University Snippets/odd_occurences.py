
def find_it(seq):
    '''
    This function takes a sequence of numbers and returns the number that appears an odd number of times.
    '''
    elem = list(set(seq))
    n = len(elem)
    lists =[]
    for i in elem:
        x = [i]
        lists.append(x)

    for i in seq:
        for j in lists:
            if i == j[0]:
                j.append(i)

    for g in lists:
        if (len(g)-1) % 2 == 1:
            return g[0]
    return None

one = [1, 3 , 2 , -1, 1, 3, 2, 2, 2, 10, -1]
two = [23,23,45,56,-12,-12, 45, 56, 76 ,87, 90]

print(find_it(one))
print(find_it(two))

