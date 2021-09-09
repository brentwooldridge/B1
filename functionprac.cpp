#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<iomanip>

using namespace std;

double x = 2.0;
double a[2] = {};
double square(double x)
{
	return x*x;
}
double cube(double x)
{
	return x*x*x;
}

int main()
{
	a[0] = square(x);
	a[1] = cube(x);
	cout << a[0] << setw(2);
	cout << a[1];
	
	
}
