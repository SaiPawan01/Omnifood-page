n=int(input("enter the number : "))
i=1
for i in range(2,n):
    if n%i==0:
        print(f"{n} is not prime")
        break
else:
    print(f"{n} is prime")

fact=1
j=1
for j in range(1,n+1):
    fact=fact*j
else:
    print(f"factorial of {n} is {fact}")