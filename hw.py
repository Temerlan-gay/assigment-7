def is_prime(n:int)->bool:
    if n<2:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False
    return True
def nth_fibonacci(n:int)->int:
    a,b=0,1
    for _ in range(n-1):a,b=b,a+b
    return a
def factorial(n:int)->int:
    r=1
    for i in range(1,n+1):r*=i
    return r
def count_vowels(s:str)->int:
    v="aeiou";c=0
    for x in s.lower():
        if x in v:c+=1
    return c
def sum_of_digits(n:int)->int:
    s=0
    for d in str(abs(n)):s+=int(d)
    return s
def reverse_string(s:str)->str:
    return s[::-1]
def sum_of_squares(n:int)->int:
    s=0
    for i in range(1,n+1):s+=i*i
    return s
def collatz_sequence_length(n:int)->int:
    c=1
    while n!=1:
        if n%2==0:n//=2
        else:n=n*3+1
        c+=1
    return c
def is_leap_year(y:int)->bool:
    return (y%4==0 and y%100!=0) or (y%400==0)
def count_words(s:str)->int:
    return len(s.split()) if s else 0
def is_palindrome(s:str)->bool:
    return s==s[::-1]
def sum_of_multiples(n:int,x:int,y:int)->int:
    s=0
    for i in range(1,n+1):
        if i%x==0 or i%y==0:s+=i
    return s
def gcd(a:int,b:int)->int:
    while b:a,b=b,a%b
    return abs(a)
def lcm(a:int,b:int)->int:
    if a==0 or b==0:return 0
    return abs(a*b)//gcd(a,b)
def count_characters(s:str,c:str)->int:
    k=0
    for x in s:
        if x==c:k+=1
    return k
def digit_count(n:int)->int:
    return len(str(abs(n)))
def is_power_of_two(n:int)->bool:
    return n>0 and (n&(n-1))==0
def sum_of_cubes(n:int)->int:
    s=0
    for i in range(1,n+1):s+=i**3
    return s
def is_perfect_square(n:int)->bool:
    if n<0:return False
    x=int(n**0.5)
    return x*x==n
def is_armstrong_number(n:int)->bool:
    s=str(n);p=len(s);r=0
    for d in s:r+=int(d)**p
    return r==n