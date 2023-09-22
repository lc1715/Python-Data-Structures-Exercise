def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

  
    new_lst = []

    lst = phrase.split()

    for val in lst:
        new_lst.append(val.capitalize())
    
    return ' '.join(new_lst)

