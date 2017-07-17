import os
import zipfile
MODPATH = os.getenv("APPDATA") + "\\Factorio\\mods\\"
with zipfile.ZipFile(MODPATH + "Dectorio_0.5.13.zip") as test:
    with test.open("Dectorio_0.5.13/info.json") as f:
        print(f.read())
#TODO read dependencies
