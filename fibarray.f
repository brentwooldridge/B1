      PROGRAM FIBARRAY
      
      INTEGER i, n
      INTEGER a(15)
      
      
      i = 3
      n=15
      
      a(1) = 1
      a(2) = 1
      
      do while(i.le.n)
          a(i) = a(i-1) + a(i-2)
          i = i+1
      end do
      print*,a
      read (*,*)
      END PROGRAM FIBARRAY
