def pt(func):
    """Decorator to format the text for console printing"""

    def inner(*args, **kwargs):  # get all parameters and ignore them.
        print("\n" + "-" * len(func.__name__))
        print(func.__name__)
        print("-" * len(func.__name__))
        func()
        print("")

    return inner
