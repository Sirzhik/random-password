from colorama import Fore
from random import randint
print(Fore.GREEN + 'random password')
name = input("file name: ")
file = open(name, "w")
sym = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sym1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
password = sym[randint(0, 25)] + num[randint(0, 9)] + sym[randint(0, 25)] + sym1[randint(0, 25)] + sym[randint(0, 25)] + sym[randint(0, 25)] + num[randint(0, 9)] + sym1[randint(0, 25)]
print(password)
print('Your password: /usr/bin/' + name)
file.write(password)
file.close()

