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


def Reverse_Fence_Skip():
    mem.write_float(module + X, 880.91)
    mem.write_float(module + Y, 2372.05)
    mem.write_float(module + Z, 12102.76)
    mem.write_float(module + R, 6.27071)
    time.sleep(0.3)
    mem.write_float(module + C1, 1.57054)
    mem.write_float(module + C2, -1.309)


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


def TurkeyA2():
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
    mem.write_float(module + X, -3242.0)
    mem.write_float(module + Y, -610.25)
    mem.write_float(module + Z, 6197.0)
    mem.write_float(module + R, 1.178)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.7488)
    mem.write_float(module + C2, 0.1419)


def BridgeSwim():
    mem.write_float(module + X, 106.19)
    mem.write_float(module + Y, -912.21)
    mem.write_float(module + Z, 5601.59)
    mem.write_float(module + R, 4.60753)
    mem.write_int(module + TyState1, 17)
    time.sleep(0.3)
    mem.write_float(module + C1, 6.17832)
    mem.write_float(module + C2, 0.10777)


def Flick_Dennis():
    mem.write_float(module + X, -1309.7)
    mem.write_float(module + Y, 811.11)
    mem.write_float(module + Z, -5658.0)
    mem.write_float(module + R, 0.61244)
    mem.write_int(module + TyState1, 17)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.18324)
    mem.write_float(module + C2, 0.57931)


def RexMission():
    mem.write_float(module + X, 4767.2)
    mem.write_float(module + Y, -102.39)
    mem.write_float(module + Z, -3667.72)
    mem.write_float(module + R, 3.15073)
    mem.write_int(module + TyState1, 17)
    time.sleep(0.3)
    mem.write_float(module + C1, 4.72152)
    mem.write_float(module + C2, 0.15286)


def Neddy():
    mem.write_float(module + X, 5291.03)
    mem.write_float(module + Y, 59.18)
    mem.write_float(module + Z, -161.26)
    mem.write_float(module + R, 3.02003)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 4.69342)
    mem.write_float(module + C2, -0.16379)


def Turkey():
    mem.write_float(module + X, 8430.67)
    mem.write_float(module + Y, 97.09)
    mem.write_float(module + Z, -3758.4)
    mem.write_float(module + R, 1.58495)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 3.16196)
    mem.write_float(module + C2, 0.00586)


def Old_BridgeSwim():
    mem.write_float(module + X, -6318.7)
    mem.write_float(module + Y, -764.01)
    mem.write_float(module + Z, 4604.15)
    mem.write_float(module + R, 4.48567)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 6.05647)
    mem.write_float(module + C2, 0.14518)


def Old_Swim():
    mem.write_float(module + X, -6318.94)
    mem.write_float(module + Y, -763.79)
    mem.write_float(module + Z, 4604.13)
    mem.write_float(module + R, 4.48315)
    mem.write_int(module + TyState1, 17)
    time.sleep(0.3)
    mem.write_float(module + C1, 6.05395)
    mem.write_float(module + C2, 0.03766)


def Spawn_B2():
    mem.write_float(module + X, -518.0)
    mem.write_float(module + Y, -2624.4)
    mem.write_float(module + Z, 212.0)
    mem.write_float(module + R, 3.344)
    time.sleep(0.3)
    mem.write_float(module + C1, 4.9148)
    mem.write_float(module + C2, 0.1419)


def Yabby():
    mem.write_float(module + X, 20107.09)
    mem.write_float(module + Y, -8531.91)
    mem.write_float(module + Z, -14314.21)
    mem.write_float(module + R, 1.09624)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.57753)
    mem.write_float(module + C2, 0.22563)


def LawnSwim():
    mem.write_float(module + X, 21679.29)
    mem.write_float(module + Y, -10209.63)
    mem.write_float(module + Z, -19789.04)
    mem.write_float(module + R, 1.68173)
    mem.write_int(module + TyState1, 17)
    time.sleep(0.3)
    mem.write_float(module + C1, 3.25252)
    mem.write_float(module + C2, -0.07137)


def Icicles():
    mem.write_float(module + X, 43124.38)
    mem.write_float(module + Y, -2723.73)
    mem.write_float(module + Z, -20936.08)
    mem.write_float(module + R, 0.58667)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.12447)
    mem.write_float(module + C2, 0.16289)


def Mountain():
    mem.write_float(module + X, 43642.73)
    mem.write_float(module + Y, -2700.32)
    mem.write_float(module + Z, -16108.59)
    mem.write_float(module + R, 3.98017)
    time.sleep(0.3)
    mem.write_float(module + C1, 5.56665)
    mem.write_float(module + C2, 0.31289)


def MillSkip():
    mem.write_float(module + X, 40646.48)
    mem.write_float(module + Y, -543.4)
    mem.write_float(module + Z, -215.04)
    mem.write_float(module + R, 3.71202)
    time.sleep(0.3)
    mem.write_float(module + C1, 5.32332)
    mem.write_float(module + C2, 0.1449)


