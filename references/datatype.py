import math
from helper.printformatter import pt

"""
Topics:
- string datatype and its methods
- splicing string
- number datatype
- datatype conversion
- user input
"""

@pt
def string_datatype():
    word = "HelLo wOrlD. "
    word2 = "another great day, another great night, and yet another workday"
    string_list = ["one", "two"]
    print(f"Original word : \"{word}\"")
    print(f"with upper \t : {word.upper()}")
    print(f"with lower \t : {word.lower()}")
    print(f"with capitalize \t : {word.capitalize()}")
    print(f"with casefold \t : {word.casefold()}")
    print(f"with join \t : {word.join(string_list)}")
    print(f"with center \t : {word.upper().center(20, '*')}")  # __width = total length
    print(f"ends with \t : {word.endswith('wOrlD. ')}")
    print(f"find wOr \t : {word.find('wOr')}")  # returns index (-1 for non-exist)
    try:
        print(f"index He \t : {word.index('z')}")  # same as find, but raise ValueError
    except ValueError as e:
        print("Index of non-exist : ", e)
    print(f"replace \t : {word2.replace('another', 'the', 2)}")  # replace only first 2 instances


@pt
def string_access():
    word = "hello world"
    print(word[0])
    print(word[:])
    print(word[1:-1])
    print(word[::-1])  # read with [:] but step -1 each time

    # looping string as each char
    for w in word:
        print(w, end='-')


@pt
def number_basic():
    num1 = 5.2598
    num2 = 2.751
    num3 = -59.5

    print(num1 / num2)
    print(num1 // num2)
    print(num1 % num2)
    print(abs(num3))
    print(num1 ** 3)  # raised to the power of 3
    print(pow(num1, 3))  # same as ** 3
    print("max", max(num1, num2, num3))
    print("round", round(num1, 2))
    print("ceil", math.ceil(num1))
    print("floor", math.floor(num2))
    print("sqrt", round(math.sqrt(num2), 2))


@pt
def datatype_conversion():
    print("My favorite number is " + str(5.7))


@pt
# required user input!
def datatype_conversion_input():
    # by default, all input from user is treated as 'str' datatype.
    num1 = input("> enter first number  : ")
    num2 = input("> enter second number : ")
    result = float(num1) / float(num2)  # convert string to float
    print(f"result of {num1} divided by {num2} = {result}")


def main():
    string_datatype()
    string_access()
    number_basic()
    datatype_conversion()
    # datatype_conversion_input()


if __name__ == "__main__":
    main()
