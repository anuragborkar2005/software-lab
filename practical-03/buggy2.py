def is_even(n) :
    return n % 2 == 1

# wrong: this is the test for odd numbers

for n in [2, 3, 4, 7]:
    print (n, "is even:", is_even(n) )