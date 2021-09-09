
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 00:00:12 2015

@author: Brent
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint


NP   = 500
NEQ  = 45
TINI = 20
TPER = 1000
TW   = 0.5
AMPL = 80.0
tf = 100
ts = 100000
iii  =  1000
ii   =     0

#
# Initial Conditions
#
frel  = 0.0
fcal  = 0.0
fup   = 0.0
ftrpn = 0.0
fnaca = 0.0
fxfer = 0.0
fleak = 0.0
fcab  = 0.0
fpca  = 0.0
frelm = 0.0
fcalm = 0.0
#
srel  = 0.0
scal  = 0.0
sup   = 0.0
strpn = 0.0
snaca = 0.0
sxfer = 0.0
sleak = 0.0
scab  = 0.0
spca  = 0.0

t = np.linspace(0, tf, ts)

def beta2(state, t):
    
    
    
    
    iii  =  1000
    ii   =     0
    STON = []
    STOFF= []
    Y1 = state[0]
    Y2 = state[1]
    Y3 = state[2]
    Y4 = state[3]
    Y5 = state[4]
    Y6 = state[5]
    Y7 = state[6]
    Y8 = state[7]
    Y9 = state[8]
    Y10 = state[9]
    Y11 = state[10]
    Y12 = state[11]
    Y13 = state[12]
    Y14 = state[13]
    Y15 = state[14]
    Y16 = state[15]
    Y17 = state[16]
    Y18 = state[17]
    Y19 = state[18]
    Y20 = state[19]
    Y21 = state[20]
    Y22 = state[21]
    Y23 = state[22]
    Y24 = state[23]
    Y25 = state[24]
    Y26 = state[25]
    Y27 = state[26]
    Y28 = state[27]
    Y29 = state[28]
    Y30 = state[29]
    Y31 = state[30]
    Y32 = state[31]
    Y33 = state[32]
    Y34 = state[33]
    Y35 = state[34]
    Y36 = state[35]
    Y37 = state[36]
    Y38 = state[37]
    Y39 = state[38]
    Y40 = state[39]
    Y41 = state[40]
    Y42 = state[41]
    Y43 = state[42]
    Y44 = state[43]
    Y45 = state[44]
   
    

    dt       =     0.0001
    NP   = 500
    NEQ  = 45
    TINI = 20
    TPER = 1000
    TW   = 0.5
    AMPL = 80.0
    
    durat    = 10000.0
    stimon1  =    20.0
    stimoff1 =    20.5
    stimst1  =    75.0
    stimon2  =   520.0
    stimoff2 =  1020.0
    stimst2  =    20.0
    Vrest    =   -80.0
    

   
    
 
 
    


    
    
