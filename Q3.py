#Write a program to swap two variables.

# a, b = input("enter two variables:").split()
# print(a,b)
# temp1 = a
# temp2 = b
# a = temp2
# b = temp1
# print(a,b)


# method 2 

a, b = input("enter two variables ").split()
print("original values:",a,b)
# swap using tuple pakcking and unpacking

a,b = b,a

print("swapped values: ",a,b)