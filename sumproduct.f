      program sumproduct
	   
          integer n,i,x
          character y
           

           PRINT*, 'n='
           READ(*,*) n
           PRINT*, 'Sum or Product'
           READ(*,*), y
      if (y == 'sum' .or. y == 'Sum') then
               x=0

      else if (y=='product' .or. y=='Product') then
          x=1

      end if
      WRITE(*,*)'x=', x
	  pause
      end program sumproduct
