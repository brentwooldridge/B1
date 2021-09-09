#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>

using namespace std;

int main()
{
	int i, n ;
	float a,b,h,fa,fb,XI0,XI1,XI2,X,fX,XI;
	a = 0.0;
	b = 3*M_PI/8;
	n = 8;

	h =(b-a)/n;

    fa = tan(a);
    fb = tan(b);
	XI0 = fa + fb;
	XI1 = 0;
	XI2 = 0;
	
	for (i = 0; i<n; i++)
	{
    	X = a+i*h;
    	fX = tan(X);
    	if (i%2 == 0)
        	{
			XI2 = XI2 + fX;
			}
   	 	else{
        	XI1 = XI1 + fX;
        	}
	}
XI = h*(XI0 + 2*XI2 + 4*XI1)/3;

cout << XI;
}


