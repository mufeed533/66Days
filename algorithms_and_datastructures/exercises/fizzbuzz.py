"""
Given a number n, print all the numbers from zero to n,
when a number i is divisible by 3 print Fizz, when number is divisible by 5 print Buzz, when divisible by both
3 and 5 print FizzBuzz
"""


def print_fizz_buzz(integer):
    for i in range(1, integer + 1):
        number_to_be_printed = ""
        if i % 3 == 0:
            number_to_be_printed += "Fizz"
        if i % 5 == 0:
            number_to_be_printed += "Buzz"
        if not number_to_be_printed:
            number_to_be_printed = i
        print(number_to_be_printed)


input_number = int(input())
print_fizz_buzz(input_number)
