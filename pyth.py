# Print the Fibonacci sequence
def fibonacci_sequence(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Finding the Maximum Value in a List
def find_maximum_value(lst):
    return max(lst)

# Counting Vowels in a String
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Finding Prime Numbers within a Range
def find_prime_numbers(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

# Simulating a Basic ATM Withdrawal
def atm_withdrawal(balance, request):
    if request <= balance:
        balance -= request
        print(f"Withdrawal successful. Remaining balance: {balance}")
    else:
        print("Insufficient funds.")
    return balance

# Finding Common Elements in Two Lists
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Calculating Factorial of a Number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Validating User Input with While Loop
def validate_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Invalid input, please enter a number.")

# Finding the Sum of Digits of a Number
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Checking for Palindrome Strings
def is_palindrome(s):
    return s == s[::-1]

# Creating a Dictionary from Two Lists
def create_dict(keys, values):
    return dict(zip(keys, values))

# Simulating a Simple Password Check
def check_password(input_password, actual_password="secret"):
    return input_password == actual_password

# Generating a Multiplication Table for a Given Number
def generate_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")