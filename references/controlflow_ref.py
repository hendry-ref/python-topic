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
    if 'a' in 'hello world':  # or if 1 in [1,2,3,4]:
        print('> a in hello world')
    else:
        print('> a not in hello world')


@pt
def while_loop():
    i = 1

    # full while-loop
    while i <= 5:
        print(f"i = {i}", end=" , ")
        i += 1
    else:
        print("Completed entire while-loop")

    # break/continue while-loop
    i = 1
    while i <= 100:
        if i % 5 == 0:
            i += 1
            continue
        elif i > 15:
            break
        else:
            print(f"i = {i}", end=" , ")
        i += 1
    else:
        print("[Wrong] completed entire while-loop")
    print("END")


@pt
def for_loop():
    for i in range(2, 10, 2):  # 2,4,6,8 (exclude 10)
        print(f"i = {i}", end=", ")
    print()

    for l in ["hello", 1, True, None]:  # or range(len(my_list))
        print(l, end=", ")
    print()


def main():
    if_else_basic()
    while_loop()
    for_loop()


if __name__ == '__main__':
    main()
