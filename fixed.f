      PROGRAM Fixed
      
      real p0, p, TOL
      INTEGER i, N0
      N0 = 10
      i = 1
      DO WHILE (i .LE. N0)
         p = (10/(4+p0))**0.5
         IF (abs(p-p0) < TOL) THEN
            PRINT*, p
         END IF
        i = i+1
        p0 = p
      END DO
      
      PRINT*, p
      READ*, w
      END PROGRAM

