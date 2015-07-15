def celsius2fahren(degree=0):
    """
    Convert celsius temperature to fahrenheit
    :param degree: can be int or string (default 0)
    :return: int value
    """
    try:
        degree = int(degree)
    except ValueError:
         return False
    if degree < - 273:
        return False
    return degree + 273
