def square(x):
    """Return the square of x.
    >>> square(2)
    4
    >>> square(-2)
    4
    """
    return x * x

if __name__ == '__main__':
    import doctest
    f = doctest.testmod()
    if f.failed == 0:
        print("success, pay!")
    else:
        print("nope")
