
def factorial_num(n):
   if n==0 or n==1:
     return 1
   else:
     return n*factorial_num(n-1)

number =int(input("Enter the value:"))
ANS= factorial_num(number)

print("The factorial of {} is {}.".format(number,ANS))
