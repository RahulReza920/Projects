 
#Basic input,Output,Function with argument
#exponentiation operator,list,if..else
#For loop,while loop
#Try..Except,calender
#squareroot,temperature,muliplication table
#pythagorian,fibonacci,calender,armstong,factorial

playagain=True
while(playagain==True):

 def add(x,y):
       return x+y

 def subtract(x,y):
       return x-y
    
 def multiply(x,y):
       return x*y
   
 def divide(x,y):
       return x/y

 def sqr_root(x):
     return x**0.5

 def celcious_Fahrenhite(celsius):
     return (celsius*1.8)+32
 

 def Multiplication_table():
     num=int(input("Enter the number: "))
    
     for x in range(1,num+1):
        print(num, "X", x, "=", num*x)
        
        

 def factor(num):
    ls = []
    for i in range(1,num):
        if num % i == 0:
            ls.append(i)
    if len(ls) == 1:
        print(num," is a prime number")
    ls.append(num)
    print(ls)
    
 def Fibonacci_generator():
    
  nterms = int(input("How many terms? "))


  n1, n2 = 0, 1
  count = 0


  if nterms <= 0:
   print("Please enter a positive integer")
  elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
  else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
      
       n1 = n2
       n2 = nth
       count += 1

 def Pythagorian_triples():
    while True:
        try:
            side1 = int(input("Enter first side: ")) ** 2 #exponential operator
            side2 = int(input("Enter second side: ")) ** 2
            side3 = int(input("Enter third side: ")) ** 2
        except ValueError:
             print ("\nSorry that is not a number. \n")
        else :
             break
    
    triangle = [side1,side2,side3]
    hyp = max(triangle)
    triangle.remove(hyp)

    if sum(triangle) == hyp:
        print("You have a pythagorean triple.")
    else:
        print("You dont have a pythagorean triple.")


 def Calender_Making():
  import calendar



  yy = int(input("Enter year: "))
  mm = int(input("Enter month: "))
  print()
  print(calendar.month(yy, mm))
  
#407
 def Armstong_Checker():
  num = int(input("Enter a number: "))

  sum = 0

  temp = num
  while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

  if num == sum:
   print(num,"is an Armstrong number")
  else:
   print(num,"is not an Armstrong number")
   
 def Factorial():
    
  num =int(input("Enter the Number: "))
  factorial = 1

  if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
  elif num == 0:
   print("The factorial of 0 is 1")
  else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
   
   
   
 print()   
 print("Sir, please select Your desire operation from below : ")
 print()
 print("*******************************************")
 print("*******************************************")
 print("1.ADD TWO NUMBER")
 print("2.SUBTRACT TWO NUMBER")
 print("3.MULTIPLY TWO NUMBER")
 print("4.DIVIDE TWO NUMBER")
 print("5.SQUARE ROOT OF A GIVEN NUMBER")
 print("6.CELCIOUS TO FAHRENHITE CONVERTER")
 print("7.MULTIPLICATION TABLE GENERATOR")
 print("8.FACTORS GENERATOR AND PRIME CHECK")
 print("9.PYTHAGORIAN TRIPLES CHECKER")
 print("10.FIBONACCI SEQUENCE GENERATOR")
 print("11.CALENDER GENERATOR OF ANY MONTH" )
 print("12.ARMSTONG NUMBER CHECKER")
 print("13.FACTORIAL DETERMINATION")
 print("*******************************************")
 print("*******************************************")
    
 
 choice = input("Please Enter your choice(1/2/3/4/5/6/7/8/9/10/11/12/13):")
    
 if choice == '1':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1,"+",num2,"=", add(num1,num2))
        
 elif choice == '2':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1,"-",num2,"=", subtract(num1,num2))
        
 elif choice == '3':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1,"*",num2,"=", multiply(num1,num2))
        
 elif choice == '4':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1,"/",num2,"=", divide(num1,num2))
        
 elif choice == '5':
        num1 = float(input("Enter the number: "))
        print("Square Root of the number is:")
        print(sqr_root(num1))
    
 elif choice == '6':
        num1 = float(input("Enter temperature in celcious: "))
        print("Fahrenhite temperature is: ")
        print(celcious_Fahrenhite(num1))
        
 elif choice== '7':
    Multiplication_table()
    
 elif choice== '8':
    num = int(input("Enter a number to generate its factors: "))
    factor(num)
    
 elif choice== '9':
    Pythagorian_triples()
    
 elif choice=='10':
    Fibonacci_generator()
    
 elif choice== '11':
    Calender_Making()
    
 elif choice== '12':
    Armstong_Checker()
    
 elif choice== '13':
    Factorial()
    
    
    
 else:
       print("Invalid input")
       
       
 request=input("Would you like to play again? (Y/N) :").lower()
 if(request=='y'):
        playagain=True
        print("Play again")
 elif(request=='n'):
        playagain=False
        print("Exit The game")
 else:
        print("Enter Right input")
        
        