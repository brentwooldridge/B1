#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<complex>
#include<cmath>


using namespace std; 

int main()

{
typedef complex<double> dcmplx;
dcmplx p0(0.5,0.0);
dcmplx p1(-0.5,0.0);
dcmplx p2(0.0,0.0);
int N0, i;
float TOL;
TOL = 10e-5;
N0 = 8;





i = 3;
while (i<=N0)

{	
	dcmplx h1 = p1-p0;
	dcmplx h2 = p2-p1;
	dcmplx p00 = pow(p0,4);
	dcmplx p01 = pow(p0,3);
	dcmplx p02 = pow(p0,2);
	dcmplx p10 = pow(p1,4);
	dcmplx p11 = pow(p1,3);
	dcmplx p12 = pow(p1,2);
	dcmplx p20 = pow(p2,4);
	dcmplx p21 = pow(p2,3);
	dcmplx p22 = pow(p2,2);
	dcmplx fp0 = p00-3.0*p01+p02+p0+dcmplx(1.0,0.0);
	dcmplx fp1 = p10-3.0*p11+p12+p1+dcmplx(1.0,0.0);
	dcmplx fp2 = p20-3.0*p21+p22+p2+dcmplx(1.0,0.0);   
	dcmplx del1 = (fp1-fp0)/h1;
	dcmplx del2 = (fp2-fp1)/h2;
	dcmplx d = (del2 - del1)/(h2+h1);
    dcmplx b = del2+h2*d;
    dcmplx D = pow((pow(b,2)-4.0*fp2*d),0.5);
    dcmplx E;
    dcmplx l = b - D;
    dcmplx r = b + D;
    if (abs(l)<abs(r))
    {
         E = b+D;
    }
    else
    {
         E = b-D;
    }
    dcmplx h = -2.0*fp2/E;
    dcmplx p = p2 + h;  
    if (abs(h)<TOL)
    {
        cout << p;
    }
    p0 = p1;
    p1 = p2;
    p2 = p;
    h1 = p1 - p0;
    h2 = p2 - p1;
    del1 = (fp1-fp0)/h1;
    del2 = (fp2-fp1)/h2;
    d = (del2 - del1)/(h2 + h1);
    i = i+1;
	
	
	
	
}
	
	
	
}
