def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is not
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """

    string = ''

    if n < 3:
        return 'Truncation must be at least 3 characters.'

    elif len(phrase) >= n:
        for i in range(n-3):
            string += phrase[i]
        string += '...'
        return string
    
    else:
        return phrase

    

    




    #    for c in range(3, n - 1):
    #      + '...'

    #  for c in range(n, 0, -1 )