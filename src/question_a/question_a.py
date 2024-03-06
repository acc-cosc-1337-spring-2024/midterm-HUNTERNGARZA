#write functions here, don't add input('') statements here!
def test_config():
    return True


def get_sum_of_evens(num):
    all_numbers = range(num + 1)
    even_numbers = [n for n in all_numbers if (n % 2) == 0]
    return sum(even_numbers)
