x=((1,0),(0,1)) # Inputs
b = (1,0)       # Expected Values
w = [1,2]       # Weights
q = -1          # threshold value
A = 0.5         # learning coefficient
net = [0,0]     # Sums
c = [1,-1]      # Output

notFinish = True
while notFinish:
    for n in range(len(net)):
        for i in range(len(x[n])):
            net[n]+=  w[i]*x[n][i]
        print(net[n])
        if net[n] > q:
            c[n] = 1
        elif net[n] <= q:
            c[n] = 0
        if n%len(net)==1:
            notFinish = False
            for s in range(len(c)):
                if c[s] != b[s]:
                    notFinish = True
                    continue
        if c[n] > b[n]:
            for i in range(len(w)):
                w[i] = w[i] - A*x[n][i]
                continue
        elif c[n] < b[n]:
            for i in range(len(w)):
                w[i] = w[i] + A*x[n][i]
                continue
        
print(str(w))
print(str(c))