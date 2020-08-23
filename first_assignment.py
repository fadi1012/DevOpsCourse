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


def main():
    task_a()


if __name__ == "__main__":
    main()
