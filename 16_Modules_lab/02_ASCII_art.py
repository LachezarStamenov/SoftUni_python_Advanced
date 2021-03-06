# Write a program that encrypts given words by using the characters: "-|_/\()" to structure the word. Use the pyfiglet
# module.
# Directions
# 1.	First you need to install the module that we will be using. To install it go to Setting --> Project
# <your_project_name> --> Project Interpreter --> + --> search for pyfiglet --> install package.
# 2.	Import the module
# 3.	Implement the logic. We will be using the figlet_format method
from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg):
    ascii_art = figlet_format(msg, font="isometric1")
    print(ascii_art)


message = input()
print_art(message)
print(colored(message, 'green'))
