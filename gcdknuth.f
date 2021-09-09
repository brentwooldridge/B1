      PROGRAM GCDKNUTH
      

      integer m,n,r;
      m = 6099;
      n = 2166;
      r = mod(m,n);
      if (r.eq.0) then
          print*,n;
      else

          do while (r.gt.0)
             r = mod(m,n);
             m = n;
             n = r;

          end do

      end if
      PRINT*,m;
      read(*,*)
      END PROGRAM GCDKNUTH
