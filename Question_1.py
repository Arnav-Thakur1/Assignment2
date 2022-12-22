#Problem 1
input_str="Python is a case sensitive language"
print("a.",len(input_str))
print('b.',input_str[::-1])
new_str=input_str[11:-9]
print('c.',new_str)
x=input_str.replace("a case sensitive", "object oriented")
print(x)
print(input_str.index('a'))
y=input_str.replace(' ','')
print(y)