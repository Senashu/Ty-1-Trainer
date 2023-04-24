from pymem import Pymem
from pymem.process import module_from_name

from Offsets import *

mem = Pymem("Ty.exe")
module = module_from_name(mem.process_handle, "Ty.exe").lpBaseOfDll


def Health():
    mem.write_int(module + Health1, 4)


def HealthWater():
    mem.write_int(module + HealthWater1, 8)


def SuperBite():
    mem.write_int(module + SuperBite1, 100)