#    77  continue
#      if (time.ge.durat) go to 88
#      if(mod(ii,iii).ne.0) go to 6
#
    time  =      0.0
    Istim =      0.0
    Y2ini =   Y2
    Acap =  1.5340e-4
    Vmyo = 25.8400e-6
    Vjsr =  0.1200e-6
    Vnsr =  2.0980e-6
    Vss  =  1.4850e-9
      #
      # Standard Ionic Concentrations
      #
    cKo  =   4000.0
    cNao = 136000.0
    cCao =   1800.0
      #
      # SR Parameters
      #
    Icasmax = 7.0
    t1  = 0.04
    t2  = -0.1/Icasmax
    
    v1    = 4.0    
    v2    =  5.8e-5*0.3
    v3    =  1.8*0.25*0.7
    Kmup  =  0.5
    Ttr   = 20.0
    Txfer =  8.0
    Kap   =  0.006075
    Kam   =  0.07125
    Kbp   =  0.00405
    Kbm   =  0.965
    Kcp   =  0.009
    Kcm   =  0.0008
      #
      # L-type Ca2+ Channel Parameters
      #
    Kpcmax  =  0.11662
    Kpchalf = 10.0
    Kpcb    =  0.0005
    Kpcf    =  2.5
    SFC4I1  =  0.01
    SFC4I2  =  0.002
    SFC4I3  =  1.0
    SFOI1   =  1.0
    SFOI2   =  0.001
    SFI1I3  =  0.001
    SFI2I3  =  1.0
    SFICA   =  0.02222
      #
      #Buffering Parameters
      #
    cLTRPNtot =    70.0
    cHTRPNtot =   140.0
    khtrpnp   =     0.00237
    khtrpnm   =     0.000032
    kltrpnp   =     0.0327
    kltrpnm   =     0.0196
    cCMDNtot  =    50.0
    cCSQNtot  = 15000.0
    Kmcmdn    =     0.238
    Kmcsqn    =   800.0
      #
      # Membrane Current Parameters
      #
    Cm      =     1.0
    F       =    96.5
    T       =   298.0
    R       =     8.314
    factor  =    R*T/F
    ifactor =    F/(R*T)
    Gna     =    13.0
    Gkp     =     0.00828
    Pnak    =     0.01833
    knaca   =   292.8*0.8
    Kmna    = 87500.0
    Kmca    =  1380.0
    ksat    =     0.1
    nu      =     0.35
    Inakmax =     0.88*0.8
    Kmnai   = 21000.0
    Kmko    =  1500.0
    sigma   = (np.exp(cNao/67300.0)-1.0)/7.0
    Ipcamax =     1.0*0.17*0.5
    Kmpca   =     0.5
    Gcab    =     0.000165*0.3
    Gnab    =     0.0026
    dito    =     7.0
    Gks     =     0.46/80.
    Gkto    =     0.3846
    Gkur1   =     0.0
    Gkur2   =     0.3424
    Gkur3   =     0.0611
      #
      # HERG current parameters
      #
    kf  = 0.023761
    kb  = 0.036778
    Gkr = 0.078
      #
      # Calcium activated chloride current
      #
    Gclca     = 10.0
    Poclcamax = 0.2
    Kmclca    = 10.0
    Ecl       = -40.0
    Icas = 0.2342*(Y1-63.0)*Y8
    Jup      = v3*Y2*Y2/(Kmup*Kmup+Y2*Y2)
    Pryr     = np.exp((Y1-5.0)*(Y1-5.0)/(-648.0))
    Jrelt    = v1*(Y18+Y19)*(Y6-Y7)*Pryr
#    Jrelt    = v1*(Y18+Y19)*(Y6-Y7)*Y44
    Jtrt     = ((Y3-Y6)/Ttr)
    Jxfert   = ((Y7-Y2)/Txfer)
    Jleak    = v2*(Y3-Y2)
    temp12    = khtrpnp*Y2*(cHTRPNtot-Y5)-khtrpnm*Y5
    temp13    = kltrpnp*Y2*(cLTRPNtot-Y4)-kltrpnm*Y4
    Jtrpn    = temp12 + temp13
    tempa1 = knaca/(Kmna*Kmna*Kmna+cNao*cNao*cNao)
    tempa2 = 1.0/(Kmca+cCao)
    tempa3 = 1.0/(1.0+ksat*np.exp((nu-1.0)*Y1*ifactor))
    tempa41 = np.exp(nu*Y1*ifactor)*Y23*Y23*Y23*cCao
    tempa42 = np.exp((nu-1.0)*Y1*ifactor)*cNao*cNao*cNao*Y2
    tempa4 = tempa41-tempa42
    Inaca = tempa1*tempa2*tempa3*tempa4
    global Ecan 
    Ecan = 0.5*factor*np.log(cCao/Y2)
    global Icab 
    Icab = Gcab*(Y1-Ecan)
    global Ipca 
    Ipca = Ipcamax*Y2*Y2/(Kmpca*Kmpca+Y2*Y2)
      #
      # Read initial conditions from file
      #
#    6 continue
#     ii ii+1
#
    
              
          
    
#
       
      #
       
    Jrelt    = v1*(Y18+Y19)*(Y6-Y7)*Y44
    frel  = Jrelt*Vjsr/Vmyo
    fcal  = -1.0*Icas*Acap*Cm/(2.0*F*Vmyo)
    fup   = -1.0*Jup
    ftrpn = -1.0*Jtrpn
    fnaca = 2.0*Inaca*Acap*Cm/(F*Vmyo)
    fxfer = Jxfert
    fleak = Jleak
    fcab  = -1.0*Icab*Acap*Cm/(F*Vmyo)
    fpca  = -1.0*Ipca*Acap*Cm/(F*Vmyo)
      #
    
    
          
      #
   
    #
