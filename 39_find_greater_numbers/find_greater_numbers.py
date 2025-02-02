def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """

    total = 0
  
    while len(nums) > 1:  
        first_num = nums[0]  
        j = greater(nums, first_num)
        total += j

        nums.pop(0)
 
    return total


def greater(nums, first_num):  
    total = 0

    for num in nums:
        if num > first_num:
            total += 1
         
    return total



