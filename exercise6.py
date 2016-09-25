input = raw_input
number_str = input("Input the first number:  ")
number1_int = int(number_str)
number_str = input("Input the second number:  ")
number2_int = int(number_str)
operation_str = input("Input an operation (+, -, *, /):  ")
if operation_str == '+':
    print (number1_int + number2_int)
elif operation_str == '-':
    print (number1_int - number2_int)
elif operation_str == '/':
    print (number1_int / number2_int)
elif operation_str == '*':
    print (number1_int * number2_int)
else:
    print("Not valid operation")

