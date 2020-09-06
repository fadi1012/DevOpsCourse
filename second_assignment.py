def a(x, y):
    return "BIG" if x > y else "small"


def b():
    for i in range(5):
        print(f"iteration number is {i}")


def c(x=1):
    if x == 1:
        return "summer"
    elif x == 2:
        return "winter"
    elif x == "3":
        return "fall"
    elif x == "4":
        return "spring"
    print("please enter a valid number from 1 to 4")
    return False


def d():
    # the method will run till it reaches count 11 which is from 1 to 10 - > 10 times
    # 11 will be printed last
    pass


def e(age=27, first_letter_of_your_firstname="f", curreny=3.4, departed=True, apt_num=3):
    print(f"age value is {age}")
    print(f"first letter of your firstname is {first_letter_of_your_firstname}")
    print(f"current shekels-dollar currency is {curreny}")
    print(f"flying abroad status is {departed}")
    print(f"apartment number is {apt_num}")
    res = None
    try:
        res = age + curreny
    except e:
        print(f"the following error occurred {e}")
    return res


def f():
    phone_number = input("Please enter your phone number:")
    print(f"phone number is {phone_number}")


# G
def print_hello():
    return print("hello")


def calculate(x=5, y=3.2):
    return print(f"sum is {x + y}")


# H
def print_name(name):
    return print(f"name is {name}")


def divide_number(number, divison=2):
    return number / divison


# I
def i(x, y):
    return x + y


def i1(s1, s2):
    return (s1 + s2).strip()


def pyramid(n=5):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


def x_shape(N=7):
    for i in range(N):
        for j in range(N):
            if (i == j) or ((N - j - 1) == i):
                print('*', end='')
            else:
                print(' ', end='')
        print('')


def m():
    number = int(input("Please enter an number:"))
    return number


def m1(method):
    number = method()
    sum = 0
    while number != 0:
        sum += number % 10
        number //= 10
    print(f"sum is {sum}")
    return sum


def main():
    pyramid()
    x_shape()
    m1(m)


if __name__ == "__main__":
    main()
