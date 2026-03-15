def factorial(n):
    numbers = []
    result = 1

    while n > 0:
        numbers.append(n)
        n = n - 1
    
    for i in numbers:
        result = result * i
    
    return result

print(factorial(8))