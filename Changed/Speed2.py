import pymem.process

Speed = 0x288914


class Speedy420():
    pm = pymem.Pymem("TY.exe")
    client = pymem.process.module_from_name(pm.process_handle, "TY.exe").lpBaseOfDll

    while True:
        val = pm.read_float(client + Speed)
        change = pm.write_float(client + Speed, 50.0)
        print(val)
        break
