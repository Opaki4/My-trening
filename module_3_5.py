def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        if int(str_number[-1]) == 0:
            return get_multiplied_digits(str_number[0,-1])
        else:
            return first * get_multiplied_digits(int(str_number[1:]))

    return first


result = get_multiplied_digits(40203)
print(result)