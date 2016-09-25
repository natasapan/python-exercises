number1_str=input("Input the first number:  ")
number1_int=int(number1_str)
number2_str=input("Input the second number:  ")
number2_int=int(number2_str)
number3_str=input("Input the third number:  ")
number3_int=int(number3_str)
if number1_int>number2_int and number1_int>number3_int:
    print (number1_int,"is the largest")
elif number2_int>number1_int and number2_int>number3_int:
    print (number2_int,"is the largest")
else:
    print (number3_int,"is the largest")
