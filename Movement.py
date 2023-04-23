import time

from pymem import Pymem
from pymem.process import module_from_name
from Offsets import *

mem = Pymem("Ty.exe")
module = module_from_name(mem.process_handle, "Ty.exe").lpBaseOfDll


def Glide1():
    mem.write_float(module + Glide, 5.5)


def Glide2(value):
    mem.write_float(module + Glide, float(value))


def GlideSpeed1():
    mem.write_float(module + GlideSpeed, 7.0)


def GlideSpeed2(value):
    mem.write_float(module + GlideSpeed, float(value))


def ToggleTyState():
    mem.write_int(module + TyState1, 35)
    time.sleep(0.5)
    mem.write_int(module + TyState1, 39)


def RunSpeed1():
    mem.write_float(module + RunSpeed, 10.0)


def RunSpeed2(value):
    mem.write_float(module + RunSpeed, float(value))


def JumpHeightG1():
    mem.write_float(module + JumpHeightG, 18.57417488)


def JumpHeightG2(value):
    mem.write_float(module + JumpHeightG, float(value))


def JumpHeightW1():
    mem.write_float(module + JumpHeightW, 10.67707825)


def JumpHeightW2(value):
    mem.write_float(module + JumpHeightW, float(value))


def JumpPeak1():
    Test1 = mem.write_float(module + JumpPeak, -3055.0)
    print(Test1)


def JumpPeak2():
    Test2 = mem.write_float(module + JumpPeak, 1050.0)
    print(Test2)


def SwimSurface1():
    mem.write_float(module + SwimSurface, 6.0)


def SwimSurface2(value):
    mem.write_float(module + SwimSurface, float(value))


def AirborneSpeed1():
    mem.write_float(module + AirborneSpeed, 10.0)


def AirborneSpeed2(value):
    mem.write_float(module + AirborneSpeed, float(value))
