def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return (fib(n-1)+fib(n-2))
    
n=int(input("Enter the length of the Fibnacci series : "))
print("The ",n,"Fibonacci numbers are : \n")
for i in range(n):
    print(fib(i),"\t")
