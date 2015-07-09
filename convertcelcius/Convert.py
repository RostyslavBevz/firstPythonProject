def celsius2fahren(degree):
    try:
        degree = int(degree)
    except ValueError:
         return False
    if degree < - 273:
        return False
    return degree + 273

def ask_user():
    user_val = input("Please, enter temperature in Celcius:")
    print(celsius2fahren(user_val))