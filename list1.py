def average(listN):
    
    """
    >>> listN = [20,10,15,75]
    >>> average(listN)
    30
    """

    sumN = 0

    for val in listN:
        sumN += val

    return sumN / len(listN)

