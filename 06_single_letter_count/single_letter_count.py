def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """

    dic = {}

    letter_lower_case = letter.lower()
    word_lower_case = word.lower()

    if letter_lower_case in word_lower_case:
        for char in word:                          
            lower_case = char.lower()

            if lower_case in dic:
                dic[lower_case] += 1
            else:
                dic[lower_case] = 1
    else:
        return 0

    return dic[letter_lower_case]


