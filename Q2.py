# Write a program to find the sum of two numbers.

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))

# sum = num1 + num2

# print(sum)


#method2 - we can take two inputs at a same time using split method

num1, num2 = map(int, input("enter two numbers: ").split())
sum = num1 + num2
print(sum)
