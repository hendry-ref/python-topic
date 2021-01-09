from helper.printformatter import pt

"""
Topics:
- basic printing
- format printing
- escape character
"""


@pt
def basic_print():
    my_var = "hello world"
    print("Hello world")
    print(my_var)
    print("[1] I'm printing " + my_var)
    print("[2] I'm printing ", my_var)


@pt
def print_formatting():
    """
    Multiple way of formatting:
    - "... %s %d ..." % ("hello", 5)
    - f"... {var} ..."
    - "... %s %d ...".format(var)
    """
    my_var = "hello world"
    my_num = 12123816.349
    print(f"[3] I'm printing {my_var}, which has length {len(my_var)}")
    print("[4] I'm printing %s with %.2f" % (my_var, my_num))  # str % (tuple)
    print("$ {:,.2f}".format(my_num))  # print currency with comma as thousandth separator and 2 decimal


@pt
def print_property():
    # sep for separating objects passed into print(...). (default = "")
    print("This", "is", "\"my\"", "name", sep=" ---")

    # end is for end of print. (default = \n)
    for i in range(3):
        print(i, end=",")


def main():
    basic_print()
    print_formatting()
    print_property()


if __name__ == '__main__':
    main()
