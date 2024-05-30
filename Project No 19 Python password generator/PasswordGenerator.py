import random 
chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+"
length=int(input("enter length:"))
password =""
for a in range(length):
    password+=random.choice(chars)
print(password)