      PROGRAM EULER
      

      INTEGER N, i;
      REAL a, b, alpha, omega, fty, h, t;

      a = 0.0;
      b = 2;
      N = 10;
      alpha = 0.5;
      h = (b-a)/N;
      t = a;
      omega = alpha;
      PRINT*, t,omega;

      i = 1
      do while (i< N+1)
          fty = omega-t**2+1.0;
          omega = omega +h*fty;
          t = a +i*h;
          i = i+1;
          PRINT*, t,omega;
      end do
      read(*,*);







      END PROGRAM EULER
