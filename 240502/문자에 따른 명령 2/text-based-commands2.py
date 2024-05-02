dx, dy = [1,0,-1,0], [0,-1,0,1]
x,y =0,0
a = input()
dir_num =3
for k in range(len(a)):
    if a[k] in 'F':
        x += dx[dir_num]
        y += dy[dir_num]
    elif a[k] in 'L':
        dir_num = (dir_num-1)%4
    else:
        dir_num = (dir_num+1) %4
        
print(x,y)