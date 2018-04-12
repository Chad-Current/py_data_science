import math
import os
def howToVariable(): # Not really variables as in other languages but a Name Reference to Objects
    """
    Looking at how binding with variables works
    """
    x = 1000 # the object created is the 1000 and is immutable, x is just referencing the 1000 object
    y = x # the obect is now referenced by both the x and y variables
    # id() deals with the object not the reference, where as "is" refers to the referencing
    print("checking is")
    print(x is y)
    print("Is checked")
    print("X: ",x)
    print("Y: ",y)
    print("X_id: ",id(x))
    print("Y_id: ",id(y))
    print("checking id")
    print(id(x) == id(y))
    print("Id checked")
    x = 3000
    print("X: ",x)
    print("Y: ",y)
    print("X_id: ",id(x))
    print("Y_id: ",id(y))
    print("checking id")
    print(id(x) == id(y))
    print("Id checked")
    return
def howToBinding(): # Binding of objects i.e. variables
    r = [2,4,6]
    s = r #binding the list object of [2,4,6] to variable s also
    print("Printing r-list: ",r)
    print("Printing s-list: ",s)
    print("Is r and s equal",(s is r))
    s[0] = 17 #now the list object od [2,4,6] is now [17,4,6] and the variable s reference will reflex the same
    print("Printing r-list modified by s[0] = 17 : ",r)
    print("Printing s-list modified by s[0] = 17 : ",s)
    print("Is r and s equal",(s is r))
    return
def howToFunctionRef(): #Showing how functions can modify and not modify Named References to Objects i.e. variable
    g  = [1,2,3,4,5]
    print("*List G: ",g)
    def nonChangeList(g):
        h = [6,7,8,9,10]
        print("**Printing List nonChangeList of h: ",h)
        return
    nonChangeList(g)
    print("***List G is not changed : ",g)
    def changingList(g):
        h = g # h is a reference to the same object that g is also referened too
        h[0] = 6
        h[1] = 7
        h[2] = 8
        h[3] = 9
        h[4] = 10
        print("*****Printing changingList with new reference objects: ",g)
        return
    changingList(g)
    print("******Now Changed List G: ", g)
def howToScope(): # Showing how to access global variable
    # print("Enter Count")
    count = 0
    c = 0
    # input(c)
    def set_count_non_global(c):
        count = c
        print("Non-Global count : ",c)
    def set_count_global(c):
        global count
        count = c
        print("Global count : ",c)
def howToCollectionsTuple():
    def minmax(items):
        return min(items),max(items)
    myTuple = (14,66,33,77)
    alphaTuple = (a,(b,(c,d))) = (1,(2,(3,4)))
    print(14 in myTuple) # checking value in tuple,
    print(14 not in myTuple) # checking value not in tuple
    a = 'jelly'
    b = 'bean'
    print("Intial state before tuple unpacking ",a)
    print("Intial state before tuple unpacking ",b)
    a, b = b ,a
    print("State after swap tuple ",a)
    print("State after swap tuple ",b)
    lower, upper = minmax(myTuple)
    print("Printing lower and upper tuple from myTuple lower and upper",lower,upper)
    print("*Tuple is t = () format , t = ((222,333),(444,555)) 'immutable'")
def howToCollectionsStr(): # Showing string
    lengthofstring = "this is a string that is using length is find the length of the string"
    print("Length of the string lengthofstring ",len(lengthofstring))
    lengthofstring = "--".join([lengthofstring,'#435ff0'])
    print("Join method : ", lengthofstring)
    print("Split method : ", lengthofstring.split('--'))
    print("Partition Method : ", lengthofstring.partition("string"))
    origin, _, end = lengthofstring.partition('length')
    print(origin)
    print(end)
    print("This _, is elimanting the unnecessary 'stuff' from the string")
    print("This is a format example {0} is {1} and also {0}".format('here','there'))
    print("This is another style of format {} and {}".format('here','there')) # Usable when the args are used in sequence
    print("This is a default style of format {lat}, {long}".format(lat="60N",
                                                                   long="5E"))
    pos = (65.3,32.1,82.2)
    print("This is a tuple string format x={pos[0]}, y={pos[1]}, z ={pos[2]}".format(pos=pos))
    print("This is a format to three trailing only, pi ={m.pi:.3f}".format(m=math))
    print("This is a format now 10 trailing, pi ={m.pi:.10f}".format(m=math))
