import os
import sys
import math
import glob

words ='Why sometime i have believed as many as six impossible things'.split()
print(words)
# below is the list comprehesion
[len(word) for word in words]
""" [expr(item) for item in iterable]
That is for each item in the iterable we evaluate the expression on the left

Same as ^^^
lengths = []
    for words in words:
        lengths.append(len(word))

"""
# Set comprehesion
aset = {1,2,3,4,5,6,7,8}
{len(str(sets)) for sets in aset}

# Dictionary comprehesion
# {key_expr:value_expr for item in iterable}
country_to_capital {'Usa':'D.C.','Japan':'Tokyo','China':'Shanghi'}
country_to_capital = {capital: country for country, capital in country_to_capital.items()}
                    # ^key_expr  ^^^key for key^^^    ^^^tuple unpacking using the .items()^^^

# A gotcha moment
words = ['hi','hello','foxtrot','bravo','hotel']
{x[0]:x for x in words}
#^take the first index of the key made and make it the key.
#prints {'h':'hotel','f':'foxtrot','b','bravo'}
# This is because duplicate keys overwrite earlier keys, beware of this

# import os
# import glob
# file_sizes = {os.path.realpath(p):os.stat(p).st_size for p in glob.glob('*.py')}

# Filtering Predicates
def is_prime(x):
    if x < 2:
        return False
    for i in range(2,int(sqrt(x))+1):
        if x % 1 == 0
            return False
    return True

[x for x in range(101) if is_prime(x)]  # *if* is the filtering clause i.e. predicate


# Iterable Protocol and Iterator Protocol
# iterator = iter(iterable)
# item = next(iterator)

# Generator comprehesion
# (expr(item) for item in iterable)
mill = (x * x for x in range(1,100))
list(mill) # forcing the generator to list numbers


if __name__ == '__comprehensions__':
    print(__name__)
