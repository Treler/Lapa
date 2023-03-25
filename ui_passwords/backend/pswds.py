from random import choice
import string

res = string.ascii_lowercase
count = 5
length = 45

# sym = input("Use symbols?(y/n)")
# LET = input("Use letter case?(y/n)")
# nums = input("Use numbers?(y/n)")

sym = 'y'
LET = 'y'
nums = 'y'

if sym == "y":
    res += string.punctuation
if nums == "y":
    res += string.digits
if LET == "y":
    res += string.ascii_uppercase


for i in range(count):
    passw = "".join(choice(res) for j in range(length))
    print(passw)
