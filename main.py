from cal import add,mul,sub,div
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
c = ["+","-","*","/"]
# print(f"Enter Selection {*c}")
print(*c)
d = input("Waiting for Cal Selection")
for i in range(len(c)):
    if d==c[0]:
        print(add(a,b))
        exit()
    elif d==c[1]:
        print(sub(a,b))
        exit()
    elif d==c[2]:
        print(mul(a,b))
        exit()
    elif d==c[3]:
        print(div(a,b))
        exit()
    else:
        # print(f"Select from {*c}")2
        
        print("s")