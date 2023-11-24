def my_func_args(*args):
    print("> args fn")
    print(type(args), args)


def my_func_kwargs(**kwargs):
    print("> kwargs fn")
    print(type(kwargs), kwargs)


def my_func_args_kwargs(*args, **kwargs):
    print("> args and kwargs fn")
    print(type(args), args)
    print(type(kwargs), kwargs)


def my_config(name, color, **kwargs):
    print("> my config fn")
    print(name, color, kwargs)


if __name__ == "__main__":
    my_func_args("Hello", 1, 2, 10)
    my_func_kwargs(name="Hello", order=1, copy=2, send=10)

    my_func_args_kwargs("Hello", 1, copy=2, send=10)

    my_config("Tl", "blue", u="PSU", province="Songkhla")
