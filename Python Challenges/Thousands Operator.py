def format_number(number):
    if number < 0:
        return

    number = "{:,}".format(number)

    return number

print(format_number(10000))
