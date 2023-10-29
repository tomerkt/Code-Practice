def add(num1, num2):
    return num1 + num2
def substract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2


operations  = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for symbol in operations:
    print(symbol)
operations_sysmbol = input("Enter the operation: ")

calculate = operations[operations_sysmbol]

answer = calculate(num1, num2)

print(f"{num1} {operations_sysmbol} {num2} = {answer}")