def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    

    lst = []
    lst2 = []

    for char in str(num1):
        lst.append(int(char))

    lst.sort()
    

    for char in str(num2):
        lst2.append(int(char))
    
    lst2.sort()

    if lst == lst2:
        return True
    else:
        return False


    




    # [int(char) for char in str(num2)]
   





    # lst = [num for num in num1]
    # list(num1).sort() == list(num2).sort()


    # print(list(num1))

    # return True if list(num1).sort() == list(num2).sort() else False
        