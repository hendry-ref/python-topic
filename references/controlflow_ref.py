# todo - if, else, for, while, etc.

from helper.printformatter import pt


@pt
def if_else_basic():
    """
    Type of available operator
    - or, and, > , < , != , == ,
    """
    age = 30
    if age >= 80:
        print("Elderly generation")
    elif age >= 50:
        print("Old generation")
    elif age >= 30:
        print("Mature generation")
    else:
        print("Young generation")

    # if with in
    if 'a' in 'hello world':
        print('> a in hello world')
    else:
        print('> a not in hello world')


def main():
    if_else_basic()


if __name__ == '__main__':
    main()
