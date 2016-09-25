number1_str=input ("Input the first integer number:  ")
number1_int=int(number1_str)
number2_str=input ("Input the second integer number:  ")
number2_int=int(number2_str)
if number1_int>number2_int:
    print (number1_int,"is bigger than", number2_int)
elif number1_int<number2_int:
    print (number1_int, "is smaler than", number2_int)
else:
    print (number1_int, "is equal to", number2_int)
