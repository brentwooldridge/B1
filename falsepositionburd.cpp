#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;

int main()

{
	
int i, N0;
float p0, p1, q0, q1, fp0, fp1, fp,TOL,p,q;
p0 = 0.5;
p1 = 3.14/4;
TOL = 10e-5;
N0 = 10;

i = 2;


fp0 = cos(p0)-p0;
fp1 = cos(p1)-p1;   
q0 = fp0;
q1 = fp1;

while (i<=N0)
{
    p = p1-q1*(p1-p0)/(q1-q0);
    if (abs(p-p1)<TOL)
        cout<<p;
    i++;
    fp = cos(p)-p;
    q = fp;
    if (q*q1<0)
    {
        p0 = p1;
        q0 = q1;
    }
    p1 = p;
    q1 = q;
	
	
}
	
	
	
	
	
}
