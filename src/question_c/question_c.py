def is_prime(number):
    for n in range(2, number):
        if (number%n == 0):
            return False
        
    return True
