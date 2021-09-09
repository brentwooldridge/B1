      PROGRAM TAYLORBURD
      
      REAL x, TOL, y, sumi, power, term, sign
      INTEGER M, n
      x = 1.5

      TOL = 10e-5

      M = 15

      n = 1
      y = x-1
      sumi = 0
      power = y
      term = y
      sign = -1

      do while (n.le.M)
         sign = -sign
         sumi = sumi+sign*term
         power = power*y
         term = power/(n+1)
         if (abs(term)<TOL)  then
             print*,n
         end if
         n = n+1
      end do
      
      read(*,*)
      
      
      END PROGRAM TAYLORBURD
