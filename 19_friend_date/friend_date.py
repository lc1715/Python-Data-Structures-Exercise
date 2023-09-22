def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False if not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    
    lst = []  
    lst2 = []

    for val in a:
        lst.append(val)

    for val in b:
        lst2.append(val)

    if lst[2][0] == lst2[2][0]:
        return True
    elif lst[2][0] == lst2[2][1]:
        return True 
    elif lst[2][1] == lst2[2][0]:
        return True
    elif lst [2][1] == lst2[2][1]:
        return True
    else:
        return False
