def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+':add,
    '-': subtract,
    '*':multiply,'/':divide
}

is_running = True
while is_running:
    print('<<<<<<< * | * Calculator * | * >>>>>>>')
    num1 = int(input('Enter first digit'))

    operand=''
    invalid_input = True
    while invalid_input:
        for x in operations:
            print(x)
        operand = input('Pick operand')
        if operand not in operations:
            print(f'Invalid operand - {operand}')
        else:
            invalid_input = False

    num2 = int(input('Enter second digit'))
    result = operations[operand](num1, num2)
    print(f'{num1} {operand} {num2} = {result}')



