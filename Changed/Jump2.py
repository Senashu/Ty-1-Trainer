import pymem.process

Jump = 0x28893C


class Jumpy():
    pm = pymem.Pymem("TY.exe")
    client = pymem.process.module_from_name(pm.process_handle, "TY.exe").lpBaseOfDll

    while True:
        val = pm.read_float(client + Jump)
        change = pm.write_float(client + Jump, 42.0)
        print(val)
        break
