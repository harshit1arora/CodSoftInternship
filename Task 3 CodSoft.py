#Created By - Harshit Arora
#Task 3 CODSOFT

#PASSWORD GENERATOR PROJECT

print("Welcome to the Password Generator!")
import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+[]|;:'\",.<>?/"

len_of_letters = int(input("Enter the desired length for the letters in password: "))
len_of_numbers = int(input("Enter the desired length for the numbers in password: "))
len_of_symbols = int(input("Enter the desired length for the symbols in password: "))

length = int(input("Enter the desired length for the password: "))

password_letters = [random.choice(letters) for _ in range(len_of_letters)]
password_numbers = [random.choice(numbers) for _ in range(len_of_numbers)]
password_symbols = [random.choice(symbols) for _ in range(len_of_symbols)]

password = password_letters + password_numbers + password_symbols
random.shuffle(password)
password = ''.join(password)


print(f"The Generated Password is: {password}")