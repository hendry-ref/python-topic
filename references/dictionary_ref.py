from helper.printformatter import pt

"""
dict { "k" : "v" } : mutable unordered K:V sequence
defaultdict : class that enable dictionary to have default value (if non-exist)
"""


@pt
def dict_create():
    # dictionary is K:V pair, Key must be unique and it can be of any data-types
    # method 1 - literal
    the_dict = {1: "one", "dua": "two", "is_human": True, 0: None}
    print("the_dict = ", the_dict)
    the_dict["tiga"] = "three"
    print("updated the_dict = ", the_dict)
    print(the_dict.get("dua"))
    print(the_dict[1])

    # method 2 - dict function
    the_dict_2 = dict(satu=1, dua="two", is_human=True)
    print("the_dict_2 = ", the_dict_2)

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

    # dict.keys() and dict.values()
    print("\n- iterate dict without items() -")
    print("All keys : ", the_dict.keys())
    print("All vals : ", the_dict.values())
    for k in the_dict.keys():
        print(f"Key :{k} -> {the_dict[k]}")


@pt
def dict_update():
    the_dict = {1: "one", "dua": "two", "is_human": True, 0: None}
    print("Original dict = ", the_dict)
    the_dict[1] = "uno"
    print(the_dict)


@pt
def dict_deletion():
    the_dict = {1: "one", "dua": "two", "is_human": True, 0: None}

    # dict.del()
    del the_dict["is_human"]  # delete this specific K:V , del the_dict will delete entire dictionary
    print("the_dict = ", the_dict)

    print(len(the_dict))
    # dict.pop() -> remove and return last item in the dictionary
    print("Pop the dict : ", the_dict.pop("dua"))
    print("the_dict after pop() = ", the_dict)

    # list.clear() -> delete everything, returns empty list []
    the_dict.clear()
    print("the_dict after clear() = ", the_dict)


@pt
def dict_methods():
    pass


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
