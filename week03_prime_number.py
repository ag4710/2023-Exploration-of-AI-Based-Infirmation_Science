number = int(input("Input number : "))
#count = 0
is_prime = True

for i in range(2, number): # -2 loop
    if number % i == 0:
        is_prime = False

if is_prime == 0:
    print(f'{number} is prime number!')
else:
    print(f'{number} is Not prime number.')
