import numpy as np

inf = float('inf')
def Memorized_MC(p):
    n = len(p) - 1
    m = np.asarray([[inf]*n]*n)
    s = np.asarray([[inf]*n]*n)
    return lookup_chain1(m,p,0,n-1,s)

def lookup_chain(m,p,i,j,s):
    if m[i][j] < inf:
        return m[i][j], s
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i,j):
            q = lookup_chain(m,p,i,k,s)[0] + lookup_chain(m,p,k+1,j,s)[0] + p[i]*p[k+1]*p[j+1]
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = k
    return m[i][j],s


def lookup_chain1(m,p,i,j,s):
    if m[i][j] < inf:
        return (m, s)
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i,j):
            q = lookup_chain1(m,p,i,k,s)[0][i][k] + lookup_chain1(m,p,k+1,j,s)[0][k+1][j] + p[i]*p[k+1]*p[j+1]
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = k
    return (m,s)



p = [30,35,15,5,10,20,25]

(m,s)= Memorized_MC(p)
print('m =', m,'\n', 's=', s)