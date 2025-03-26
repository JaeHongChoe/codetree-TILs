a, o, c = input().split()
a = int(a)
c = int(c)

if o == "/":
    print(a/c)
else:
    print(a,o,c,"=", end=' ')
    if o == "+":
        print(a+c)
    elif o == "-":
        print(a-c)
    elif o == "*":
        print(a*c)


# Please write your code here.