#
      #           Calcium fluxes

    
    
   

      #            Ionic currents

      #
      # Y(1)   : Membrane potential (mV)
      #
    V = Y1
      #
      # Icab   : Calcium background current
      #
    Ecan = 0.5*factor*np.log(cCao/Y2)
    Icab = Gcab*(Y1-Ecan)

     #
      # Ipca   : Calcium pump current
      #
    Ipca = Ipcamax*Y2*Y2/(Kmpca*Kmpca+Y2*Y2)
      #
      # Inaca  : Na-Ca exchange current
      #
    tempa1 = knaca/(Kmna*Kmna*Kmna+cNao*cNao*cNao)
    tempa2 = 1.0/(Kmca+cCao)
    tempa3 = 1.0/(1.0+ksat*np.exp((nu-1.0)*Y1*ifactor))
    tempa41 = np.exp(nu*Y1*ifactor)*Y23*Y23*Y23*cCao
    tempa42 = np.exp((nu-1.0)*Y1*ifactor)*cNao*cNao*cNao*Y2
    tempa4 = tempa41-tempa42
    Inaca = tempa1*tempa2*tempa3*tempa4
    #
    # Ica    : L-type calcium current
    #
    Icas = 0.2342*(Y1-52.0)*Y8
    #
    # Ina    : Na fast current (Luo and Rudy, 1994)
    #
    ENa = factor*np.log((0.9*cNao+0.1*cKo)/(0.9*Y23+0.1*Y24))
    Ina = Gna*Y37*(Y1-ENa)
    #
    # Inab   : Na background current
    #
    Inab = Gnab*(Y1-ENa)
    #
    # Inak    : Na-K exchange current
    #
    tempa5 = 1.0/(1.0+(Kmnai/Y23)*np.sqrt(Kmnai/Y23))
    tempa6 = cKo/(cKo+Kmko)
    tempa11= 1.0+0.1245*np.exp(-0.1*Y1*ifactor)
    +0.0365*sigma*np.exp(-1.0*Y1*ifactor)
    Inak = Inakmax*tempa5*tempa6/tempa11
    #
    # Ikto    : transient outward current (Liu and Rasmusson, 1997)
    #
    EK = factor*np.log(cKo/Y24)
    Ikto = Gkto*Y25*Y25*Y25*Y26*(Y1-EK)
    #
    # Ik1    : Time independent K+ current (Rasmusson et al. 1990)
    #
    tempa7 = 0.3397*cKo/(cKo+210.0)
    tempa8 = 1.0+np.exp(0.0448*(Y1-EK))
    Ik1 = tempa7*(Y1-EK)/tempa8
    #
    # IR   : leak current
    #
    IR = 0.0193*Y1
    #
    # Iks    : Delayed rectifier K+ current (Rasmusson et al. 1990)
    #
    Iks = Gks*Y27*Y27*(Y1-EK)
    
    #
    # Ikur   : Ultra-rapidly activating delayed rectifier Ikur
    #                  (Zhou et al., 1998)
    #
    Ikur1 = Gkur1*Y28*Y29*(Y1-EK)
    Ikur2 = Gkur2*Y35*Y36*(Y1-EK)
    Ikur3 = Gkur3*Y43*(Y1-EK)
    Ikur = Ikur1+Ikur2+Ikur3
    #
    # Ikr    : HERG current (Wang et al., 1997)
    #
    EKr = factor*np.log((0.98*cKo+0.02*cNao)/(0.98*Y24+0.02*Y23))
    Ikr = Gkr*Y33*(Y1-EKr)
    #
    # Iclca  : calcium-activated chloride current (Xu et al., 2002)
    #
    tempa9  = Poclcamax/(1+np.exp((46.7-Y1)/7.8))
    tempa10 = Y2/(Y2+Kmclca)
    Iclca = Gclca*tempa9*tempa10*(Y1-Ecl)
    #

    #
    # Y(1)  membrane potential
    #
    sum_i = Icas+Icab+Inaca+Ipca+Ina+Inab+Iclca+IR
    +Inak+Ikto+Ik1+Iks+Ikur+Ikr-Istim
    YDOT1 = -sum_i/Cm
    #
    # Y(2)  intracellular calcium Cai
    #
    Bi = 1.0/(1+cCMDNtot*Kmcmdn/((Kmcmdn+Y2)*(Kmcmdn+Y2)))
    temp1 = 0.5*(Icab - 2.0*Inaca + Ipca)*Acap/(Vmyo*F)
    YDOT2 = Bi*(Jleak + Jxfert - Jup - Jtrpn - temp1)
    #
    # Y(3)  network SR calcium Cansr
    #
    YDOT3 = (Jup-Jleak)*Vmyo/Vnsr - Jtrt*Vjsr/Vnsr
    #
    # Y(4)  cLTRPNca
    #
    YDOT4 = kltrpnp*Y2*(cLTRPNtot-Y4) - kltrpnm*Y4
    #
    # Y(5)  cHTRPNca
    #
    YDOT5 = khtrpnp*Y2*(cHTRPNtot-Y5) - khtrpnm*Y5
    #
    #     Partial contributions
    #
    alpha = 0.4 * np.exp((Y1+15.0)/15.0)
    beta  = 0.13 * np.exp(-1.0*(Y1+15.0)/18.0)
    #
    gamma = Kpcmax*Y7/(Kpchalf+Y7)
    #
    # Y(6) cCajsr junction SR calcium concentartion
    #
    temp2 = (Kmcsqn+Y6)*(Kmcsqn+Y6)
    Bjsr  = 1.0/(1.0+cCSQNtot*Kmcsqn/temp2)
    YDOT6 = Bjsr*(Jtrt-Jrelt)
    #
    # Y(7) cCass  subspace calcium concentration
    #
    temp3 = (Kmcmdn+Y7)*(Kmcmdn+Y7)
    Bss   = 1.0/(1.0+cCMDNtot*Kmcmdn/temp3)
    temp4 = Jrelt*Vjsr/Vss-Jxfert*Vmyo/Vss
    YDOT7 = Bss*(temp4-Icas*Acap/(2.0*Vss*F))
    #
    # Y(8)     O  Ca channel variable
    #
    YDOT8 = alpha*Y12 - 4.0*beta*Y8
    + SFOI1*Kpcb*Y13 - SFOI1*gamma*Y8
    + SFOI2*alpha*Y14 - SFOI2*Kpcf*Y8
    #
    # Y(9)    C1  Ca channel variable
    #
    YDOT9 = beta*Y10-4.0*alpha*Y9
    #
    # Y(10)   C2  Ca channel variable
    #
    YDOT10 = 4.0*alpha*Y9 - beta*Y10
    + 2.0*beta*Y11 - 3.0*alpha*Y10
    #
    # Y(11)   C3  Ca channel variable
    #
    YDOT11 = 3.0*alpha*Y10 - 2.0*beta*Y11
    + 3.0*beta*Y12 - 2.0*alpha*Y11
    #
    # Y(12)   C4  Ca channel variable
    #
    YDOT12 = 2.0*alpha*Y11 - 3.0*beta*Y12
    + 4.0*beta*Y8 - alpha*Y12
    + 4.0*SFC4I1*Kpcb*beta*Y13 - SFC4I1*alpha*gamma*Y12
    + 4.0*SFC4I2*beta*Y14 - SFC4I2*Kpcf*Y12
    + 4.0*SFC4I3*beta*Kpcb*Y15 - SFC4I3*gamma*Kpcf*Y12
    #
    # Y(13)   I1  Ca channel variable
    #
    YDOT13 = SFOI1*gamma*Y8 - SFOI1*Kpcb*Y13
    + SFI1I3*alpha*Y15 - SFI1I3*Kpcf*Y13
    + SFC4I1*alpha*gamma*Y12 - 4.0*SFC4I1*beta*Kpcb*Y13
    #
    # Y(14)   I2  Ca channel variable
    #
    YDOT14 = SFOI2*Kpcf*Y8 - SFOI2*alpha*Y14
    + SFI2I3*Kpcb*Y15 - SFI2I3*gamma*Y14
    + SFC4I2*Kpcf*Y12 - 4.0*SFC4I2*beta*Y14
    #
    # Y(15)   I3  Ca channel variable
    #
    YDOT15 = SFI1I3*Kpcf*Y13 - SFI1I3*alpha*Y15
    + SFI2I3*gamma*Y14 - SFI2I3*Kpcb*Y15
    + SFC4I3*gamma*Kpcf*Y12 - 4.0*SFC4I3*beta*Kpcb*Y15
    #
    # Y(16)-Y(19)  RyR channel states
    #
    temp5 = Y7*Y7*Y7
    temp6 = Y7*Y7*Y7*Y7
    YDOT16=-Kap*temp6*Y16+Kam*Y18
    YDOT17= Kcp*Y18-Kcm*Y17
    YDOT18= Kap*temp6*Y16-Kam*Y18
    -Kbp*temp5*Y18+Kbm*Y19
    -Kcp*Y18+Kcm*Y17
    YDOT19= Kbp*temp5*Y18-Kbm*Y19
    #
    #  Y(20)-Y(22),Y(37)-Y(42) Na fast current (Clancy-Rudy, Circulation, 2002)
    #
    Va=Y1+2.5
    Vi=Y1+7.0
    alp11 = 3.802/(0.1027*np.exp(-Va/17.0)+0.20*np.exp(-Va/150.0))
    alp12 = 3.802/(0.1027*np.exp(-Va/15.0)+0.23*np.exp(-Va/150.0))
    alp13 = 3.802/(0.1027*np.exp(-Va/12.0)+0.25*np.exp(-Va/150.0))
    bet11 = 0.1917*np.exp(-Va/20.3)
    bet12 = 0.20*np.exp(-(Va-5.0)/20.3)
    bet13 = 0.22*np.exp(-(Va-10.0)/20.3)
    alp3  = 7.0e-7*np.exp(-Vi/7.7)
    bet3  = (0.0084+0.00002*Vi)
    alp2  = 1.0/(0.188495*np.exp(-Vi/16.6)+0.393956)
    bet2  = alp13*alp2*alp3/(bet13*bet3)
    alp4  = alp2/1000.0
    bet4  = alp3
    alp5  = alp2/9.5e4
    bet5  = alp3/50.0

    YDOT20 = bet11*Y21 - alp11*Y20
    + alp3*Y42  - bet3*Y20
    YDOT21 = alp11*Y20 - bet11*Y21
    + bet12*Y22 - alp12*Y21
    + alp3*Y41  - bet3*Y21
    YDOT22 = alp12*Y21 - bet12*Y22
    + bet13*Y37 - alp13*Y22
    + alp3*Y38  - bet3*Y22
    YDOT37 = alp13*Y22 - bet13*Y37
    + bet2*Y38  - alp2*Y37
    YDOT38 = alp2*Y37  - bet2*Y38
    + bet3*Y22  - alp3*Y38
    + bet4*Y39  - alp4*Y38
    + alp12*Y41 - bet12*Y38
    YDOT39 = alp4*Y38  - bet4*Y39
    + bet5*Y40  - alp5*Y39
    YDOT40 = alp5*Y39  - bet5*Y40
    YDOT41 = alp11*Y42 - bet11*Y41
    + bet12*Y38 - alp12*Y41
    + bet3*Y21  - alp3*Y41
    YDOT42 = bet11*Y41 - alp11*Y42
    + bet3*Y20  - alp3*Y42
    #
    #  Y(23)  Na intracellular concentration
    #
    YDOT23 = -1.0*(Ina+Inab+3.0*(Inaca+Inak))*Acap/(Vmyo*F)
    #
    #  Y(24)  K  intracellular concentration
    #
    YDOT24 = -1.0*(Ikto+Ik1+IR+Iks+Ikur+Ikr-2.0*Inak)*Acap/(Vmyo*F)
    #
    #  Y(25),Y(26)  ato and ito gating variables for Ikto
      
    alp25 = 0.04516*np.exp(0.03577*(Y1+30.0))*4.0
    bet25 = 0.0989*np.exp(-0.06237*(Y1+30.0))*4.0
    temp7 = 0.0019*np.exp((Y1+13.5)/(-1.0*dito))
    temp8 = 0.067083*np.exp((Y1+13.5+20.0)/(-1.0*dito))
    alp26 = 0.08*temp7/(1.0+temp8)
    temp9  = 0.0019*np.exp((Y1+13.5+20.0)/dito)
    temp10 = 0.051335*np.exp((Y1+13.5+20.0)/dito)
    bet26 = 0.5*temp9/(1.0+temp10)
   
    
    #
    YDOT25 = alp25*(1.0-Y25) - bet25*Y25
    YDOT26 = alp26*(1.0-Y26) - bet26*Y26
    #
    #  Y(27)  nks gating variable for Iks
    #
    temp11 = 0.00001444*(Y1+26.5)
    alp27  = temp11/(1.0-np.exp(-0.128*(Y1+26.5)))/3.0
    bet27  = 0.000286*np.exp(-0.038*(Y1+26.5))/3.0
    #
    YDOT27 = alp27*(1.0-Y27) - bet27*Y27
    #
    #  Y(28), Y(29)  aur and iur gating variables for Ikur1
    #
    ass = 1.0/(1.0+np.exp((-22.5-Y1)/7.7))
    iss1 = 1.0/(1.0+np.exp((45.2+Y1)/5.7))
