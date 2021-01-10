# tuple : ordered, immutable, allows duplicate elements
from helper.printformatter import pt
import sys, timeit

@pt
def tuple_create():
    the_tuple = ("super", 1, True, -2.5)  # with our without bracket, it'll be treated as tuple
    the_string = ("data")  # despite having bracket, single value will be treated as string/int/bool etc.
    single_tuple = ("data",)  # put comma at the end, to create single tuple value
    the_tuple_iterable = tuple("data")  # create tuple from iterable tuple(iter) -> tuple of 'd', 'a', 't', 'a'

    print(f"{the_tuple} has type of {type(the_tuple)}")
    print(f"{the_string} has type of {type(the_string)}")
    print(f"{single_tuple} has type of {type(single_tuple)}")
    print(f"{the_tuple_iterable} has type of {type(the_tuple_iterable)}")


@pt
def tuple_access():
    the_tuple = ("Hendry", 10, "Medan")
    # unpacking must match number of variable (applicable to list too)
    # - hit ValueError: not enough values to unpack if variable > tuple size
    # - hit ValueError: too many values to unpack if variable < tuple size
    name, user_id, loc = the_tuple
    print(f"[#{user_id}] - {name} located at {loc}")

    # unpacking with * to get the list (can only have 1 * )
    the_tuplenum = (1, 2, 3, 4, 5, 6, 7)
    i1, *i2, i3 = the_tuplenum
    print("i1 = ", i1, " , i2 = ", i2, " , i3 = ", i3)


@pt
def tuple_list_efficiency():
    # tuple is immutable and generally has lower size compare to list
    the_list = [0, 1, 2, "hello", True, None]
    the_tuple = tuple(the_list)

    print(f"LIST  {the_list} has size of {sys.getsizeof(the_list)} bytes")

    print(f"TUPLE {the_tuple} has size of {sys.getsizeof(the_tuple)} bytes")
    print(f"Speed to create 1000000 list  = {timeit.timeit(stmt='[0,1,2,3,4,5,6,7,100]', number=1000000)}")
    print(f"Speed to create 1000000 tuple = {timeit.timeit(stmt='(0,1,2,3,4,5,6,7,100)', number=1000000)}")


def main():
    tuple_create()
    tuple_access()
    tuple_list_efficiency()


if __name__ == "__main__":
    main()
