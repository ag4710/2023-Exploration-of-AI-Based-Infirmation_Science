number = int(input("Input number : "))
count = 0

for i in range(2, number+1): # -2 loop
    if number % i == 0:
        count = count + 1

if count == 0:
    print(f'{number} is prime number!')
else:
    print(f'{number} is Not prime number.')
