def count_substrings(s:str,sub:str)->int:
    c=0;i=0
    while i<=len(s)-len(sub):
        if s[i:i+len(sub)]==sub:c+=1;i+=len(sub)
        else:i+=1
    return c
def find_smallest_divisor(n:int)->int:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return i
    return n
def check_divisible_by_any(n:int,d:str)->bool:
    for x in d.split():
        if n%int(x)==0:return True
    return False
def find_nth_root(x:float,n:int)->float:
    return round(x**(1/n),3)
def collatz_sequence_length(n:int)->int:
    c=0
    while n!=1:
        if n%2==0:n//=2
        else:n=n*3+1
        c+=1
    return c