from helper.printformatter import pt

"""
dict { "k" : "v" } : mutable unordered K:V sequence
defaultdict : class that enable dictionary to have default value (if non-exist)
"""


@pt
def dict_create():
    # dictionary is K:V pair, Key must be unique and it can be of any data-types
    the_dict = {1: "one", "dua": "two", "is_human": True, 0: None}
    print("the_dict = ", the_dict)
    print(the_dict.get("dua"))
    print(the_dict[1])

    copy_dict = the_dict.copy()
    print("copied_dict = ", copy_dict)

    copy_dict2 = dict(the_dict)  # dict({1: "one", 2: "two"})
    print("copied_dict2 = ", copy_dict2)


@pt
def dict_access():
    the_dict = {1: "one", "dua": "two", "is_human": True, 0: None}
    # get data from dict with [...] or dict.get(k, default)
    print("key = dua  --> ", the_dict["dua"])
    print("key = 1    --> ", the_dict.get(1))
    print("key = none --> ", the_dict.get("None", "None doesn't exist"))

    # items() returns list of tuple (k,v) of the dict, that we can iterate into.
    print("items() = ", the_dict.items())
    for (k, v) in the_dict.items():
        print(f"Key: {k} -> {v}")

    print("\n- iterate dict without items() -")
    print("All keys : ", the_dict.keys())
    print("All vals : ", the_dict.values())
    for k in the_dict.keys():
        print(f"Key :{k} -> {the_dict[k]}")


@pt
def dict_update():
    the_dict = {1: "one", "dua": "two", "is_human": True, 0: None}
    the_dict[1] = "uno"
    print(the_dict)


@pt
def dict_deletion():
    the_list = [1, "Hello", True, 5.7, None, MyData(), my_func()]

    # list.remove()
    the_list.remove(5.7)
    print("the_list = ", the_list)

    # list.pop() -> remove and return last item in the list
    print("Pop the list : ", the_list.pop())
    print("the_list = ", the_list)

    # list.clear() -> delete everything, returns empty list []
    the_list.clear()
    print("the_list = ", the_list)


@pt
def dict_methods():
    the_list = [1, "Hello", True, 5.7, None, MyData(), my_func()]
    the_list += ["Hello", True, True]

    # list.count() to retrieve number of occurance
    print("count True in the_list = ", the_list.count(True))  # 1 is also True, hence the result is 4

    # sorting the list with sort() and sorted(...)
    print("\n - List sorting - ")
    the_list2 = [12, 6, 1, 2, -6, 90, 0, -100]
    sorted_the_list2 = sorted(the_list2)
    print("original the_list2 = ", the_list2)
    print("sorted_the_list2   = ", sorted_the_list2)
    the_list2.sort()  # in-place sorting
    print("sorted the_list2   = ", the_list2)


class MyData:
    def __str__(self):
        return "From MyData class"


def my_func():
    return "From my_func"


def main():
    dict_create()
    dict_access()
    dict_update()
    dict_deletion()
    dict_methods()


if __name__ == '__main__':
    main()
