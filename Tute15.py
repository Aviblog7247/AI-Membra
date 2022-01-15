print("Enter any no.")
num1=input()
print("enter any second no.")
num2=input()
try:
    print("addition of two no.",int(num1)+int(num2))
except Exception as e:
    print(e)
print("this is a very important line")