#   taua1 = (0.493*exp(-0.0629*Y(1))+2.058)
    taua1 = 6.1/(np.exp(0.0629*(Y1+40.0))
    + np.exp(-0.0629*(Y1+40.0)))+2.058
    taui1 = 270 + 1050.0/(1+np.exp((Y1+45.2)/5.7))
    #
    YDOT28 = (ass-Y28)/taua1
    YDOT29 = (iss1-Y29)/taui1
    #
    #  Y(35), Y(36)  aur and iur gating variables for Ikur2
    #
    iss2 = 1.0/(1.0+np.exp((45.2+Y1)/5.7))
#           taua2 = (0.493*exp(-0.0629*Y(1))+2.058)
    taua2 = 6.1/(np.exp(0.0629*(Y1+40.0))
    + np.exp(-0.0629*(Y1+40.0)))+2.058
    taui2 = 1200.0-170.0/(1.0+np.exp((45.2+Y1)/5.7))
    #
    YDOT35 = (ass-Y35)/taua2
    YDOT36 = (iss2-Y36)/taui2
    #
    #  Y(43) aur gating variable for Ikur3
    #
    #      taua3 = (39.3*exp(-0.0862*Y(1))+13.17)
    taua3 = 1235.5/(np.exp(0.0862*(Y1+40.0))
    + np.exp(-0.0862*(Y1+40.0)))+13.17
    YDOT43 = (ass-Y43)/taua3
    YDOT45 = (ass-Y45)/taui1
    #
    # Y(30)-Y(34) HERG channel state variables
    #
    ala0 = 0.022348*np.exp(0.01176*Y1)
    bea0 = 0.047002*np.exp(-0.0631*Y1)
    ala1 = 0.013733*np.exp(0.038198*Y1)
    bea1 = 0.0000689*np.exp(-0.04178*Y1)
    ali  = 0.090821*np.exp(0.023391*(Y1+5.0))
    bei  = 0.006497*np.exp(-0.03268*(Y1+5.0))
    #
    YDOT30 = bea0*Y31-ala0*Y30
    YDOT31 = ala0*Y30-bea0*Y31+kb*Y32-kf*Y31
    YDOT32 = kf*Y31-kb*Y32+bea1*Y33-ala1*Y32
    YDOT33 = ala1*Y32-bea1*Y33+bei*Y34-ali*Y33
    YDOT34 = ali*Y33-bei*Y34
    #
    #   Y(44) Pryr Ryanodine receptor modulation factor
    #
    YDOT44 = -t1*Y44+t2*Icas*np.exp((Y1+5.0)*(Y1+5.0)/(-648.0))
   
    
   
    #
    
    return [YDOT1, YDOT2, YDOT3, YDOT4, YDOT5, YDOT6, YDOT7, YDOT8, YDOT9, 
        YDOT10, YDOT11, YDOT12, YDOT13, YDOT14, YDOT15, YDOT16, YDOT17, YDOT18, 
        YDOT19, YDOT20, YDOT21, YDOT22, YDOT23, YDOT24, YDOT25, YDOT26, 
        YDOT27, YDOT28, YDOT29, YDOT30, YDOT31, YDOT32, YDOT33, YDOT34, YDOT35, 
        YDOT36, YDOT37, YDOT38, YDOT39, YDOT40, YDOT41, YDOT42, YDOT43, YDOT44,
        YDOT45]
    

