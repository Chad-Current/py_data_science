# Implemented as callables that take a callable and return other callables
"""
Example of what is happenend

****Function Decorators

@my_decorator
def my_function(x,y):
    return x + y   ---> this is a returned function object which is then passed to
                        the function my_decorator(f):
                        return new_f ---> Function object



        def escape_unicode(f):  <-- the f argument is being passed to line 13 as a function i.e. function object
1.            def wrap(*args,**kwargs): <-- this is just taking an unknown amount of args and passing them to the line below
2.                x = f(*args,**kwargs) <-- this is essentially def northern_city with the argument of a
3.                return ascii(x)
            return wrap

        @escape_unicode
2.       def northern_city(a):    <--- this code is called in the REPL first, this added to the escape_unicode method
            return a      <--- this returned object is passed to the escape_unicode(f) as the f argument

calling northern_city goes in the sequence above, wrap function first, then the execution of northern_city is 
applied to x, then the return statement is exucuted, hence the decorator is always executed first

****Classes as Decorators

The class needs to be callable i.e. __call__ method, the dundercall

class Hello:
    def __init__(self,f):
        self.f = f
        self.count = 0
    def __call__(self,*args,**kwargs):
        self.count += 1
        return self.f(*args,**kwargs)

@Hello
def sayhello(*args):
    print('Hello {}'.format(*args))


****Class instance Decorators --- We are using the instance of the class as the decorator, !!Not the class itself!!

class Trace:
    def __init__(self):
        self.enable = True
    def __call__(self,f):
        def wrap(*args,**kwargs):
            if self.enable:
                print('Calling {}'.format(f))
            return wrap

tracer = Trace()    <--- instaniating an object

@tracer             <--- here is the instance being used as the decorator
def rotate_list(l):
    return l[1:] + [l[0]]

****Multiple Decorators

@decorator1   <--- When decorators are used like this, they are processed in reverse order, so dec3, then dec2 and finally dec1
@decorator2
@decorator3
def some_function():    The some_function is passed first to decorator3, the result is called by decorator2, and so on



***functools.wrap()

 import functools

 def noop(f):
     @functools.wraps(f)  <--- this decorator makes it so the hello name and doc are shown(called) essentially replaces code below
     def noop_wrapper():        noop_wrapper.__name__ = f.__name__  and noop_wrapper.__doc__ = f.__doc__
         return f()
     return noop_wrapper

@noop
def hell0():
    "Print a well known message"
    print('Hell world!')


***More complex Decorators

def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError('Argument {} must not be negative.'.format(index))
            return f(*args)
        return wrap
    return validator

@check_non_negative(1)
def create_list(value,size):
    return [value] * size