def howToCollectionsRange(): # Ranges are not widely used in modern Python
    for i in range(5):
        print(i)
    range(5,10)
    print(list(range(5,20,3))) #start,stop,step
    print("Always prefer to use iteration over iterable objcts, such as list, don't abuse range")
    s = [4,6,8,10]
    print("This is the list of s: ",s)
    for r in s:
        print(r)
    for r in enumerate(s):
        print("Yields (index,value) ",r)
    for r, t in enumerate(s):
        print("Tuple unpacking  i = {}, v = {}".format(r,t))
def howToCollectionsList(): # List
     s ="show how to index into sequences".split()
     print(s)
     print("After Split ",s[-3]) # negative indexing is more elegant
     t = s[1:3]
     u = s[3:]
     v = s[:3]
     print("Printing on the first and second indices with stop at 3-index", t)
     print("Printing from the third indices on ",u)
     print("Printing the first three indices ",v)
     full_slice = s[:] # !Important idiom for copying list
     print("Copied list of s to full_slice :",full_slice)
     x = s.copy()
     w = list(s) # !This is the more preferable way as it can work with any iterable series as the source, not just the list
                 # This is shallow copying
                 # def howToCollectionsListRep(): # List Repetition :GOTO COLLECTIONS SHALLOW COPIES AND REDO SECTION ON COLLECTIONS from SHALLOW on
def howToCollectionsDict(): # Dictionaries are iterable and random with no indices
    myDict = {'name':'Chad','age':35,'gender':'male'} # Dictionary keys are immutable and values are mutable(can be changed)
    print("Printing myDict'name'",myDict['name'])
    group = [('Holly',41),('Sharon',70)]
    d = dict(group) # dict() constructor accepts iterable seris of key-value 2-tuples(shown below)
    print("Printing groups :",d)
    tup = ((a,b),(c,d)) = (('name','age'),('gender','location'))
    t = dict(tup)
    print("Printing tuple", t)
    keyWords = dict(a="alpha",b="bravo",c="charlie",d="delta")
    print("Printing direct input to dict() constructor ", keyWords)
    t.update(keyWords)
    print("Printing tuple with update (keyWords)", t)
    for key, value in t.items():
            print("{key} => {value}".format(key=key,value=value))
def howToCollectionSet(): # Sets are mutable as items can be added and removed from the set, but each element is immutable
    p = {1,2,3,4,5,6,7,7,7,7,8} # Duplicates are removed
    print("Printing set of p : ",p)
    d = set() # Must set set() constructor otherwise it will create a dict type
    print(type(d))
    p.add(10)
    print("10 was added to the set ", p)
    p.update([11,12,13])
    print("11,12,13 were added by update method ",p)
    p.remove(13)
    p.discard(99)
    r = p.copy() # shallow copy, copies references, but not the objects they refer to
    t = set(p)
    blue_eyes = {'chad','holly','sharon','george'}
    blonde_hair = {'chad','george','Frank'}
    red_hair = {'holly'}
    print("Showing Union Method, i.e. all blue-eyes and blonde hair",blue_eyes.union(blonde_hair))
    print("Showing ")
    print("Checking equality of sets ",blue_eyes.union() == blonde_hair.union()) # Communiative
    print("Showing intersections : ", blue_eyes.intersection(blonde_hair))
    print("Showing difference : ",blue_eyes.difference(blonde_hair))
    print("Showing exclusive blue or blonde but not both :", blue_eyes.symmetric_difference(blonde_hair))
    print("Is subset : ", blue_eyes.issubset(blonde_hair))
    print("Is superset : ", blue_eyes.issuperset(blonde_hair))
    print("Is disjoint, no commonality : ", blue_eyes.isdisjoint(blonde_hair))
def howToHandlingExceptions():
    print("Nothing")
def convert(s):
    try:
        x= int(s)
        print("Conversion succeeded! x =",x)
    except ValueError:
        print("Conversion Failed!")
        x = -1
    return x



if __name__ == '__main__':
print (__name__)

print('\n')
howToVariable()
print('\n')
howToBinding()
print('\n')
howToFunctionRef()
print('\n')
howToScope()
print('\n')
howToCollectionsTuple()
print('\n')
howToCollectionsStr()
print('\n')
howToCollectionsRange()
print('\n')
howToCollectionsList()
print('\n')
# howToCollectionsListRep()
# print('\n')
howToCollectionsDict()
print('\n')
howToCollectionSet()
print('\n')
howToHandlingExceptions()
print('\n')
convert()
