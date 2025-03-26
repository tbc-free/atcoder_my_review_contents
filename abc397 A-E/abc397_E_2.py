from collections import deque
N, K = map(int, input().split())

tdp = [1]*(N*K)
adjacent = [[] for _ in range(N*K)]

for i in range(N*K-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adjacent[u].append(v)
    adjacent[v].append(u)
    
st = deque()
st.append((0, -1, 0))
# now, parent, flag
    
while st:
    node, parent, flag = st.pop()
    
    if flag == 0:
        st.append((node, parent, 1))
        
        for child in adjacent[node]:
            if parent == child:
                continue
            st.append((child, node, 0))
    else:
        tmp = tdp[node]
        count = 0
        
        for child in adjacent[node]:
            if parent == child:
                continue
            
            if tdp[child] != 0:
                tmp += tdp[child]
                count += 1
            
        if tmp > K or count > 2:
            print("No")
            exit()
        elif tmp < K and count == 2:
            print("No")
            exit()
        elif tmp == K:
            tdp[node] = 0
        else:
            tdp[node] = tmp
            
if tdp[0] == 0:    
    print("Yes")
else:
    print("No")
