def cel_to_fh(num):
    """
    Converts Celsius temperature to Fahrenheit.
    """
    convert = num * 9/5 + 32
    # as we can see here, 3 operation performing in this operation and it varies significantly
    # this method is also not good for measuring time ...
    return convert

num = int(input("Enter temperature in Celsius \n"))
pass_fun = cel_to_fh(num)

print(f"{num}°C is equal to {pass_fun}°F")