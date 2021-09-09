      program bisection
	  
	  real p, function f(a,b)
	  
	  f=p^2
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	  subroutine bisection(a,b)
	  integer N0, i
	   real a, b, TOL
	   i=1
		FA=f(a)
	   
	   WHILE i<=1
		p=a+(b-a)/2;
		FP=f(p)
	   if FP=0 .OR. (b-a)/2<TOL
		WRITE(*,*) 'p=' , p
		i=i+i
	   if FA*FP>0 
		FA=FP
	   else if 
	   b=p