def sum_numbers(numbers=None):
    sum = 0
    if numbers is None:
        numbers = range(1,101)

    for i in numbers:
        sum += i

    return sum
