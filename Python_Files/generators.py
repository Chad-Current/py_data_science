# All Generators are iterators
# Are evaluated lazily, the next vallue in the sequence is computed on demand
# Can model infinite sequences, such as data streams with no definite demand
# Generators are defined by any function that uses yield in it's definition
def gen123():
    yield 1
    yield 2
    yield 3

a = gen123()

next(a)
next(a)
next(a)

for i in gen123():
    print(i)

# Stateful Generators

def take(count,iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return  # Once the counter is equal to count, the return statment is executed and the iteration stops
        counter += 1
        yield item    # This is where controll is passed back to run_take print(items)

def run_take():
    items = [2,3,4,5,6,7,8]
    for item in take(5,items)
        print(items)
""" """

def distinct(iterable):   
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_distinct():
    items = [2,3,4,5,5,5,6,7,8,9]
    for item in distinct(items):
        print(items)

def run_pipeline():
    items = [3,4,4,5,5,5,5,6,7,8]
    for item in take(3,distinct(items)):
        print(item)


if __name__ == '__generators__':
    run_pipeline()
