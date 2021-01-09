from string import Template

from helper.printformatter import pt

"""
Ref: https://pyformat.info/ for all string formatting purposes

Topics:
- basic printing
- format printing ( % , f"..", format, template)
- string template
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


def print_template_string():
    # method-1 : using .format(...)
    str1 = "you're watching '{0}' by {1}, {0} is a great topic.".format("Method-1", "Hendry")
    print(str1)

    # method-2 : using .format( keyword )
    str2 = "the {q} {b} {f}".format(q='quick', b='brown', f='fox')
    print(str2)

    # method-3 : using template string [keyword-argument]
    template = Template("you're watching '${title}' by ${author}, ${title} is a great topic.")
    str3 = template.substitute(title='Method-2', author="Leon")
    print(str3)

    # method-4 : using template string [dictionary-argument]
    data = {
        'author': 'george',
        'title': 'Method-3',
        'titlea': 'Method-3'  # this will be ignored
    }
    str4 = template.substitute(data)
    print(str4)

    # method-5 : using value:width.precision
    result = 100 / 777
    print("the result of 100/777 is {r:10.3} -- Good stuff!".format(r=result))  # r:width.precision
    print(f"the result of 100/777 is {result:10.3f} -- Good stuff!")


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
    print_template_string()
    print_property()


if __name__ == '__main__':
    main()
