from time import time

def group(seq):
    """Divide a sequence of at least 12 elements into groups of 4
    or 5. Groups of 5 will be at the end. Returns a tuple of
    sequences, each corresponding to a group, with type matching
    that of the input sequence.

    >>> group(range(14))
    (range(0, 4), range(4, 9), range(9, 14))
    >>> group(tuple(range(17)))
    ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15, 16))
    """
    if len(seq) == 0:
        return ()
    mult = len(seq) % 4
    if len(seq) >= (4 + mult * 5):
        return (seq[:4],) if len(seq) == 4 else (seq[:4],) + group(seq[4:])
    else:
        return (seq[:5],) if len(seq) == 5 else (seq[:5],) + group(seq[5:])  

def make_accumulator():
    """Return an accumulator function that takes a single numeric
    argument and accumulates that argument into total, then
    returns total.

    >>> acc = make_accumulator()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    pass # replace with your solution
    total = 0
    def accumulate(val):
        nonlocal total
        total += val 
        return total
    return accumulate

class Timer:
    """A timer class that can be used as a context manager with
    the 'with' statement. The constructor must be passed a
    function or callable to be used to determine the current
    time. Initializes the total time to 0. For each entry and
    exit pair, adds the time between the two calls to the total
    time, using the timer function or callable to read the
    current time.

    >>> class Counter:
    ...     def __init__(self):
    ...         self.count = 0
    ...     def __call__(self):
    ...         self.count += 1
    ...         return self.count - 1
    >>> t = Timer(Counter())
    >>> t.total()
    0
    >>> with t:
    ...    t.total()
    0
    >>> t.total()
    1
    >>> with t:
    ...    t.total()
    1
    >>> t.total()
    2
    >>> t2 = Timer(Counter())
    >>> with t2:
    ...    t2.total()
    0
    >>> t2.total()
    1
    >>> t.total()
    2
    """
    def __init__(self, time_fn):
        self.timer_fn = time_fn
        self.sum = 0
        self.checkpoint = 0

    def total(self):
        return self.sum
    
    def __enter__(self):
        _ = self.timer_fn()
        self.checkpoint = _

    def __exit__(self, exc_type, exc_val, exc_tb):
        _ = self.timer_fn()
        self.sum += (_ - self.checkpoint)
        self.checkpoint = _