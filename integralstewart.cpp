      #include<iostream>
      #include<cstdlib>
      #include<cstdio>
      #include<cmath>
      using namespace std;
      
      int main()
      {
	  
      double  a, b, fti, dx, ti, y, z;
      int i, n;
      a = -1.0;
      b = 2.0;
      n = 600;
      i = 1;

      dx = (b-a)/n;
      z = 0;

      for(int i=1; i<=n; i++)
      {
         ti = a + (i)*dx;
         y = (1+pow(ti,2))*dx;
         z = z + y;

         
     }
 
	   cout << z;     
  }
      
   

