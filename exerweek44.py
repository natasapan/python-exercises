input = raw_input
s_str = input("wright a word:    ")
t_str = s_str[::-1]
sum_str=" "
for i in t_str:
    sum_str = sum_str + i
print (sum_str)
