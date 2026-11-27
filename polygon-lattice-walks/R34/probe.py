from fractions import Fraction as F
from itertools import product


def costs(p,s,f,c,L):
    e=(p*s,p*(1-s)); n=((1-p)*f,(1-p)*(1-f))
    # Each action is chosen after observing its signal, before the deadline.
    costs=[sum(c*(e[i]+n[i]) if a[i] else L*e[i] for i in range(2))
           for a in product((0,1),repeat=2)]
    formula=sum(min(c*(e[i]+n[i]),L*e[i]) for i in range(2))
    assert min(costs)==formula<=min(c,p*L)
    robust=[a for a in product((0,1),repeat=2)
            if all(a[i] or not e[i] for i in range(2))]
    if 0<p<1 and 0<s<1: assert robust==[(1,1)]
    return formula


def main():
    grid=[F(i,10) for i in range(11)]
    count=0
    for p,s,f,c in product(grid,repeat=4):
        costs(p,s,f,c,F(1));count+=1
    print('exact binary decision cases:',count)
    p,s,f,c,L=F(1,5),F(4,5),F(1,5),F(2),F(10)
    assert costs(p,s,f,c,L)==F(26,25)
    print('baseline:',min(c,p*L),'early noisy:',costs(p,s,f,c,L),'saving:',F(24,25))
    print('miss probability under positive-only preparation:',p*(1-s))
    # Repeated copies of one signal are perfectly dependent, not independent.
    posterior=p*s/(p*s+(1-p)*f)
    false_independence=p*s**5/(p*s**5+(1-p)*f**5)
    assert posterior==F(1,2) and false_independence==F(256,257)
    print('five copies: correct posterior',posterior,'false independence posterior',false_independence)
    print('all exact assertions passed')

if __name__=='__main__':main()
