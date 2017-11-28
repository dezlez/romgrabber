import os
for file in os.listdir("/home/pi/RetroPie/roms/snes"):
    if file.endswith(".srm"):
        print(os.path.join("/snes", file))
