#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;

int main()
{

      int N0, i;
      float a,b,TOL, FA, FP,p;


      a = 1.0;
      b = 2.0;
      N0 = 15;
      TOL = 10e-4;
      i = 1;


      FA = pow(a,3)+4*pow(a,2)-10;
      while (i <= N0)
         {
		 p = a+(b-a)/2;
         FP = pow(p,3)+4*pow(p,2)-10;
         if (FP == 0 || (b-a)/2 < TOL) 
         {
		 
            cout << p;
    }
         i = i+1;

         if (FP*FA > 0 || (b-a)/2 < TOL) 
           {
			 a = p;
		}
          else
            {
			b = p;
		}
          
      }
      
}
    
      
