# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 09:32:57 2015

@author: Brent
"""

STON = []
STOFF= []
for j in range  (0,len(np.linspace(0, tf, ts))): 
    STON=STON+[TINI+j*TPER]
    STOFF=STOFF+[TINI+j*TPER+TW]
    for i in range (0, len(np.linspace(0,tf, ts))):
        if(t[i]>=9020 and t[i])<=10020:
            srel  = srel+frel*(tf/ts)
            scal  = scal+fcal*(tf/ts)
            sup   = sup+fup*(tf/ts)
            strpn = strpn+ftrpn*(tf/ts)
            snaca = snaca+fnaca*(tf/ts)
            sxfer = sxfer+fxfer*(tf/ts)
            sleak = sleak+fleak*(tf/ts)
            scab  = scab+fcab*(tf/ts)
            spca  = spca+fpca*(tf/ts)
        
        if ii % iii !=0:
            ii = ii + 1
            for i in range(0, len(np.linspace(0, tf, ts))):
                if t[i]<=95000.0:
                    ii = ii + 1   
                    
                    
                    
                    
                    
                    
for i in range (0,len(np.linspace(0, tf, ts))):
        
        if(int(t[i]) >= STON[i] and int(t[i]) <=STOFF[i]):
            Istim = AMPL
            IP = i
            Y9  = 1.0-(Y8+Y10+Y11+Y12+Y13+Y14+Y15)
            Y16 = 1.0-(Y17+Y18+Y19)
            Y20 = 1.0-(Y21+Y22+Y37+Y38+Y39+Y40+Y41+Y42)
            Y30 = 1.0-(Y31+Y32+Y33+Y34)
        else:
            Istim = 0.0