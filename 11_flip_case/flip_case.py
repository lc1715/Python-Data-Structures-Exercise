def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    string = ''
    
    for char in phrase:
        if char.swapcase() == to_swap:
            string += char.swapcase()
        elif char == to_swap:
            string += char.swapcase()
        elif char != to_swap:
            string += char
    return string
    

