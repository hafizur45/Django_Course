def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y==0:
        return "Error: division by zero is undefined"
    else:
        return x/y
def modulus(x,y):
    if y==0:
        return "Error: modulus by zero is undifined"
    else:
        return x%y

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")
print("Enter Choice:1/2/3/4/5")
choice = int(input())
if choice in [1,2,3,4,5]:
    try:
        num1 = float(input("Enter First Number"))
        num2 = float(input("Enter second number"))
    except ValueError:
        print("Error: please choose correct Number")
        
  
     
    if choice==1:
        print(f"{num1} + {num2} = {addition(num1,num2)}")
    elif choice==2:
         print(f"{num1} - {num2} = {subtraction(num1,num2)}")
    elif choice==3:
         print(f"{num1} * {num2} = {multiplication(num1,num2)}")
    elif choice==4:
         print(f"{num1} / {num2} = {division(num1,num2)}")
    elif choice==5:
         print(f"{num1} % {num2} = {modulus(num1,num2)}")
    else:
        print("Please choose correct option")
        
        
        
    
    