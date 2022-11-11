def factorial(number1, number2):
    fact = 1
    for result in range(number1, number2, -1):
        fact *= result
    return f"{fact:.2f}"


num1 = int(input())
num2 = int(input())
print(factorial(num1, num2))