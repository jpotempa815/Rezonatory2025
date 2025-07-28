import os, platform
from ctypes import cdll
path = "open-closed-aperture_250725/TLPMX_64.dll"

with open(path, "rb") as f:
    print(f.read(4))

print(platform.architecture())

dll_name = "TLPMX_64.dll"
dllabspath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + dll_name
dll = cdll.LoadLibrary(dllabspath)

