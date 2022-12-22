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

#Problem2
z=""" \n
      Hey, {My_Name} Here! \n
      My SID is {Sid}\n
      I am from {department_name} and my CGPA is {cgpa}"""
My_Name="Arnav Thakur"
Sid="22105028"
department_Name="ECE"
print(z.format(My_Name="Arnav Thakur", Sid=22105028, department_name="ECE", cgpa=9.9 ))

#Problem3
a=56
b=10
print(a & b)
print(a | b)
print(a ^ b)
print("left shift a by 2:-", a << 2)
print("left shift b by 2:-", b << 2)
print("right shift a  by 2:-", a >> 2)
print("right shift b  by 4:-", b>>4)

#Problem 4
m=float(input("Enter the first number: "))
n=float(input("Enter the second number: "))
o=float(input("Enter the third number: "))
print("the greatest of the three numbers is ", max(m,n,o))

#Problem5
Sentence= input("Enter a string:")
if "name" in Sentence:
    print("Yes")    
else:
    print("No")      

#Problem 6
s1 = float(input("Enter the length of side 1: "))
s2 = float(input("Enter the length of side 2: "))
s3 = float(input("Enter the length of side 3: "))
if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print("Yes")
else:
    print("No")

























