#include<iostream>
#include<cstdlib>
#include<cstdio>

using namespace std;

fibn (int n)
{	
	return 0;	
}
fibn1 (int n)
{	
	return 1;	
}		
fibn2 (int n)
{	
	return fibn(n)+fibn1(n);	
}	
int main()
{
	int n,x,z,y;
	n = 1;
	if (n == 0)
	{
		x = fibn(n);
		cout << x;
	
		if (n == 1)
	{
		y = fibn1(n);
		cout << y;
	}
		
	if (n>1)
	
		z = fibn2(n);
		cout << z;
	}
	
	
}









	
	
	

