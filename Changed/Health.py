import pymem.process

Health = 0x2737CC


class Healthy():
    pm = pymem.Pymem("TY.exe")
    client = pymem.process.module_from_name(pm.process_handle, "TY.exe").lpBaseOfDll

    while True:
        val = pm.read_int(client + Health)
        change = pm.write_int(client + Health, val + 1)
        print(val)
        break
