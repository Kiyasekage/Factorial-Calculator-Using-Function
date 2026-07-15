def factor(number):
    if number==0:
        print("The factorial of 0 is 1")
        quit()
    total = 1
    for numbers in range(1,number+1):
        total*=numbers
    return total
print("Welcome to counting factorial!")
ans = int(input("Please input your number : "))
print(f"The factorial of  {ans} is {factor(ans)}")
print("Thankyou for using our program!")
        
