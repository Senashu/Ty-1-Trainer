import pymem.process

Glide = 0x288964


class SpaceGlide():
    pm = pymem.Pymem("TY.exe")
    client = pymem.process.module_from_name(pm.process_handle, "TY.exe").lpBaseOfDll

    while True:
        val = pm.read_float(client + Glide)
        change = pm.write_float(client + Glide, 5.5)
        print(val)
        break
