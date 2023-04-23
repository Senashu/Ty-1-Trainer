from pymem import Pymem
from pymem.process import module_from_name
from Offsets import *
import time

mem = Pymem("Ty.exe")
module = module_from_name(mem.process_handle, "Ty.exe").lpBaseOfDll


def Spawn_Z1():
    mem.write_float(module + X, 71.0)
    mem.write_float(module + Y, 2622.94)
    mem.write_float(module + Z, 209.0)
    mem.write_float(module + R, 3.13)
    time.sleep(0.3)
    mem.write_float(module + C1, 4.69)
    mem.write_float(module + C2, 0.17)


def Hub1():
    mem.write_float(module + X, 480.58)
    mem.write_float(module + Y, 2372.05)
    mem.write_float(module + Z, 9597.81)
    mem.write_float(module + R, 3.14897)
    time.sleep(0.3)
    mem.write_float(module + C1, 4.74098)
    mem.write_float(module + C2, 0.1179)


def Hub2():
    mem.write_float(module + X, -3020.3)
    mem.write_float(module + Y, 131.61)
    mem.write_float(module + Z, 9045.79)
    mem.write_float(module + R, 5.13115)
    time.sleep(0.3)
    mem.write_float(module + C1, 0.39604)
    mem.write_float(module + C2, 0.12515)


def Hub3():
    mem.write_float(module + X, 5011.57)
    mem.write_float(module + Y, 1016.98)
    mem.write_float(module + Z, 7448.6)
    mem.write_float(module + R, 3.53157)
    time.sleep(0.3)
    mem.write_float(module + C1, 5.27552)
    mem.write_float(module + C2, 0.05155)


def Fence_Skip():
    mem.write_float(module + X, 825.51)
    mem.write_float(module + Y, 2372.05)
    mem.write_float(module + Z, 11993.98)
    mem.write_float(module + R, 3.29465)
    time.sleep(0.3)
    mem.write_float(module + C1, 4.86098)
    mem.write_float(module + C2, 0.2109)


def Julius():
    mem.write_float(module + X, -6273.16)
    mem.write_float(module + Y, 459.32)
    mem.write_float(module + Z, 774.88)
    mem.write_float(module + R, 4.83383)
    time.sleep(0.3)
    mem.write_float(module + C1, 0.11656)
    mem.write_float(module + C2, 0.05507)


def Gate_Skip():
    mem.write_float(module + X, -2099.99)
    mem.write_float(module + Y, -200.94)
    mem.write_float(module + Z, -3444.54)
    mem.write_float(module + R, 0.70687)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.25744)
    mem.write_float(module + C2, 0.09302)


def Behind_Gate():
    mem.write_float(module + X, -18.59)
    mem.write_float(module + Y, 63.28)
    mem.write_float(module + Z, -6975.4)
    mem.write_float(module + R, 0.04462)
    time.sleep(0.3)
    mem.write_float(module + C1, 1.61544)
    mem.write_float(module + C2, 0.13202)


def Spawn_A1():
    mem.write_float(module + X, -2989.0)
    mem.write_float(module + Y, 240.67)
    mem.write_float(module + Z, 8238.0)
    mem.write_float(module + R, 1.942)
    time.sleep(0.3)
    mem.write_float(module + C1, 3.5128)
    mem.write_float(module + C2, 0.18459)


def Bilby1():
    mem.write_float(module + X, 4357.9)
    mem.write_float(module + Y, -556.21)
    mem.write_float(module + Z, 5493.36)
    mem.write_float(module + R, 0.15035)
    time.sleep(0.3)
    mem.write_float(module + C1, 1.75414)
    mem.write_float(module + C2, 0.18168)


def Two_Up_Swim():
    mem.write_float(module + X, 2675.79)
    mem.write_float(module + Y, -715.44)
    mem.write_float(module + Z, 6447.27)
    mem.write_float(module + R, 3.43001)
    time.sleep(0.3)
    mem.write_float(module + C1, 5.00086)
    mem.write_float(module + C2, 0.22148)


def Spyeggs():
    mem.write_float(module + X, -328.58)
    mem.write_float(module + Y, -698.63)
    mem.write_float(module + Z, 4194.1)
    mem.write_float(module + R, 5.31223)
    time.sleep(0.3)
    mem.write_float(module + C1, 0.58721)
    mem.write_float(module + C2, 0.2058)


