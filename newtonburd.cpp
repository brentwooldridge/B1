#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>

using namespace std;

int main()
{

int N0, i;
float p0, TOL, fp0, fpp0,p ;
	p0 = 2.0;
	TOL = 10e-5;
	N0 = 10;
	i = 1;





	while  (i<=N0)
	{
		fp0 = pow(p0,2)-2;

		fpp0 = 2*p0;
	    p = p0-fp0/fpp0;
    
	    if (abs(p-p0)<TOL)
	    {
		    cout << p;
		}
	    i++;
	    p0 = p;
	 	
	}
    
}
