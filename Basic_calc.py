def add(*numbers):
    total = 0
    for number in numbers:
        result += number
    return total

def subtract(*numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    return result

def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def divide(*numbers):
    if not numbers:
        return 0
    result = numbers[0]
    for number in numbers[1:]:
        if number != 0:
            result /= number
        else:
            return "Cannot divide by zero!"
    return result

def calculate():
    operation = input("Enter operation (add / subtract / multiply / divide): ")
    nums = input("Enter numbers separated by space: ")
    
number_list = [float(num) for num in nums.split()]

    if operation == "add":
        return add(*number_list)
    elif operation == "subtract":
        return subtract(*number_list)
    elif operation == "multiply":
        return multiply(*number_list)
    elif operation == "divide":
        return divide(*number_list)
    else:
        return "Invalid operation."

result = calculate()
print("Result: ", result)
