def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings.
    'Strings are compared in alphabetical order':

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """



    min_and_max = []

    for key in d.keys():
        min_and_max.append(key)

    min_and_max_sorted = sorted(min_and_max)

    return (min_and_max_sorted[0], min_and_max_sorted[-1])
  

