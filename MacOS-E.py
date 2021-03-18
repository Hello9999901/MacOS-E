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
sw_vers = sw.strip().rstrip()

abmodelID = modelID.strip("Model Identifier")
abmodelID = abmodelID.strip(": ")
print (abmodelID)

#MACBOOK
if abmodelID == ("MacBook10,1"):
    modelInfo = ("MacBook (Retina, 12-inch, 2017)")
elif abmodelID == ("MacBook9,1"):
    modelInfo = ("MacBook (Retina, 12-inch, Early 2016)")
elif abmodelID == ("MacBook8,1"):
    modelInfo = ("MacBook (Retina, 12-inch, Early 2015)")
elif abmodelID == ("MacBook8,1"):
    modelInfo = ("MacBook (13-inch, Mid 2010)")
elif abmodelID == ("MacBook6,1"):
    modelInfo = ("MacBook (13-inch, Late 2009)")
elif abmodelID == ("MacBook5,2"):
    modelInfo = ("MacBook (13-inch, Early/Mid 2009)")
#MACBOOK PRO
elif abmodelID == ("MacBookPro17,1"):
    modelInfo = ("MacBook Pro (13-inch, M1, 2020)")
elif abmodelID == ("MacBookPro16,3"):
    modelInfo = ("MacBook Pro (13-inch, 2020, 2 Thunderbolt 3 Ports)")
elif abmodelID == ("MacBookPro16,2"):
    modelInfo = ("MacBook Pro (13-inch, 2020, 4 Thunderbolt 3 Ports)")
elif abmodelID == ("MacBookPro16,1"):
    modelInfo = ("MacBook Pro (16-inch, 2019)")
elif abmodelID == ("MacBookPro16,4"):
    modelInfo = ("MacBook Pro (16-inch, 2019)")
elif abmodelID == ("MacBookPro15,4"):
    modelInfo = ("MacBook Pro (13-inch, 2019, 2 Thunderbolt 3 Ports)")
elif abmodelID == ("MacBookPro15,1"):
    modelInfo = ("MacBook Pro (15-inch, 2019)")
elif abmodelID == ("MacBookPro15,3"):
    modelInfo = ("MacBook Pro (15-inch, 2019)")
elif abmodelID == ("MacBookPro15,2"):
    modelInfo = ("MacBook Pro (13-inch, 2019, 4 Thunderbolt 3 Ports)")
elif abmodelID == ("MacBookPro15,1"):
    modelInfo = ("MacBook Pro (15-inch, 2018)")
elif abmodelID == ("MacBookPro15,2"):
    modelInfo = ("MacBook Pro (13-inch, 2018, 4 Thunderbolt 3 Ports)")
elif abmodelID == ("MacBookPro14,3"):
    modelInfo = ("MacBook Pro (15-inch, 2017)")
elif abmodelID == ("MacBookPro14,2"):
    modelInfo = ("MacBook Pro (13-inch, 2017, 4 Thunderbolt 3 Ports)")
elif abmodelID == ("MacBookPro14,1"):
    modelInfo = ("MacBook Pro (13-inch, 2017, 2 Thunderbolt 3 Ports)")
elif abmodelID == ("MacBookPro13,3"):
    modelInfo = ("MacBook Pro (15-inch, 2016)")
elif abmodelID == ("MacBookPro13,2"):
    modelInfo = ("MacBook Pro (13-inch, 2016, 4 Thunderbolt 3 Ports)")
elif abmodelID == ("MacBookPro13,1"):
    modelInfo = ("MacBook Pro (13-inch, 2016, 2 Thunderbolt 3 Ports)")
elif abmodelID == ("MacBookPro11,4"):
    modelInfo = ("MacBook Pro (Retina, 15-inch, Mid 2015)")
elif abmodelID == ("MacBookPro11,5"):
    modelInfo = ("MacBook Pro (Retina, 15-inch, Mid 2015)")
elif abmodelID == ("MacBookPro12,1"):
    modelInfo = ("MacBook Pro (Retina, 13-inch, Early 2015)")
elif abmodelID == ("MacBookPro11,2"):
    modelInfo = ("MacBook Pro (Retina, 15-inch, Early 2014)")
elif abmodelID == ("MacBookPro11,3"):
    modelInfo = ("MacBook Pro (Retina, 15-inch, Early 2014)")
elif abmodelID == ("MacBookPro11,1"):
    modelInfo = ("MacBook Pro (Retina, 13-inch, Mid 2014)")
elif abmodelID == ("MacBookPro11,2"):
    modelInfo = ("MacBook Pro (Retina, 15-inch, Late 2013)")
elif abmodelID == ("MacBookPro11,3"):
    modelInfo = ("MacBook Pro (Retina, 15-inch, Late 2013)")
