print("Jarl. Day 1. The journey to the USA has begun.")
name = input("Hi, my name is Arslan, whats your name? ")
print("Nice to meet you, " + name + "!")
age = input("How old are you? ")
usa_age = int(age) + 4
print("When you finish college, you will be " + str(usa_age) + " years old!")
if usa_age < 21:
    print("Note: You can't buy beer there yet, but you can code hard!")
else:
    print("Welcome to the US, you are fully adult there!")