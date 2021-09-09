#include<iostream>
#include<cstdlib>
#include<cstdio>

using namespace std;

int main()

{
	double a, b, TOL, FA, FP, p;
	int N0, i;
	TOL = 10^-4;
	N0 = 13;
	i = 1;
	a = 1;
	b = 2;
	FA = a*a*a + 4*a*a -10;
	while(i<=N0)
	
	{
		p = a + (b-a)/2;
			FP = p*p*p + 4*p*p -10;
		
		if(FP == 0 || (b-a)/2 < TOL)
		{cout << p;
		}
		
		i++;
		
		if(FA*FP > 0)
		
		{
			a = p;
			FA = FP;
		}
		else
		{b = p;}
		
		}
		cout << p;
	}
	
	
	
	
	
	
	

