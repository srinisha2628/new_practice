import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
def add(a,b):
    print("addition of two numbers is",a+b)

def sub(a,b):
    print("substarction os two numbers is",a-b)

def mul(a,b):
    print("multiplication of two numbers is",a*b)

def div(a,b):
    if(b==0):
        print("b value cannot be zero")
    else:
        print("division of two numbers is",a/b)
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)
