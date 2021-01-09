from helper.printformatter import pt

"""
Collections can have multiple value of different data-types in it's sequence.

List []  : mutable, ordered, non-unique sequence
    - C = append(v), insert (i, v) , ls = [0] * 5 , ls += ls2 , ls.extend(ls2)
    - R = list[i] , list[slice:slice]
    - U = list[i] = v
    - D = clear() , remove(v), pop()
    - Others = reverse(), sort() , sorted(the_list) , list3 = list1 + list2
    - Copy : list2 = list1.copy() , list2 = list(list1) , list2 = list1[:]
    
Tuple () : immutable, ordered, non-unique sequence
    - C = tp = (1,2,3.5)

dict { "k" : "v" } : mutable unordered K:V sequence
set {}   : mutable unordered unique sequence
namedtuple : tuple with named fields
OrderedDict : mutable ordered set of K:V
defaultdict : class that enable dictionary to have default value (if non-exist)
Counter : track number of distinct value. We can wrap a list in a counter ( Counter ([1,1,1,2,2,3]) )
    - it'll automatically create { 1 : 3 , 2 : 2 , 3 : 1 }
    - Counter.update( list... )
    - Counter.subtract ( list... )
    - x = Counter (...)  -->  x.most_common(3)
deque : double-ended list object
"""


@pt
def list_basic():
    # list can have any data types (including user-defined or function)
    the_list = [1, "Hello", True, 5.7, None, MyData(), my_func()]

    print("The list data : ")
    for i in the_list:
        print(i, end="  ||  ")
    print()

    print("\n - List access - ")
    try:
        print("index of 5.7 : ", the_list.index(51))
    except ValueError as err:
        print(err)

    the_list += ["Hello", True, True]
    print("count True in the_list = ", the_list.count(True))  # 1 is also True, hence the result is 4

    # add to list with insert and append
    print("\n - List modification - ")

    the_list.append("New Data")
    print("the_list = ", the_list)

    the_list.insert(3, "index-3")
    print("new_list = ", the_list)

    # extend list with += and extend
    another_list = ["good", 100]
    the_list += another_list
    print("the_list = ", the_list)

    another_list2 = ["bad", 0]
    the_list.extend(another_list2)  # similar to += , however we can chain this other function
    print("the_list = ", the_list)

    # sorting the list with sort() and sorted(...)
    print("\n - List sorting - ")
    the_list2 = [12, 6, 1, 2, -6, 90, 0, -100]
    sorted_the_list2 = sorted(the_list2)
    print("original the_list2 = ", the_list2)
    print("sorted_the_list2   = ", sorted_the_list2)
    the_list2.sort()  # in-place sorting
    print("sorted the_list2   = ", the_list2)

    # remove list with pop, remove and clear
    print("\n - List deletion - ")
    the_list.remove(5.7)
    print("the_list = ", the_list)

    print("Pop the list : ", the_list.pop())
    print("the_list = ", the_list)

    the_list.clear()
    print("the_list = ", the_list)


@pt
def tuple_basic():
    coord = (4, 5)
    coord += (6, 7)
    print(coord)

    try:
        coord[0] = 7  # tuple is immutable
    except TypeError as err:
        print(err)


class MyData:
    def __str__(self):
        return "From MyData class"


def my_func():
    return "From my_func"


def main():
    list_basic()
    tuple_basic()


if __name__ == '__main__':
    main()
