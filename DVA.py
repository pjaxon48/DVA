#    Dease Vector Accelerator, a simple micropython-calculator-compatible tool to make
#    basic vector algebra applications in Engineering Statics easier.
#
#    Copyright (C) 2023  Philip Dease
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

global precision
precision = int(3)

def waiter():
    input("EXE to cont.")
    return

def rounder(rounder):
    global precision
    # forced decimal (NO FLOAT)
    factor = pow(10,precision)
    rounder1 = int(rounder * factor)
    rounder2 = int(rounder) * factor
    rounder2 = rounder1 - rounder2
    rounder1 = rounder1 // factor;
    roundme = str(rounder1) + "." + str(abs(rounder2))
    return roundme

def blanker():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    return

def precise():
    blanker()
    global precision
    number = input("Decimal Precision: ")
    if number != '':
        number = int(number)
        precision = number
    return

def selector():
    print("Dease Vector")
    print("Accelerator: v0.3a")
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
    precise()
    blanker()
    print("Input First Vector")
    Ai=float(input("Ai= "))
    Aj=float(input("Aj= "))
    Ak=float(input("Ak= "))
    print("Input Second Vector")
    Bi=float(input("Bi= "))
    Bj=float(input("Bj= "))
    Bk=float(input("Bk= ")) 
    mA=float(pow((abs(Ai*Ai)+abs(Aj*Aj)+abs(Ak*Ak)),0.5))
    mB=float(pow((abs(Bi*Bi)+abs(Bj*Bj)+abs(Bk*Bk)),0.5))
    AdB=float(Ai*Bi+Aj*Bj+Ak*Bk)
    mAmB=float(mA*mB)
    unvA=[rounder(Ai/mA),rounder(Aj/mA),rounder(Ak/mA)]
    unvB=[rounder(Bi/mB),rounder(Bj/mB),rounder(Bk/mB)]
    AcB=[rounder(Aj*Bk-Ak*Bj),rounder(Ak*Bi-Ai*Bk),rounder(Ai*Bj-Aj*Bi)]
    print("magn.A= ",rounder(mA))
    print("magn.B= ",rounder(mB))
    print("unit v.A= ",unvA[0],"i ",unvA[1],"j ",unvA[2],"k ")
    print("unit v.B= ",unvB[0],"i ",unvB[1],"j ",unvB[2],"k ")
    print("A dot B= ",rounder(AdB))
    print("A x B= ",AcB[0],"i ",AcB[1],"j ",AcB[2],"k ")
    return

def vectoramplifier():
    precise()
    blanker()
    print("Input Components")
    Ci=float(input("i= "))
    Cj=float(input("j= "))
    Ck=float(input("k= "))
    mC=float(pow((abs(Ci*Ci)+abs(Cj*Cj)+abs(Ck*Ck)),0.5))
    unvC=[Ci/mC,Cj/mC,Ck/mC]
    displunvC=[rounder(x) for x in unvC]
    print(displunvC)
    print("Input Scalar Coeff.")
    scalC=float(input("Scalar= "))
    tunvC = [rounder((scalC*x)) for x in unvC]
    print(" ")
    print("Amplified Vector=")
    print(tunvC[0],"i ",tunvC[1],"j ",tunvC[2],"k ")
    return

blanker()
selector()
