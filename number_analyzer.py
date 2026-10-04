# number analyzer
def digits_num(x):
    return len(str(x))
def reverse_num(x):
    y=x
    z=0
    while y!=0:
        z+=(y%10)*(10**(len(str(y))-1))
        y//=10
    return z
def digits_sum(x):
    y=x
    z=0
    while y!=0:
        z+=y%10
        y//=10
    return z
def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def factors(x):
    for i in range(1,x+1):
        if x%i==0:
            print(i,end=" ")
    print()
print(digits_num(120))
print(reverse_num(120))
print(digits_sum(120))
print(prime(120))
factors(120)

