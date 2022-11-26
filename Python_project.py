def ispalindrome(number):
    x=number
    reverse=0
    while(x!=0):
        digit=x%10
        reverse=reverse*10+digit
        x=x//10
    if number==reverse:
        return True
    else:
        return False
def isprime(num):
    y=True
    for i in range(2,num):
        if(num%i==0):
            y= False
            break
    return y
n=int(input("Enter the value of n:"))
primeAndPalindrome=[]
p=10**n
for j in range (2,p):
    if ispalindrome(j) and isprime(j):
        primeAndPalindrome.append(j)
    if len(primeAndPalindrome)==n+10:
        break
print(f'{n}th Prime Palindrome number is {primeAndPalindrome[n-1]}')