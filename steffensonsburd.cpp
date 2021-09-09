#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>

using namespace std;

int main()

{
	int i, N0;
	float p0, gp0, p1, gp1, p2, p, TOL;
	
	p0 = 1.5;
	TOL = 10e-5;
	N0 = 25;

	i = 1;

    
    
while (i<=N0)
{
	gp0=pow((10/(p0+4)),0.5);
    p1 = gp0;
    gp1=pow((10/(p1+4)),0.5);
    p2 = gp1;
    p  = p0-pow((p1-p0),2)/(p2-2*p1+p0);
    if (abs(p-p0)<TOL)
    {
        cout << p;
    }
	i++;
    p0 = p;
//    cout << p0;
}
	
	
	
	
	
	
	
	
	
}