t = np.linspace(0, tf, ts)


state =[ -0.7624524735E+02,
          0.1280999943E+00,
          0.1115217386E+04,
          0.1232596963E+02,
          0.1266506549E+03,
          0.1115217386E+04,
          0.1280999943E+00,
          0.8826160637E-11,
          0.9931232892E+00,
          0.6858913455E-02,
          0.1776391749E-04,
          0.2044747347E-07,
          0.2603730259E-10,
          0.3272528036E-08,
          0.9654005429E-08,
          0.9997188280E+00,
          0.2582190329E-03,
          0.2295280289E-04,
          0.2024933516E-09,
          0.4178212515E+00,
          0.2675896691E-01,
          0.7304321592E-03,
          0.1477292015E+05,
          0.1432134541E+06,
          0.4857287150E-02,
          0.9999445673E+00,
          0.6518345732E-03,
          0.9295293130E-03,
          0.9957072881E+00,
          0.9968369629E+00,
          0.1573676639E-02,
          0.1016698315E-02,
          0.4554446131E-03,
          0.1172175786E-03,
          0.9295293130E-03,
          0.9957072880E+00,
          0.4220365114E-05,
          0.9098152690E-03,
          0.1281126499E-04,
          0.9494611654E-07,
          0.3333056516E-01,
          0.5204318424E+00,
          0.9295293130E-03,
          0.3752713569E-13,
          0.4281555833E-02]
       
