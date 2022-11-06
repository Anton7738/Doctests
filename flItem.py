def first_last_item(li):
    """
    >>> li = ['apples','bananas','oranges','grapes','watermelons']
    >>> first_last_item(li)
    'apples-watermelons'
    >>> first_last_item(li)
    apples-watermelons
    """

    return li[0] + '-' + li[-1]