def Bite_Slide():
    mem.write_float(module + X, -4848.68)
    mem.write_float(module + Y, 59.83)
    mem.write_float(module + Z, 4861.63)
    mem.write_float(module + R, 4.86604)
    time.sleep(0.3)
    mem.write_float(module + C1, 0.09103)
    mem.write_float(module + C2, 0.41813)


def Two_Up_Buttons():
    mem.write_float(module + X, -2595.75)
    mem.write_float(module + Y, 144.92)
    mem.write_float(module + Z, -680.92)
    mem.write_float(module + R, 3.69804)
    time.sleep(0.3)
    mem.write_float(module + C1, 5.26883)
    mem.write_float(module + C2, -0.08558)


def Two_Up_Portal():
    mem.write_float(module + X, -8497.19)
    mem.write_float(module + Y, 451.76)
    mem.write_float(module + Z, -580.0)
    mem.write_float(module + R, 3.69383)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.92772)
    mem.write_float(module + C2, 0.4115)


def Two_Up_Skip():
    mem.write_float(module + X, 2615.12)
    mem.write_float(module + Y, -310.37)
    mem.write_float(module + Z, -2029.0)
    mem.write_float(module + R, 3.83502)
    time.sleep(0.3)
    mem.write_int(module + TyState1, 35)
    mem.write_float(module + C1, 5.40978)
    mem.write_float(module + C2, 0.0189)


def Second_Rang():
    mem.write_float(module + X, -2888.34)
    mem.write_float(module + Y, -53.3)
    mem.write_float(module + Z, -3645.26)
    mem.write_float(module + R, 0.62568)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.19501)
    mem.write_float(module + C2, 0.36572)


def End():
    mem.write_float(module + X, -6437.52)
    mem.write_float(module + Y, 293.41)
    mem.write_float(module + Z, -3130.07)
    mem.write_float(module + R, 3.53153)
    time.sleep(0.3)
    mem.write_float(module + C1, 5.0582)
    mem.write_float(module + C2, 0.06272)


def Spawn_A2():
    mem.write_float(module + X, -8940.0)
    mem.write_float(module + Y, -1453.55)
    mem.write_float(module + Z, 7162.0)
    mem.write_float(module + R, 0.992)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.5628)
    mem.write_float(module + C2, 0.1419)


def Buzchy_Swim():
    mem.write_float(module + X, -5962.93)
    mem.write_float(module + Y, -1472.52)
    mem.write_float(module + Z, 3572.01)
    mem.write_float(module + R, 4.79116)
    time.sleep(0.3)
    mem.write_float(module + C1, 0.07889)
    mem.write_float(module + C2, 1.303)


def Walk_Skip():
    mem.write_float(module + X, -4302.91)
    mem.write_float(module + Y, -817.35)
    mem.write_float(module + Z, 3061.66)
    mem.write_float(module + R, 0.45562)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.0242)
    mem.write_float(module + C2, 0.11271)


def Ken():
    mem.write_float(module + X, -2562.97)
    mem.write_float(module + Y, -2281.12)
    mem.write_float(module + Z, -4177.06)
    mem.write_float(module + R, 0.19595)
    mem.write_int(module + TyState1, 17)
    time.sleep(0.3)
    mem.write_float(module + C1, 1.76674)
    mem.write_float(module + C2, 0.1329)


def Turkey():
    mem.write_float(module + X, 1492.81)
    mem.write_float(module + Y, -3356.75)
    mem.write_float(module + Z, -692.25)
    mem.write_float(module + R, 2.02041)
    time.sleep(0.3)
    mem.write_float(module + C1, 3.5522)
    mem.write_float(module + C2, 0.21988)


def EndA2():
    mem.write_float(module + X, -5958.79)
    mem.write_float(module + Y, 237.16)
    mem.write_float(module + Z, 7389.61)
    mem.write_float(module + R, 4.82565)
    time.sleep(0.3)
    mem.write_float(module + C1, 0.11301)
    mem.write_float(module + C2, 0.33947)


def PortalA2():
    mem.write_float(module + X, 6678.63)
    mem.write_float(module + Y, -277.19)
    mem.write_float(module + Z, 7310.58)
    mem.write_float(module + R, 0.90595)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.47675)
    mem.write_float(module + C2, 0.28865)


def Spawn_A3():
    mem.write_float(module + X, -13646.0)
    mem.write_float(module + Y, 338.0)
    mem.write_float(module + Z, 22715.0)
    mem.write_float(module + R, 1.005)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.5758)
    mem.write_float(module + C2, 0.1419)


