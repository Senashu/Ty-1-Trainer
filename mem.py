from readwritememory import readwritememory

rwm = ReadWriteMemory()

process = rwm.get_progress_by_name("TY.exe")
process.open()

baseadress = 0x5C0000+0x288964

Fly = process.get_pointer(0x00848964)

while l:
    value = process.read(Fly)
    print(value)