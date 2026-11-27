from fractions import Fraction as F
from itertools import combinations, product


def scatter(a):
    n=len(a)
    u=[tuple(F(p[i])-F(sum(q[i] for q in a),n) for i in range(2)) for p in a]
    return tuple(sum(p[i]*p[j] for p in u) for i,j in ((0,0),(0,1),(1,1)))


def det(s):
    a,b,c=s
    return a*c-b*b


def area2(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def main():
    grid=list(product(range(-1,2),repeat=2)); tests=0
    for n in range(3,7):
        for a in combinations(grid,n):
            s=scatter(a); D=det(s); T=s[0]+s[2]
            assert n*D==sum(area2(*t)**2 for t in combinations(a,3))
            assert 4*D<=T*T
            if D:assert T/(4*D)>=1/T
            tests+=1
    print('grid subset area and trace checks:',tests)
    print('h individual worst variance / sigma^2 ; combined worst variance / sigma^2')
    for k in range(1,13):
        h=F(1,2**k)
        a=((-1,0),(1,0),(0,h)); b=((0,-1),(0,1),(h,0))
        s,t=scatter(a),scatter(b)
        assert s==(2,0,2*h*h/3) and t==(2*h*h/3,0,2)
        z=tuple(x+y for x,y in zip(s,t)); assert z[0]==z[2] and z[1]==0
        print(h,3/(8*h*h),1/(4*z[0]))
    # Reusing one noisy anchor reading induces correlations between contrasts.
    # For anchors at (0,0),(1,0),(0,1), errors dx=(e0-e1)/2, dy=(e0-e2)/2.
    errs=[(F(e[0]-e[1],2),F(e[0]-e[2],2)) for e in product((-1,1),repeat=3)]
    cov=tuple(sum(p[i]*p[j] for p in errs)/8 for i,j in ((0,0),(0,1),(1,1)))
    assert cov==(F(1,2),F(1,4),F(1,2))
    print('shared-reading covariance / sigma^2:',cov)
    print('all exact assertions passed')

if __name__=='__main__':main()
