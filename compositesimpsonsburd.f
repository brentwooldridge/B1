      PROGRAM COMPOSITESIMPSONBURD

      INTEGER i, n ;
      REAL a,b,h,fa,fb,XI0,XI1,XI2,X,fX,XI, pi;
      a = 0.0;
      pi = 4.*atan(1.)
      b = 3*pi/8;
      n = 8;

      h =(b-a)/n;

      fa = tan(a);
      fb = tan(b);
      XI0 = fa + fb;
      XI1 = 0;
      XI2 = 0;
      i = 1
      do while(i.lt.n)

    	X = a+i*h;
    	fX = tan(X);
    	if (mod(i,2) .EQ. 0) then
            XI2 = XI2 + fX;
        else
             XI1 = XI1 + fX;
        end if
        i = i+1
      end do

      XI = h*(XI0 + 2*XI2 + 4*XI1)/3;

      print*, XI;
      read(*,*)
      
      
      
      
      END PROGRAM COMPOSITESIMPSONBURD
