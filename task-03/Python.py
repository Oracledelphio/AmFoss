def prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    n = int(input("Enter a number (n): "))
    if n < 2:
        print("There are no prime numbers up to and including", n)
    else:
        primes = [num for num in range(2, n + 1) if prime(num)]
        print("Prime numbers up to and including", n, "are:", primes)
except ValueError:
    print("Invalid input. Please enter a valid number.")
