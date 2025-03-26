a, o, c = input().split()
a = int(a)
c = int(c)

if o == "/":
    print(a,o,c,"=", int(a/c))
elif o == "+":
    print(a,o,c,"=", a+c)
elif o == "-":
    print(a,o,c,"=", a-c)
elif o == "*":
    print(a,o,c,"=", a*c)
else:
    print(False)


# Please write your code here.