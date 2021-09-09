#include<iostream>
#include<cstdlib>
#include<cstdio>

using namespace std;

int main()

{
	
int n, j;
float x0,x,y,z;

n = 3;
float a[] = {1.0,0.0,0.0,-2.0};
x0 = 0.0;

y = 1;
z = 1;
j = 0;
while (j <= n-1)
{
    y = x0*y + a[j];
    z = x0*z + y;
    j++;
}
y = x0*y+ a[n];
cout << y;

cout << z;
	
	
}
	
	
	
	
	
	

