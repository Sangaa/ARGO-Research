#include <bits/stdc++.h>
using namespace std;
uint64_t rot(uint64_t x,int m){return ((x<<1)&((1ULL<<m)-1))|(x>>(m-1));}
uint64_t canon(uint64_t x,int m){uint64_t y=0; for(int i=0;i<m;i++)if(x>>i&1)y|=1ULL<<(m-1-i);uint64_t z=x;for(int i=0;i<m;i++){z=min({z,x,y});x=rot(x,m);y=rot(y,m);}return z;}
int main(){for(int m=6;m<=26;m+=2){uint64_t mask=(1ULL<<m)-1; int k=m/2; uint64_t x=(1ULL<<k)-1;long long tests=0;vector<array<int,3>> ts;for(int a=1;a<=m/2;a++)for(int b=a;b<=m/2;b++)for(int c=b;c<=m/2;c++)if(a+b==c||a+b+c==m)ts.push_back({a,b,c});while(x<=mask){uint64_t y=mask^x;if(x<y&&canon(x,m)==x&&canon(y,m)!=x){tests++;bool good=true;for(auto [a,b,c]:ts){int j=a+b==c?c:m-b;int n=0,l=0;for(int t=0;t<m;t++){uint64_t z=(1ULL<<t)|(1ULL<<((t+a)%m))|(1ULL<<((t+j)%m));n+=(x&z)==z;l+=(y&z)==z; // add reflected triangles too
z=(1ULL<<t)|(1ULL<<((t+m-a)%m))|(1ULL<<((t+m-j)%m));n+=(x&z)==z;l+=(y&z)==z;}
if(n!=l){good=false;break;}}if(good){cout<<"found "<<m<<" "<<tests<<" "<<x<<" "<<y<<endl;return 0;}}uint64_t u=x&-x,v=x+u;x=v+(((v^x)/u)>>2);}cout<<m<<" "<<tests<<endl;}}