def MillFlick():
    mem.write_float(module + X, 40594.39)
    mem.write_float(module + Y, 399.33)
    mem.write_float(module + Z, 1031.61)
    mem.write_float(module + R, 3.7305)
    time.sleep(0.3)
    mem.write_float(module + C1, 5.3275)
    mem.write_float(module + C2, 0.1239)


def IceBlock():
    mem.write_float(module + X, 1304.9)
    mem.write_float(module + Y, -5124.65)
    mem.write_float(module + Z, -12253.62)
    mem.write_float(module + R, 4.77467)
    time.sleep(0.3)
    mem.write_float(module + C1, 0.067)
    mem.write_float(module + C2, 0.2109)


def Kid6():
    mem.write_float(module + X, 7568.02)
    mem.write_float(module + Y, -4475.24)
    mem.write_float(module + Z, -5778.75)
    mem.write_float(module + R, 5.67289)
    time.sleep(0.3)
    mem.write_float(module + C1, 1.17413)
    mem.write_float(module + C2, 0.3129)


def Outback():
    print("Sheesh")


def WIP():
    print("Sheesh")


def Spawn_E1():
    mem.write_float(module + X, -8845.0)
    mem.write_float(module + Y, 1700.07)
    mem.write_float(module + Z, 17487.0)
    mem.write_float(module + R, 2.01)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 3.5808)
    mem.write_float(module + C2, 0.1419)


def OOB_Jump():
    mem.write_float(module + X, -5386.87)
    mem.write_float(module + Y, 2443.71)
    mem.write_float(module + Z, 15793.93)
    mem.write_float(module + R, 2.22649)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 3.8298)
    mem.write_float(module + C2, 0.0339)


def On_Tree():
    mem.write_float(module + X, -4692.28)
    mem.write_float(module + Y, 3107.32)
    mem.write_float(module + Z, 15984.82)
    mem.write_float(module + R, 6.24154)
    mem.write_int(module + TyState1, 5)
    time.sleep(0.3)
    mem.write_float(module + C1, 1.52915)
    mem.write_float(module + C2, 0.1419)


def Pass_Swim():
    mem.write_float(module + X, -4693.26)
    mem.write_float(module + Y, -1858.49)
    mem.write_float(module + Z, 12779.31)
    mem.write_float(module + R, 0.48087)
    mem.write_int(module + TyState1, 17)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.05166)
    mem.write_float(module + C2, -0.07071)


def Portal_E1():
    mem.write_float(module + X, -10188.06)
    mem.write_float(module + Y, -1638.86)
    mem.write_float(module + Z, -6791.36)
    mem.write_float(module + R, 5.48193)
    mem.write_int(module + TyState1, 17)
    time.sleep(0.3)
    mem.write_float(module + C1, 1.25571)
    mem.write_float(module + C2, -0.63013)


def Spawn_D2():
    mem.write_float(module + X, -6306.0)
    mem.write_float(module + Y, -860.18)
    mem.write_float(module + Z, -7322.0)
    mem.write_float(module + R, 1.169)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.7398)
    mem.write_float(module + C2, 0.13924)


def EnableBoss():
    mem.write_float(module + X, -4207.16)
    mem.write_float(module + Y, -1354.65)
    mem.write_float(module + Z, -5649.22)
    mem.write_float(module + R, 2.82692)
    time.sleep(0.3)
    mem.write_float(module + C1, 4.38079)
    mem.write_float(module + C2, 0.27424)


def D2_Button1():
    mem.write_float(module + X, -2282.98)
    mem.write_float(module + Y, -1354.65)
    mem.write_float(module + Z, -2486.75)
    mem.write_float(module + R, 1.88734)
    time.sleep(0.3)
    mem.write_float(module + C1, 3.45813)
    mem.write_float(module + C2, 0.25275)


def D2_Button2():
    mem.write_float(module + X, -2846.48)
    mem.write_float(module + Y, 42.39)
    mem.write_float(module + Z, -12693.28)
    mem.write_float(module + R, 6.01882)
    time.sleep(0.3)
    mem.write_float(module + C1, 1.32805)
    mem.write_float(module + C2, -0.24155)


def D2_Button3():
    mem.write_float(module + X, 4913.24)
    mem.write_float(module + Y, 1464.94)
    mem.write_float(module + Z, -6769.71)
    mem.write_float(module + R, 4.95575)
    time.sleep(0.3)
    mem.write_float(module + C1, 0.22536)
    mem.write_float(module + C2, -0.48805)


def D2_End():
    mem.write_float(module + X, 8037.1)
    mem.write_float(module + Y, 2640.26)
    mem.write_float(module + Z, -5968.18)
    mem.write_float(module + R, 0.51431)
    time.sleep(0.3)
    mem.write_float(module + C1, 2.0614)
    mem.write_float(module + C2, 0.3399)


def Doom_Clip():
    mem.write_float(module + X, -1408.73)
    mem.write_float(module + Y, -235.39)
    mem.write_float(module + Z, -229.49)
    mem.write_float(module + R, 3.4473)
    time.sleep(0.3)
    mem.write_float(module + C1, 5.0268)
    mem.write_float(module + C2, 1.309)
