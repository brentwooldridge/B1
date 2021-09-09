#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<math.h>
using namespace std;

int main()

{
	
	
int N0, i;
float p0, p1, TOL, q0, q1, fp0, fp1, fp,p;
N0 = 10;
p0 = 0.5;
p1 = 3.14/4;
TOL = 10e-5;
i = 2;

fp0 = cos(p0)-p0;
fp1 = cos(p1)-p1;
q0 = fp0;
q1 = fp1;
while (i<=N0)
{
    p = p1-q1*(p1-p0)/(q1-q0);
    if (abs(p-p1)<TOL)
    {
        cout<<p;
  	}
    i = i+1;
    p0 = p1;
    q0 = q1;
    p1 = p;
    fp = cos(p)-p;
    q1 = fp;
    
	
}
	
	
	
}
