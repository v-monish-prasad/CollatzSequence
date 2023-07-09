number = int(input())
print(number, end=" ")

while number != 1:
    if number % 2:
        number = 3 * number + 1
    else:
        number //= 2
    print(number, end=" ")
