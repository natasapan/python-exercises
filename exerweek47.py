input = raw_input
s_str = input("Wright a word with more than 4 characters:    ")
t_str = s_str[:2]
r_str = s_str[-2:]
i_str = t_str + r_str
if len(s_str) < 4:
    print ("The word has less than 4 characters")
else:
    print (i_str)
