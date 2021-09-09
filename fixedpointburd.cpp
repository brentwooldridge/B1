#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>

using namespace std;

int main()

{
int N0, i;
float p0, TOL, p, gp;

p0 = 1.5;
TOL = 10e-5;
N0 = 30;


i = 1;


   gp =  p0-(pow(p0,3)+4*pow(p0,2)-10)/(3*pow(p0,2)+8*p0);
while (i<=N0)
{

    p = gp;
    if (abs(p-p0)<TOL)
        {
		cout << p;
	}
    i++;
    p0 = p;
}
}
