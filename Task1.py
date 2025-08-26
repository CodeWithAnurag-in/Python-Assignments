user_inp = int(input("Enter a number: "))

def fact_num():
    n = user_inp
    fact = 1
    for i in range (1,n+1):
        fact *= i
    print("The factorial of 5 is ", fact)
               
fact_num()