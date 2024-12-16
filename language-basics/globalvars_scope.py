#!/usr/bin/env python

from pprint import pp

test = {}
mylist =  []
a = 0
b = "string_global"

def func1():
    print("enter func1")
    print("within func1, add to dict")
    #print(a)
    test["func1"]="added"
    a=1
    mylist.append("appended within func1") #func1 sees global mylist and can modify the list-content!!
    #mylist = [1, 2 ,3]  # reassigned!! # if mylist is locally assigned after the previous stmt => compile error
    b="string_local"
    print(mylist)
    print(a)
    print("quit func1")


def func2():
    print("enter func2")
    global a
    print("within func2, add to dict")
    print(a)
    test["func2"]="added"
    a=2
    print("quit func2")

def main():
    func1()
    print(a)
    print(b)
    func2()
    print(a)
    pp(test)
    print(mylist)

if __name__ == "__main__": 
    main()