cell_model = odeint(beta2, state, t)
Y1  = [i[0] for i in cell_model]
Y2  = [i[1] for i in cell_model]
Y3  = [i[2] for i in cell_model]
Y4  = [i[3] for i in cell_model]
Y5  = [i[4] for i in cell_model]
Y6  = [i[5] for i in cell_model]
Y7  = [i[6] for i in cell_model]
Y8  = [i[7] for i in cell_model]
Y9  = [i[8] for i in cell_model]
Y10 = [i[9] for i in cell_model]
Y11 = [i[10] for i in cell_model]
Y12 = [i[11] for i in cell_model]
Y13 = [i[12] for i in cell_model]
Y14 = [i[13] for i in cell_model]
Y15 = [i[14] for i in cell_model]
Y16 = [i[15] for i in cell_model]
Y17 = [i[16] for i in cell_model]
Y18 = [i[17] for i in cell_model]
Y19 = [i[18] for i in cell_model]
Y20 = [i[19] for i in cell_model]
Y21 = [i[20] for i in cell_model]
Y22 = [i[21] for i in cell_model]
Y23 = [i[22] for i in cell_model]
Y24 = [i[23] for i in cell_model]
Y25 = [i[24] for i in cell_model]
Y26 = [i[25] for i in cell_model]
Y27 = [i[26] for i in cell_model]
Y28 = [i[27] for i in cell_model]
Y29 = [i[28] for i in cell_model]
Y30 = [i[29] for i in cell_model]
Y31 = [i[30] for i in cell_model]
Y32 = [i[31] for i in cell_model]
Y33 = [i[32] for i in cell_model]
Y34 = [i[33] for i in cell_model]
Y35 = [i[34] for i in cell_model]
Y36 = [i[35] for i in cell_model]
Y37 = [i[36] for i in cell_model]
Y38 = [i[37] for i in cell_model]
Y39 = [i[38] for i in cell_model]
Y40 = [i[39] for i in cell_model]
Y41 = [i[40] for i in cell_model]
Y42 = [i[41] for i in cell_model]
Y43 = [i[42] for i in cell_model]
Y44 = [i[43] for i in cell_model]
Y45 = [i[44] for i in cell_model]


plt.plot(t, Y1)