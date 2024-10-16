"""Exercise Set 1: Python Basics"""

import numpy as np
import matplotlib as plt


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    var1 = int(input("First Num: "))
    var2 = int(input("Second Num: "))
    var_mult = var1*var2
    if var_mult<1000:
        return var_mult
    else:
        return var1+var2



# ex2
def exercise2():
    var1 = int(input("The range is: "))
    j=0
    for i in range(var1):
        print(f"{i}th number sum with previous ({j}) is: {i+j}")
        j=i
    return


# ex3
def exercise3():
    print("start to input the list.")
    print("enter anything rather than int num to cast out.")
    lst1 = list()
    i = 1
    while True:
        var1 = input(f"element {i}: ")
        i += 1
        try:
            var1 = int(var1)
            lst1.append(var1)
        except:
            print(lst1)
            break
    if lst1[0] == lst1[-1]:
        return True
    else:
        return False



# ex4
def exercise4():
    print("Insert a set of numbers with space in between.\n")
    var1 = input()
    var1 = var1.split()
    lst1 = []
    for i in var1:
        try:
            if float(i)%5 == 0:
                print(float(i))
        except:
            print(f"{i} is not a number :/ try again")
            return exercise4()



# ex5
def exercise5():
    pass


# ex6
def exercise6():
    pass


# ex7
def exercise7():
    pass


# ex8
def exercise8():
    pass


# ex9
def exercise9():
    pass


# ex10
def exercise10():
    pass


# ex11
def exercise11():
    pass


# ex12
def exercise12():
    pass


if __name__ == "__main__":
    print("EXERCISE SET 1")
    print("EX1")
    exercise1()
    print("EX2")
    exercise2()
    print("EX3")
    exercise3()
    print("EX4")
    exercise4()
    print("EX5")
    exercise5()
    print("EX6")
    exercise6()
    print("EX7")
    exercise7()
    print("EX8")
    exercise8()
    print("EX9")
    exercise9()
    print("EX10")
    exercise10()
    print("EX11")
    exercise11()
    print("EX12")
    exercise12()
