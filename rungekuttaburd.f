      PROGRAM RUNGEKUTTABURD
      
      
      
      INTEGER i, N;
      REAL a, b, alpha, ftw, h, t,K1,K2, K3,K4, omega;
      REAL ftw1, ftw2, ftw3;
      a = 0;
      b = 2.0;
      N = 10;
      alpha = 0.5;


      h = (b-a)/N;
      t = a;
      omega = alpha;
      i = 1;
      do while (i.le.N)

	ftw = omega - t**2 +1;
        K1 = h*ftw;
        ftw1 = omega +K1/2 - (t+h/2)**2 +1;
        K2 = h*ftw1;
        ftw2 = omega +K2/2 - (t+h/2)**2 +1;
        K3 = h*ftw2;
        ftw3 = omega +K3 - (t+h)**2 +1;
        K4 = h*ftw3;

        omega = omega +(K1 + 2*K2 + 2*K3 + K4)/6;
        t = a +i*h;
        i = i+1
      end do
      print*,omega;
      read(*,*)





      END PROGRAM RUNGEKUTTABURD
