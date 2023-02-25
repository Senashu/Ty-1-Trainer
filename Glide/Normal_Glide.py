import pymem


class Normal_Glide:
    process = pymem.process
    mem = pymem.memory

    TY = pymem.Pymem("TY.exe")
    TY_base = TY.process_handle

    address = 0x848964
    value = 5.5
    print(value)
    mem.write_float(TY_base, address, value)
