import os
import tkinter as tk
import platform

action = tk.Tk()
osx = platform.platform()
mac = "macOS" in osx

if mac == True:
    pass
else:
    exit()

action.title("MacOS-E")
action.resizable(width=False, height=False)
hardware = os.popen("system_profiler SPHardwareDataType ").read()
sw = os.popen("sw_vers").read()
cpumod = os.popen("sysctl -a | grep machdep.cpu.brand_string").read()
xz = cpumod.split(":")
cpu = xz[1]


y = (hardware.rstrip().strip().split("\n"))

y.remove("Hardware:")
y.remove ("    Hardware Overview:")
y.pop(0)

model = y[1].strip()
modelID = y[2].strip()
cpuname = y[3].strip()
cpuspeed = y[4].strip()
cores = y[6].strip()
L2cache = y[7].strip()
L3cache = y[8].strip()
hyperthread = y[9].strip()
ram = y[10].strip()
romv = y[11].strip()
smcv = y[12].strip()
serial = y[13].strip()
uuid = y[14].strip()

sw_vers = sw.strip().rstrip()

tk.Label(action, text="MacOS-E: macOS's CPU-Z \n", font = "Mono 40").grid(sticky = "N")
tk.Label(action, text=cpu.strip().rstrip(), font = "Mono 25").grid(sticky = "w")
tk.Label(action, text=cpuname, font = "Mono 25").grid(sticky = "w")
tk.Label(action, text=cpuspeed, font = "Mono 25").grid(sticky = "w")
tk.Label(action, text=hyperthread, font = "Mono 25").grid(sticky = "w")
tk.Label(action, text=cores, font = "Mono 25").grid(sticky = "w")
tk.Label(action, text=L2cache, font = "Mono 25").grid(sticky = "w")
tk.Label(action, text=L3cache, font = "Mono 25").grid(sticky = "w")
tk.Label(action, text=ram, font = "Mono 25").grid(sticky = "w")
tk.Label(action, text="\n", font = "Mono 25").grid(sticky = "w")

tk.Label(action, text=model, font = "Mono 25").grid(sticky = "w")
tk.Label(action, text=modelID, font = "Mono 25").grid(sticky = "w")
tk.Label(action, text=romv, font = "Mono 25").grid(sticky = "w")
tk.Label(action, text=smcv, font = "Mono 25").grid(sticky = "w")
tk.Label(action, text=uuid, font = "Mono 25").grid(sticky = "w")
tk.Label(action, text="\n", font = "Mono 25").grid(sticky = "w")
tk.Label(action, text=sw_vers, font = "Mono 25").grid(sticky = "w")
tk.Label(action, text=serial, font = "Mono 25").grid(sticky = "w")


tk.mainloop()