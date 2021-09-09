#include<stdio.h>
#include<iostream>
#include<iomanip>

main ()
{
	
	int x=0;
	#pragma omp parallel for
	for ( int i=0; i<=10; i++)
	{
	
		x = x+i;
		
	}
	
	std::cout << x;	
	
	
	
	
	
	
	
}
