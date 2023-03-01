
def sum_even_numbers(num_list):

    sum = 0
    for number in num_list:
        if number % 2 == 0:
            sum += number
    return sum
