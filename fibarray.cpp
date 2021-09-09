#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<iomanip>
using namespace std;

int main()

{
	int i, n;
	int a[7] ={};
	n = 7;
	a[1] = 1;
	a[2] = 1;
	for (i = 3; i <= n; i++)
	{
		a[i] = a[i-1]+a[i-2];
		
	}
	
	
	
	cout << setw(3) << a[i];
	
}
