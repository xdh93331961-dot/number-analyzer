# number analyzer
def read_number():
    x=int(input("please input an number:"))
    return x

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
    if x<2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def factors(x):
    result=[]
    for i in range(1,x+1):
        if x%i==0:
            result.append(i)
    return result
def analyze_number(x):
    return{
        "digits":digits_num(x),
        "reverse":reverse_num(x),
        "sum":digits_sum(x),
        "prime":prime(x),
        "factors":factors(x)
    }
def print_results(ana):
    print(ana["digits"])
    print(ana["reverse"])
    print(ana["sum"])
    print(ana["prime"])
    print(*ana["factors"])
def main():
    print_results(analyze_number(read_number()))
if __name__=="__main__":
    main()