elif abmodelID == ("MacBookPro11,1"):
    modelInfo = ("MacBook Pro (Retina, 13-inch, Late 2013)")
elif abmodelID == ("MacBookPro10,1"):
    modelInfo = ("MacBook Pro (Retina, 15-inch, Early 2013)")
elif abmodelID == ("MacBookPro10,2"):
    modelInfo = ("MacBook Pro (Retina, 13-inch, Early 2013)")
elif abmodelID == ("MacBookPro10,2"):
    modelInfo = ("MacBook Pro (Retina, 13-inch, Late 2012)")
elif abmodelID == ("MacBookPro10,1"):
    modelInfo = ("MacBook Pro (Retina, 15-inch, Mid 2012)")       
elif abmodelID == ("MacBookPro9,1"):
    modelInfo = ("MacBook Pro (Retina, 15-inch, Mid 2012)")
elif abmodelID == ("MacBookPro9,2"):
    modelInfo = ("MacBook Pro (13-inch, Mid 2012)")
elif abmodelID == ("MacBookPro8,3"):
    modelInfo = ("MacBook Pro (17-inch, Late 2011)")
elif abmodelID == ("MacBookPro8,2"):
    modelInfo = ("MacBook Pro (15-inch, Late 2011)")
elif abmodelID == ("MacBookPro8,1"):
    modelInfo = ("MacBook Pro (13-inch, Late 2011)")
elif abmodelID == ("MacBookPro8,3"):
    modelInfo = ("MacBook Pro (17-inch, Early 2011)")
elif abmodelID == ("MacBookPro8,2"):
    modelInfo = ("MacBook Pro (15-inch, Early 2011)")
elif abmodelID == ("MacBookPro8,1"):
    modelInfo = ("MacBook Pro (13-inch, Early 2011)")
elif abmodelID == ("MacBookPro6,1"):
    modelInfo = ("MacBook Pro (17-inch, Mid 2010)")
elif abmodelID == ("MacBookPro6,2"):
    modelInfo = ("MacBook Pro (15-inch, Mid 2010)")
elif abmodelID == ("MacBookPro7,1"):
    modelInfo = ("MacBook Pro (13-inch, Mid 2010)")
elif abmodelID == ("MacBookPro5,2"):
    modelInfo = ("MacBook Pro (17-inch, Mid 2009)")
elif abmodelID == ("MacBookPro5,3"):
    modelInfo = ("MacBook Pro (15-inch, Mid 2009)")
elif abmodelID == ("MacBookPro5,3"):
    modelInfo = ("MacBook Pro (15-inch, 2.53GHz, Mid 2009)")
elif abmodelID == ("MacBookPro5,5"):
    modelInfo = ("MacBook Pro (13-inch, Mid 2009)")
elif abmodelID == ("MacBookPro5,2"):
    modelInfo = ("MacBook Pro (13-inch, Early 2009)")
elif abmodelID == ("MacBookPro5,1"):
    modelInfo = ("MacBook Pro (15-inch, Early 2008)")
elif abmodelID == ("MacBookPro4,1"):
    modelInfo = ("MacBook Pro (17-inch, Early 2008)")
elif abmodelID == ("MacBookPro4,1"):
    modelInfo = ("MacBook Pro (15-inch, Early 2008)")
#MACBOOK AIR
elif abmodelID == ("MacBookAir10,1"):
    modelInfo = ("MacBookAir (M1, 2020)")
elif abmodelID == ("MacBookAir9,1"):
    modelInfo = ("MacBookAir (Retina, 13-inch, 2020)")
elif abmodelID == ("MacBookAir8,2"):
    modelInfo = ("MacBookAir (Retina, 13-inch, 2019)")
elif abmodelID == ("MacBookAir8,1"):
    modelInfo = ("MacBookAir (Retina, 13-inch, 2018)")
elif abmodelID == ("MacBookAir7,2"):
    modelInfo = ("MacBookAir (13-inch, 2017)")
elif abmodelID == ("MacBookAir7,2"):
    modelInfo = ("MacBookAir (13-inch, Early 2015)")


else:
    pass

modelInfo = ("""Model Information: """ + modelInfo)


tk.Label(action, text="MacOS-E: macOS's CPU-Z \n", font = "Monaco 40").grid(sticky = "N")
tk.Label(action, text=cpu.strip().rstrip(), font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text=cpuname, font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text=cpuspeed, font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text=hyperthread, font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text=cores, font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text=L2cache, font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text=L3cache, font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text=ram, font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text="\n", font = "Monaco 25").grid(sticky = "w")

tk.Label(action, text=model, font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text=modelID, font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text=modelInfo, font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text=romv, font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text=smcv, font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text="\n", font = "Monaco 25").grid(sticky = "w")
tk.Label(action, text=sw_vers, font = "Monaco 25").grid(sticky = "w")

tk.mainloop()