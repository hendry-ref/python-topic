from helper.printformatter import pt


@pt
def basic_exception():
    try:
        num = 10 / 0
    except ZeroDivisionError as zde:
        print(" > ZDE : ", zde)
        print(" > ", zde.__doc__)
    except Exception as err:
        print(" > Exception : ", err)
        print(" > ", err.__doc__)
    finally:
        print("End of method")


def main():
    basic_exception()


if __name__ == '__main__':
    main()
