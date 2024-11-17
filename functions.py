#   numbers divisible by 7 and multiples of 5
def find_divisible_numbers():
    return [x for x in range(1500, 2701) if x % 7 == 0 and x % 5 == 0]

#  guess a number between 1 and 9
def guess_number_game():
    import random
    number = random.randint(1, 9)
    guess = 0
    while guess != number:
        guess = int(input('Guess a number between 1 and 9: '))
        if guess == number:
            print('Well guessed!')

#  all numbers from 0 to 6 except 3 and 6
def print_numbers():
    for i in range(7):
        if i == 3 or i == 6:
            continue
        print(i)

# pattern using a nested loop
def pattern_nested_loop():
    rows = 5
    for i in range(1, rows+1):
        print('*' * i)
    for i in range(rows-1, 0, -1):
        print('*' * i)

#  reverse a word entered
def reverse_word():
    word = input("Enter a word: ")
    reversed_word = word[::-1]
    print("Reversed word:", reversed_word)

#  count even and odd numbers in a series
def count_even_odd():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    evens = sum(1 for n in numbers if n % 2 == 0)
    odds = len(numbers) - evens
    print("Number of even numbers:", evens)
    print("Number of odd numbers:", odds)

# first alphabet pattern 'A-Z' in your name (Example with 'R')
def alphabet_pattern_R():
    print("R pattern")
    for row in range(7):
        for col in range(7):
            if (col == 1 or ((row == 0 or row == 3) and col > 1 and col < 5) or (col == 5 and row != 0 and row < 4) or (col == row - 1 and row > 2)):
                print("*", end="")
            else:
                print(end=" ")
        print()

#   a nested loop number pattern
def nested_loop_number_pattern():
    for i in range(1, 10):
        print(str(i) * i)

#  create a multiplication table 
def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(num, 'x', i, '=', num * i)

#  the sum and average of n integer numbers
def sum_and_average():
    n = int(input("Enter number of elements: "))
    numbers = list(map(int, input("Enter the numbers : ").split()))
    total = sum(numbers)
    average = total / n
    print("Sum:", total)
    print("Average:", average)

#  Fibonacci sequence 
def fibonacci_sequence():
    def fibonacci(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()
    fibonacci(200)  