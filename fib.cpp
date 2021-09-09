#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<iomanip>

	int fib(int n)
	{
	int x;
	n=12;
	
	if (n=0)
	{
		std::cout<<n;
	}
	else if(n=1)
	{
		std::cout<<n;
	}
	else if(n>1)
	{
		x=fib(n-1)+fib(n-2);
	}
}
