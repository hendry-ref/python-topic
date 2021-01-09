import math

from helper.printformatter import pt

"""
Topics:
- type()
- truth testing
- string datatype and its methods
- splicing string
- number datatype
- datatype conversion
- user input
"""


@pt
def general_data_types():
    # type() can be used to display the 'type'
    print(f'General data types: \n'
          f'Integer has type {type(5)}\n'
          f'Floating has type {type(2.5)}\n'
          f'String has type {type("hello world")}\n'
          f'List has type {type([1, 2, 3, 4])}\n'
          f'Tuple has type {type((1, 2, 4, 5, 6))}\n'
          f'Dictionary has type {type({"one": 1, "two": 2})}\n'
          f'Sets has type {type({1, 2, 3, 3})}\n'
          f'Boolean has type {type(True)}')


@pt
def truth_test():
    print(f"""These all are false
    False -> {bool(False)}
    None -> {bool(None)}
    0 -> {bool(0)}
    0.0 -> {bool(0.0)}
    "" -> {bool("")}
    [] -> {bool([])}
    {{}} -> {bool({})}
    () -> {bool(())}
    set() -> {bool(set())}
    range(0) -> {bool(range(0))}
    custom -> {bool(CustomFalse())}
    """)


@pt
def string_datatype():
    # strings and bytes are not directly interchangeable
    # strings contains unicode, bytes are raw 8-bit values

    my_byte = bytes([0x41, 0x42, 0x43, 0x44])
    my_byte_decoded = my_byte.decode('utf-8')
    my_str = "This is a string"
    my_str_encoded = my_str.encode('utf-8')

    print(f'Byte value   : {my_byte} has type {type(my_byte)}')
    print(f'Decoded Byte value   : {my_byte_decoded} has type {type(my_byte_decoded)}')
    print(f'String value : {my_str} has type {type(my_str)}')
    print(f'Encoded String value : {my_str_encoded} has type {type(my_str_encoded)}')

    # String is immutable
    # hit error: 'str' object does not support item assignment
    try:
        my_str[0] = "J"
    except TypeError as err:
        print(err)


@pt
def string_method():
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
    print(word[::2])  # start:stop:step
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


class CustomFalse:
    # instance of class that overwrite either __bool__ or __len__ with False/0 will be marked as False in bool(...)
    def __bool__(self):
        return False

    def __len__(self):
        return 0


def main():
    general_data_types()
    truth_test()
    string_datatype()
    string_method()
    string_access()
    number_basic()
    datatype_conversion()
    # datatype_conversion_input()


if __name__ == "__main__":
    main()
