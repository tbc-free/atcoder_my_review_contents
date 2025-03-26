import sys
sys.setrecursionlimit(2*10**6)
N, K = map(int, input().split())

adjacent = [[] for _ in range(N*K)]

for i in range(N*K-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adjacent[u].append(v)
    adjacent[v].append(u)
    
def dfs(node, parent):
    tmp = 1
    count = 0
    
    for child in adjacent[node]:
        if parent == child:
            continue
        
        num = dfs(child, node)
        
        if num != 0:
            tmp += num
            count += 1
            if count > 2:
                break
    
    if tmp > K or count > 2:
        print("No")
        exit()
    elif tmp < K and count == 2:
        print("No")
        exit()
    elif tmp == K:
        return 0
    else:
        return tmp



if dfs(0, -1) == 0:
    print("Yes")
else:
    print("No")
