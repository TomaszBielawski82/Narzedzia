with open('./liczby.txt') as f:
    lines = f.read().splitlines()

def isPrime(string):
    num = int(string);
    for i in range(2, num):
        if (num % i == 0):
            return False;
    return True

for num in lines:
    if isPrime(num):
        print(num, "jest liczba pierwsza")
    else:
        print(num)