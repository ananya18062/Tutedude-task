num=int(input("Enter a number:"))
def factorial(a):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

print("Factorial of the", num ,"is:",factorial(num))

