def task_a():
    first = 7
    second = 44.3
    print(first + second)
    print(first * second)
    print(first / second)


# task b
# value of a at the end is : 9
# value of b at the end is : 8
# value of c at the end is : 15


def task_c():
    # there is no difference in single or double quoted string. Both representations can be used interchangeably
    my_number = 5 + 5
    print("result is %s" % my_number)
    pass


# Task d: # the output will be 7

def task_e(x=0, y=0):
    print('BIG') if x > y else print('small')


def task_f(a):
    a = a or 2
    if a == 1:
        print("summer")
    elif a == 2:
        print("winter")
    elif a == 3:
        print("fall")
    elif a == 4:
        print("spring")
    else:
        print("please provide correct input")


def challenge():
    a = 8
    b = "123"
    print(str(a) + b)


def extra1():
    var1 = 5
    var2 = "5"
    res = var1 == var2
    sum = var1 + int(var2)
    print("total sum is larger than 5.5") if sum > 5.5 else print("total sum is less than 5.5")
    if len("hello") > len("helloo"):
        return True


def extra2():
    while True:
        name = input("Please enter your name: ")
        if name[0] != 'A':
            print("Sorry, your provided name does not start with A character.")
            continue
        else:
            break
    age = input("Please enter your age: ")
    if not isinstance(age, int):
        print("age input has which has been entered is not an integer")
    work = input("Please enter your work field: ")
    print("your stored work field is %s" % work)


def main():
    extra2()


if __name__ == "__main__":
    main()
