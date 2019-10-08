list1 = ['Engineering', 'Computer Science', 'Political Science', 'Mathematics']
list2 = ['Lab', 'Homework', 'Essay', 'Module']

# Your code here:
def segundo_elem(lista):
    return lista[1]


zipped = list(zip(list1, list2))
#print(zipped)


zipped.sort(key=segundo_elem)
print(zipped)


import operator
d = {'Honda': 1997, 'Toyota': 1995, 'Audi': 2001, 'BMW': 2005}

# Your code here:

d_en_orden = sorted(d.items(), key=operator.itemgetter(1))

print(d_en_orden)


# Your code here:
mod = lambda x, y: '1' if x % y == 0 else '0'


def divisor(b):
    """
    input: a number
    output: a function that returns 1 if the number is divisible by another number (to be passed later) and zero otherwise
    """

    # Your code here:
    return mod(b)


print(divisor(5))
