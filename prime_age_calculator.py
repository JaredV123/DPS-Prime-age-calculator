import datetime
import sympy

print("Enter your birth year here:")
birth_year = float(input())

def next_prime_year(birthyear):
    today = datetime.datetime.now()
    current_year = today.year
    age = current_year - birthyear

    next_prime_age = sympy.nextprime(age)

    return int(birthyear + next_prime_age)

print(next_prime_year(birth_year))

