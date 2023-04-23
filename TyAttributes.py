from Offsets import *
from getPointerAddress import getPointerAddress


def Give_All(pm):
    offsets = [Dive, Swim, Two, Aqua, Frosty, Flame, Zappy, Kaboom, Doomer, Mega, Zoomer, Infra, Multi, Chrono]
    addresses = [getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[offset]) for offset in
                 offsets]
    for address in addresses:
        pm.write_bool(address, True)


def Remove_All(pm):
    offsets = [Dive, Swim, Two, Aqua, Frosty, Flame, Zappy, Kaboom, Doomer, Mega, Zoomer, Infra, Multi, Chrono]
    addresses = [getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[offset]) for offset in
                 offsets]
    for address in addresses:
        pm.write_bool(address, False)


def Give_Elemental(pm):
    offsets = [Kaboom, Doomer, Mega, Zoomer, Infra, Multi, Chrono]
    addresses = [getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[offset]) for offset in
                 offsets]
    for address in addresses:
        pm.write_bool(address, True)


def Give_Techno(pm):
    offsets = [Dive, Swim, Two, Aqua, Frosty, Flame, Zappy]
    addresses = [getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[offset]) for offset in
                 offsets]
    for address in addresses:
        pm.write_bool(address, True)


def toggle_dive(pm, dive_switch):
    diveAddress = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Dive])
    dive_state = pm.read_bool(diveAddress)
    pm.write_bool(diveAddress, not dive_state)
    dive_state = pm.read_bool(diveAddress)
    if dive_state is True:
        dive_switch.configure(text="Dive On", fg_color="green")
    else:
        dive_switch.configure(text="Dive Off", fg_color="red")


def toggle_swim(pm, swim_switch):
    Address = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Swim])
    state = pm.read_bool(Address)
    pm.write_bool(Address, not state)
    state = pm.read_bool(Address)
    if state is True:
        swim_switch.configure(text="Swim On", fg_color="green")
    else:
        swim_switch.configure(text="Swim Off", fg_color="red")


def toggle_2ndRang(pm, TwoRang_switch):
    Address = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Two])
    state = pm.read_bool(Address)
    pm.write_bool(Address, not state)
    state = pm.read_bool(Address)
    if state is True:
        TwoRang_switch.configure(text=" 2nd Rang On ", fg_color="green")
    else:
        TwoRang_switch.configure(text="2nd Rang Off", fg_color="red")


def toggle_aqua(pm, Aqua_switch):
    Address = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Aqua])
    state = pm.read_bool(Address)
    pm.write_bool(Address, not state)
    state = pm.read_bool(Address)
    if state is True:
        Aqua_switch.configure(text="Aqua On", fg_color="green")
    else:
        Aqua_switch.configure(text="Aqua Off", fg_color="red")


def toggle_dive(pm, dive_switch):
    diveAddress = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Dive])
    dive_state = pm.read_bool(diveAddress)
    pm.write_bool(diveAddress, not dive_state)
    dive_state = pm.read_bool(diveAddress)
    if dive_state is True:
        dive_switch.configure(text="Dive On", fg_color="green")
    else:
        dive_switch.configure(text="Dive Off", fg_color="red")


def toggle_swim(pm, swim_switch):
    Address = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Swim])
    state = pm.read_bool(Address)
    pm.write_bool(Address, not state)
    state = pm.read_bool(Address)
    if state is True:
        swim_switch.configure(text="Swim On", fg_color="green")
    else:
        swim_switch.configure(text="Swim Off", fg_color="red")


# Toggle Frosty
def toggle_frosty(pm, frosty_switch):
    frostyAddress = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Frosty])
    frosty_state = pm.read_bool(frostyAddress)
    pm.write_bool(frostyAddress, not frosty_state)
    frosty_state = pm.read_bool(frostyAddress)
    if frosty_state is True:
        frosty_switch.configure(text="Frosty On", fg_color="green")
    else:
        frosty_switch.configure(text="Frosty Off", fg_color="red")


