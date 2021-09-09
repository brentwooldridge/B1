# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 19:40:35 2015

@author: Brent
"""

 OPEN(UNIT=101,FILE='fort.101',STATUS='OLD')
      !
      do j=1,NEQ
      read(101,*) Y(j)
      write(103,45) Y(j)
      end do
      !
      do 65 i=1,NEQ
      YDOT(i) = 0.0
  65  continue
      !
  77  continue
      if (time.ge.durat) go to 88
      if(mod(ii,iii).ne.0) go to 6
     *      if(time.le.95000.0) go to 6
     *      write(6,44) time,Y(1),Y(2),Y(3),Y(4),Y(5),Y(6)
      write(11,44) time,Y(1),Icas,Icab,Inaca,Ipca,Ina,Inab,IR
      write(12,44) time,Y(1),Inak,Ikto,Ik1,Iks,Ikur,Ikr,Iclca
      write(13,44) time,Y(1),Y(2),Y(3),Y(4),Y(5),Y(6)
      write(14,44) time,Y(7),Y(8),Y(9),Y(10),Y(11),Y(12)
      write(15,44) time,Y(13),Y(14),Y(15),Y(16),Y(17),Y(18)
      write(16,44) time,Y(19),Y(20),Y(21),Y(22),Y(23),Y(24)
      write(17,44) time,Y(25),Y(26),Y(27),Y(28),Y(29),Y(30)
      write(18,44) time,Y(31),Y(32),Y(33),Y(34),Y(35),Y(36)
      write(19,44) time,Y(37),Y(38),Y(39),Y(40),Y(41),Y(42)
      write(10,44) time,Y(43),Y(44),Y(18)+Y(19)
      write(20,44) time,Y(1),Ikto+Iks+Ikur+Ikr,Ikur1,Ikur2,Ikur3,Iclca
      write(30,44) time,frel,fcal,fup,ftrpn,fnaca,fxfer,fleak,fcab,fpca
      write(31,44) time,Bi,Bss,Bjsr
      write(32,44) time,srel,scal,sup,strpn,snaca,sxfer,sleak,scab,spca
     6  continue
      ii = ii + 1

*
          DO I=1,NP
              IF((time.GE.STON(I)).AND.(time.LE.STOFF(I))) THEN
                  Istim = AMPL
                  IP = I
                  GO TO 78
              ELSE
                  Istim = 0.0
              END IF
          END DO
    78    CONTINUE
     if((time.ge.9020).and.(time.le.10020)) then
      srel  = srel+frel*dt
      scal  = scal+fcal*dt
      sup   = sup+fup*dt
      strpn = strpn+ftrpn*dt
      snaca = snaca+fnaca*dt
      sxfer = sxfer+fxfer*dt
      sleak = sleak+fleak*dt
      scab  = scab+fcab*dt
      spca  = spca+fpca*dt
        end if
      !
      go to 77
      !
  88  continue
      !
      !   Write new initial conditions
      !
      do j=1,NEQ
      write(102,45) Y(j)
      end do
      !
  44  format(f12.5,30e15.6)
  45  format(30e20.10)
     * END of Program
            stop
      end
      
        11  continue
      return
      end