#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;

int main()

{
	double p0, TOL, p, a, b;
	int i, N0;
	a = 1;
	b = 2;
	TOL = 10^-4;
	i = 1;
	N0 = 10;
	p0 = 1.5;
	while (i <= N0)
	
	{
		p = pow(10/(4+p0), 0.5);
		
		if(abs(p-p0) < TOL)
			cout << p;
		i++;		
		p0 = p;
		
	}
	cout << p0;
	
	
}
