#    Dease Stress Accelerator, a simple micropython-calculator-compatible tool to make
#    stress transformation problems in Machine Design easier.
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
    print("Dease Stress")
    print("Accelerator: v0.1")
    print(" ")
    print("[1] Princ. Stress") 
    print("[2] Von Mises Eq")
    choice=int(input("Choose (3 to quit)"))
    if  choice == 1:
        princstress()
    if  choice == 2:
        vectoramplifier()
    if  choice == 3:
        quit()
    return 

def princstress():
    precise()
    blanker()
    print("Input Stresses:")
    oxx=float(input("@xx= "))
    oyy=float(input("@yy= "))
    txy=float(input("txy= "))
    oavg = (oxx+oyy)/2
    tmax = pow((pow((oxx-oyy)/2,2)+pow(txy,2)),0.5)
    o1 = oavg + tmax
    o2 = oavg - tmax
    ov = pow((pow(o1,2)+pow(o2,2)-(o1*o2)),0.5)
    print(" ")
    print("@1= ",rounder(o1))
    print("@2= ",rounder(o2))
    print("@avg= ",rounder(oavg))
    print("tmax= ",rounder(tmax))
    print("@v= ",rounder(ov))
    return

def vectoramplifier():
    precise()
    blanker()
    o1=float(input("@1= "))
    o2=float(input("@2= "))
    o3=float(input("@3= "))
    oy =float(input("@y= "))
    ov = pow((pow(o1,2)+pow(o2,2)+pow(o3,2)-(o1*o2)-(o2*o3)-(o3*o1)),0.5)
    fos = oy/ov
    print(" ")
    print("Von Mises Equiv=")
    print("@v/e=",rounder(ov))
    print("F.O.S= ")
    print("N= ",rounder(fos))
    return

blanker()
selector()
