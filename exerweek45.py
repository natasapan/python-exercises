input = raw_input
s_str = input("wright a word:    ")
sum_str = " "
for b in s_str:
    x = ord(b) + 1
    y = chr(x)
    sum_str = sum_str + y
print (sum_str)



