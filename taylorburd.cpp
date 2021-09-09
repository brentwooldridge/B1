#include<iostream>
#include<cstdlib>
#include<cstdio>
#include <cmath>
using namespace std;

int main()

{
	
float x, TOL, y, sumi, power, term, sign;
int M, n	;
	

x = 1.5;

TOL = 10e-5;

M = 15;

n = 1;
y = x-1;
sumi = 0;
power = y;
term = y;
sign = -1;

while (n<=M)
    {
	sign = -sign;
    sumi = sumi+sign*term;
    power = power*y;
    term = power/(n+1);
    if (abs(term)<TOL)
       {
		cout<<n;
		}
    n = n+1;
	
	
}
	
	
}
