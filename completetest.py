import pandas as pd
import ast_exporter

class Test:
    def do_something(a):
        print('another test')
class Test2(Test):
    def do_something(a):
        print('another test')

class MyClass(Test2):


    def __init__(self, classValue):
        print("hi")
        self.classValue = 1

    #My comment to define a method
    def a_method(a,b):
        res = 0
        x = [1 for x in range(0,5) if x > 1]
        x.sort(key=lambda x: x[1])

        for i in range(0,5):
            a ++ a # unary op
            res += a + b
        
        with open('/etc/passwd', 'r') as f:
            for line in f:
                print (line)
                break

        for i in range(0,5):
            res -= a + b
        
        while i in range(0,5):
            res+=a+b
        ast_exporter.export_dict(None) 
        return res

if __name__ == '__main__':
    print(MyClass.a_method(1,2))
elif __name__ == '__main__' or __name__ == "__main2__":
    print("Idk what to do")
else:
    print("whatever")
    
#Ann Assign
foo : int = 42
{1:2}
{0, 1, 2}
{s for s in [1, 2, 1, 0]}
{s:1 for s in [1, 2, 1, 0]}
del MyClass
sum(x*x for x in range(10)) #generator expressions


async def foo1(param):
    assert param, "fail"

await foo1(None)
(1,2)
def foo2(holi, *param, adior):
    try:
        raise BaseException
    except BaseException:
        print("found it not stopping now")

#if expression
a if b else c
'hello'*3

def iterable1():
    yield 1
    yield 2

def iterable2():
    yield from iterable1()
    yield 3

t[1:'this':t] #slicing
t[...,1:]

'''
asdasfdas
'''