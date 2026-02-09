def fib (n):
    if n < 2:
        return n
    else:
        return(fib(n-1)+fib(n-2))
num = int(input("enter the number:"))
if num < 0:
    print("number is invalid")
else:
    print("number is fibanocci:", fib(num))
for i in range (num):
    print(fib(i), end= "")
