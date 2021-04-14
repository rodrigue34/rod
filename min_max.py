print("how many integers would you like to enter ")
num_integer = int(input())
print("enter num_integers")
big_numbers = 0
small_numbers = 10000
for numb in range(num_integer):
    kim = int(input())
    if kim > big_numbers:
        big_numbers = kim
    if kim < small_numbers:
        small_numbers = kim
print("small numbers" + str(small_numbers))
print("big numbers" + str(big_numbers))








