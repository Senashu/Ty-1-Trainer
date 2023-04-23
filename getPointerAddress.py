from pymem.ptypes import RemotePointer


def getPointerAddress(process_handle, base, offsets):
    remote_pointer = RemotePointer(process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset
