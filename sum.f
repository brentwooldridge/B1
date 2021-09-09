      program sums
             
      IMPLICIT NONE
      integer x,n,i
      x=0
      PRINT *, 'n='
      READ(*,*) n
      do i=1,n
      x=x+i
      end do
      WRITE(*,*) 'x=', x
      READ(*,*)
      end program sums
      
                                                            
