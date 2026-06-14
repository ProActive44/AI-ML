#Python Fundamentals (Assignment1)

#1
# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print("Hello " + name + ", you are " + age + " years old!")

#2
# num1 = input("Enter number 1: ")
# num2 = input("Enter number 2: ")

# num1 = int(num1)
# num2 = int(num2)

# print(num1 + num2)
# print(abs(num1 - num2))
# print(num1 * num2)
# print(num1 / num2)

#3
# num_1 = input("Enter 1st integer: ")
# num_2 = input("Enter 2nd integer: ")
# num_3 = input("Enter a float number: ")

# num_1 = float(num_1)
# num_2 = float(num_2)
# num_3 = float(num_3)

# print((num_1 + num_2 + num_3) / 3)

#4
# num = input("Enter a number: ")
# num1 = int(num)
# num2 = float(num)
# num3 = str(num)
# print("Integer:" , num1 , type(num1))
# print("Float:" , num2 , type(num2))
# print("String:" , num3 , type(num3))

#5
# x = 10+3*2**2
# print(x)

#6
# num1 = input("Enter number 1: ")
# num2 = input("Enter number 2: ")

# num1, num2 = num2, num1

# print("Entered by user: num1:", num1, ", num2:", num2)


#7
# C_temp = input("Enter temperature in Celcius: ")

# F_temp = (float(C_temp) * (9/5)) + 32

# print("Temperature in Fahrenheit:", F_temp)

#8
# r = float(input("Enter the radius: "))
# pie = 3.14
# print("Area:", pie * r ** 2)

#9
# prin = float(input("Enter Principle amount: "))
# rate = float(input("Enter Rate: "))
# time = float(input("Enter Time: "))

# print((prin * rate * time)/ 100)

#10
dec = float(input("Enter a decimal number: "))

print("Integer Part:", int(dec))
print("Fraction part:", round(dec - int(dec), 2))