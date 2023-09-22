def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    reversed_lst = []
    for char in phrase:
        reversed_lst.insert(0, char)

        string = ''.join(reversed_lst)

    return(string)

