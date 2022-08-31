#    Dease Vector Accelerator, a simple micropython-calculator-compatible tool to make
#    basic vector algebra applications in Engineering Statics easier.
#
#    Copyright (C) 2022  Philip Dease
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import math

def waiter():
    input("EXE to cont.")
    return

def blanker():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    return

def selector():
    print("Dease Vector")
    print("Accelerator: v0.2a")
    print(" ")
    print("[1] 2 Vectors") 
    print("[2] Vec. Amplifier")
    choice=int(input("Choose (3 to quit)"))
    if  choice == 1:
        twovectors()
    if  choice == 2:
        vectoramplifier()
    if  choice == 3:
        quit()
    return 

def twovectors():
    blanker()
    print("Input First Vector")
    Ai=float(input("Ai= "))
    Aj=float(input("Aj= "))
    Ak=float(input("Ak= "))
    print("Input Second Vector")
    Bi=float(input("Bi= "))
    Bj=float(input("Bj= "))
    Bk=float(input("Bk= ")) 
    mA=float(math.sqrt(abs(Ai*Ai)+abs(Aj*Aj)+abs(Ak*Ak)))
    mB=float(math.sqrt(abs(Bi*Bi)+abs(Bj*Bj)+abs(Bk*Bk)))
    AdB=float(Ai*Bi+Aj*Bj+Ak*Bk)
    mAmB=float(mA*mB)
    unvA=[round(Ai/mA,3),round(Aj/mA,3),round(Ak/mA,3)]
    unvB=[round(Bi/mB,3),round(Bj/mA,3),round(Bk/mB,3)]
    AcB=[round(Aj*Bk-Ak*Bj,3),round(Ak*Bi-Ai*Bk,3),round(Ai*Bj-Aj*Bi,3)]
    print("magn.A= ",round(mA,3))
    print("magn.B= ",round(mB,3))
    print("unit v.A= ",unvA[0],"i ",unvA[1],"j ",unvA[2],"k ")
    print("unit v.B= ",unvB[0],"i ",unvB[1],"j ",unvB[2],"k ")
    #print("unit v.A= ",round(Ai/mA,3),"i ",round(Aj/mA,3),"j ",round(Ak/mA,3),"k")
    #print("unit v.B= ",round(Bi/mB,3),"i ",round(Bj/mB,3),"j ",round(Bk/mB,3),"k")
    print("A dot B= ",round(AdB,3))
    print("A x B= ",AcB[0],"i ",AcB[1],"j ",AcB[2],"k ")
    #print("A cross B= ",round(Aj*Bk-Ak*Bj,3),"i ",round(Ak*Bi-Ai*Bk,3),"j ",round(Ai*Bj-Aj*Bi,3),"k")
    return

def vectoramplifier():
    blanker()
    print("Input Components")
    Ci=float(input("i= "))
    Cj=float(input("j= "))
    Ck=float(input("k= "))
    mC=float(math.sqrt(abs(Ci*Ci)+abs(Cj*Cj)+abs(Ck*Ck)))
    unvC=[Ci/mC,Cj/mC,Ck/mC]
    print(unvC)
    print("Input Scalar Coeff.")
    scalC=float(input("Scalar= "))
    tunvC = [round((scalC*x),3) for x in unvC]
    print(" ")
    print("Amplified Vector=")
    print(tunvC[0],"i ",tunvC[1],"j ",tunvC[2],"k ")
    return

blanker()
selector()

