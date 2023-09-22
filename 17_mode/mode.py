def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    dic = {}   

    for num in nums:
        dic[num] = nums.count(num)


    new_key = None
    new_value = 0

    for key, value in dic.items():
        if value > new_value:
            new_key = key 
            new_value = value 

    return new_key

    