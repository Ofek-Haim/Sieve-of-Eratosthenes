"""
Sieve of Eratosthenes.
Date: 25.11.2017.
Ofek Haim.
V = 1.1.
"""

START_NUMBER = 2


def find_prime_numbers_using_eratosthenes(range_number):
    """
    This function get a number and return a list of all the prime numbers,
    up to the given number(include the given number if he is a prime number.)
    :Get: Number
    :OutPut: List of primes
    """
    prime_numbers = []
    not_prime_number_list = []
    for i in range(2, range_number + 1):
        if i not in not_prime_number_list:
            prime_numbers.append(i)
            for j in range(i ** 2, range_number + 1, i):
                not_prime_number_list.append(j)
    return prime_numbers

if __name__ == "__main__":
    number = raw_input("Enter the range - ")
    while 1:
        try:
            number = int(number)
            break
        except ValueError:
            number = raw_input("TypeError : Enter an integer - ")
    list_of_primes = find_prime_numbers_using_eratosthenes(number)
    print "The len of this list is : " + str(len(list_of_primes))
    print list_of_primes
