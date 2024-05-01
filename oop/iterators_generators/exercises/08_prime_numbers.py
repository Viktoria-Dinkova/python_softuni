"""
Create a generator function called get_primes() which should receive a list of integer numbers
and return a list containing only the prime numbers from the initial list.
You can learn more about prime numbers here:
"""

from typing import List


def get_primes(int_list: List[int]):
    for cuur_int in int_list:
        if cuur_int <= 1:
            continue

        for n in range(2, cuur_int):
            if cuur_int % n == 0:
                break
        else:
            yield cuur_int

# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))