C This Fortran program calculates the area
C of a triangle
      PRINT *, 'ENTER HEIGHT'
      READ *, H
      PRINT *, 'ENTER BASE: '
      READ *, B
      A = 0.5*H*B
      
C
C THe following demonstrates the use of a continuation line
C
      PRINT *,
     1      'AREA= ', A
      
C
C The above two lines are the same as PRINT *, 'AREA= ', A
C
      END