def Lost_Kids_Mission():
    mem.write_float(module + X, -9484.51)
    mem.write_float(module + Y, 581.22)
    mem.write_float(module + Z, 14636.73)
    mem.write_float(module + R, 2.50294)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 4.11698)
    mem.write_float(module + C2, 0.3489)


def Ship():
    mem.write_float(module + X, 9259.79)
    mem.write_float(module + Y, -1448.35)
    mem.write_float(module + Z, 24658.69)
    mem.write_float(module + R, 2.95981)
    mem.write_int(module + TyState1, 17)
    time.sleep(0.7)
    mem.write_float(module + C1, 4.5306)
    mem.write_float(module + C2, 0.3129)
    time.sleep(0.5)
    mem.write_float(module + C1, 4.5306)
    mem.write_float(module + C2, 0.3129)


def Nest_Swim():
    mem.write_float(module + X, 4911.11)
    mem.write_float(module + Y, 1.41)
    mem.write_float(module + Z, 25770.66)
    mem.write_float(module + R, 4.15921)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 5.7366)
    mem.write_float(module + C2, 0.1299)


def Coconuts():
    mem.write_float(module + X, 5887.86)
    mem.write_float(module + Y, 937.28)
    mem.write_float(module + Z, 17640.59)
    mem.write_float(module + R, 0.37927)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 1.94929)
    mem.write_float(module + C2, 0.43887)


def BilbyBite():
    mem.write_float(module + X, 11925.15)
    mem.write_float(module + Y, -16.79)
    mem.write_float(module + Z, 9913.16)
    mem.write_float(module + R, 0.76918)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.3404)
    mem.write_float(module + C2, 0.19285)


def Spire_Gate():
    mem.write_float(module + X, -11580.01)
    mem.write_float(module + Y, -23.12)
    mem.write_float(module + Z, -10634.98)
    mem.write_float(module + R, 2.44648)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 3.17762)
    mem.write_float(module + C2, -0.66952)


def Spire_Swim():
    mem.write_float(module + X, 2487.02)
    mem.write_float(module + Y, -145.27)
    mem.write_float(module + Z, -8040.23)
    mem.write_float(module + R, 0.88982)
    mem.write_int(module + TyState1, 17)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.46062)
    mem.write_float(module + C2, 0.14348)


def Top_Spire():
    mem.write_float(module + X, 2079.13)
    mem.write_float(module + Y, 5690.19)
    mem.write_float(module + Z, -11863.61)
    mem.write_float(module + R, 4.6766)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 6.24573)
    mem.write_float(module + C2, 0.20775)


def Pillar1():
    mem.write_float(module + X, -1296.7)
    mem.write_float(module + Y, -500.29)
    mem.write_float(module + Z, -1738.89)
    mem.write_float(module + R, 2.01136)
    time.sleep(0.3)
    mem.write_float(module + C1, 0.39548)
    mem.write_float(module + C2, 0.35335)


def Pillar2():
    mem.write_float(module + X, -2793.51)
    mem.write_float(module + Y, -527.66)
    mem.write_float(module + Z, -1865.33)
    mem.write_float(module + R, 4.90683)
    time.sleep(0.3)
    mem.write_float(module + C1, 0.1178)
    mem.write_float(module + C2, 0.30235)


def Pillar3():
    mem.write_float(module + X, -3975.49)
    mem.write_float(module + Y, -571.86)
    mem.write_float(module + Z, 35.68)
    mem.write_float(module + R, 0.29883)
    time.sleep(0.3)
    mem.write_float(module + C1, 1.8668)
    mem.write_float(module + C2, 0.29635)


def Pillar4():
    mem.write_float(module + X, -2448.91)
    mem.write_float(module + Y, -467.77)
    mem.write_float(module + Z, 1901.82)
    mem.write_float(module + R, 5.78907)
    time.sleep(0.3)
    mem.write_float(module + C1, 1.0118)
    mem.write_float(module + C2, 0.40735)


def Pillar5():
    mem.write_float(module + X, -70.76)
    mem.write_float(module + Y, -496.01)
    mem.write_float(module + Z, 735.47)
    mem.write_float(module + R, 4.86063)
    time.sleep(0.3)
    mem.write_float(module + C1, 0.1598)
    mem.write_float(module + C2, 0.31435)


def Bridge_Spawn():
    mem.write_float(module + X, -3353.0)
    mem.write_float(module + Y, 1983.0)
    mem.write_float(module + Z, 5.0)