# Toggle Flame
def toggle_flame(pm, flame_switch):
    flameAddress = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Flame])
    flame_state = pm.read_bool(flameAddress)
    pm.write_bool(flameAddress, not flame_state)
    flame_state = pm.read_bool(flameAddress)
    if flame_state is True:
        flame_switch.configure(text="Flame On", fg_color="green")
    else:
        flame_switch.configure(text="Flame Off", fg_color="red")


# Toggle Zappy
def toggle_zappy(pm, zappy_switch):
    zappyAddress = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Zappy])
    zappy_state = pm.read_bool(zappyAddress)
    pm.write_bool(zappyAddress, not zappy_state)
    zappy_state = pm.read_bool(zappyAddress)
    if zappy_state is True:
        zappy_switch.configure(text="Zappy On", fg_color="green")
    else:
        zappy_switch.configure(text="Zappy Off", fg_color="red")


# Toggle Kaboom
def toggle_kaboom(pm, kaboom_switch):
    kaboomAddress = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Kaboom])
    kaboom_state = pm.read_bool(kaboomAddress)
    pm.write_bool(kaboomAddress, not kaboom_state)
    kaboom_state = pm.read_bool(kaboomAddress)
    if kaboom_state is True:
        kaboom_switch.configure(text="Kaboom On", fg_color="green")
    else:
        kaboom_switch.configure(text="Kaboom Off", fg_color="red")


# Toggle Doomer
def toggle_doomer(pm, doomer_switch):
    doomerAddress = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Doomer])
    doomer_state = pm.read_bool(doomerAddress)
    pm.write_bool(doomerAddress, not doomer_state)
    doomer_state = pm.read_bool(doomerAddress)
    if doomer_state is True:
        doomer_switch.configure(text="Doomer On", fg_color="green")
    else:
        doomer_switch.configure(text="Doomer Off", fg_color="red")


def toggle_mega(pm, Mega_switch):
    Address = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Mega])
    state = pm.read_bool(Address)
    pm.write_bool(Address, not state)
    state = pm.read_bool(Address)
    if state is True:
        Mega_switch.configure(text="Mega On", fg_color="green")
    else:
        Mega_switch.configure(text="Mega Off", fg_color="red")


def toggle_zoomer(pm, Zoomer_switch):
    Address = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Zoomer])
    state = pm.read_bool(Address)
    pm.write_bool(Address, not state)
    state = pm.read_bool(Address)
    if state is True:
        Zoomer_switch.configure(text="Zoomer On", fg_color="green")
    else:
        Zoomer_switch.configure(text="Zoomer Off", fg_color="red")


def toggle_infra(pm, Infra_switch):
    Address = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Infra])
    state = pm.read_bool(Address)
    pm.write_bool(Address, not state)
    state = pm.read_bool(Address)
    if state is True:
        Infra_switch.configure(text="Infra On", fg_color="green")
    else:
        Infra_switch.configure(text="Infra Off", fg_color="red")


def toggle_multi(pm, Multi_switch):
    Address = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Multi])
    state = pm.read_bool(Address)
    pm.write_bool(Address, not state)
    state = pm.read_bool(Address)
    if state is True:
        Multi_switch.configure(text="Multi On", fg_color="green")
    else:
        Multi_switch.configure(text="Multi Off", fg_color="red")


def toggle_chrono(pm, Chrono_switch):
    Address = getPointerAddress(pm.process_handle, pm.base_address + 0x288730, offsets=[Chrono])
    state = pm.read_bool(Address)
    pm.write_bool(Address, not state)
    state = pm.read_bool(Address)
    if state is True:
        Chrono_switch.configure(text="Chrono On", fg_color="green")
    else:
        Chrono_switch.configure(text="Chrono Off", fg_color="red")
