N = int(input())

for i in range(1, int(N**(1/3)) + 1000):
    if N % i == 0:
        j = N //i
        if i > j:
            break
        
        y = (-3*i+(9*i**2-12*(i**2-j))**0.5)/6
        
        if y.is_integer() and int(y) != 0:
            y = int(y)
            x = y+i
            print(x, y)

            exit()
            
print(-1)
