# datatypes_demo.py

num_int = 10
num_float = 3.5
text = "Python"
flag = True

print(num_int, type(num_int))
print(num_float, type(num_float))
print(text, type(text))
print(flag, type(flag))

print("Sum:", num_int + num_float)
print("Product:", num_int * num_float)

user_input = input("Enter a number: ")
try:
    print("Integer value:", int(user_input))
    print("Float value:", float(user_input))
except ValueError:
    print("Invalid input")

age = 20
print("Age is " + str(age))

value = 5
print(value, type(value))
value = "Now I am a string"
print(value, type(value))
