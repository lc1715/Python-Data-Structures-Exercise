def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    lst = []

    for char in phrase:
        lst.insert(0, char)
        string = ''.join(lst).replace(' ','').lower()
    
    new_phrase = phrase.replace(' ','').lower()

    if string == new_phrase:
        return True
    else:
        return False
   