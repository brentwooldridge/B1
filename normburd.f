      PROGRAM NORMBURD
      



      INTEGER n, i;
      REAL sumi, norm, x(2);
      x(1) = 3.0
      x(2) = 4.0

      i = 1;

      n = 2;

      sumi = 0;

      do while (i .le. n)

          	sumi = sumi + x(i)*x(i);
            i = i+1
      end do
      norm = sumi**0.5
      print*, norm
      read(*,*)

      
      END PROGRAM NORMBURD
