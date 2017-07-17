import json
import os

def newList():
    for mod in data["mods"]:
        responseOK = False
        while not responseOK:
            responseOK = True
            if mod["name"] == "base":
                break
            includeMod = input("{}? ".format(mod["name"]))
            if includeMod.lower() in ["y", "yes", "1", "true"]:
                mod["enabled"] = True
            elif includeMod.lower() in ["n", "no", "0", "false" ]:
                mod["enabled"] = False
            else:
                responseOK = False
    print("\n New List:")
    for mod in data["mods"]:
        print("{}: {}".format(mod["name"], mod["enabled"]))
    listName = input("List name? ")
    with open(MODPATH + ".factorio-modloader\\" + listName + ".json", "w", newline='\n') as f:
        json.dump(data,f, indent=2)


def mainLoop():
    inp = input("What to do?")
    if inp.lower() in ["new"]:
        newList()

MODPATH = os.getenv("APPDATA") + "\\Factorio\\mods\\"
f = []
for (dirpath, dirnames, filenames) in os.walk(MODPATH):
    f.extend(filenames)
    break
# print(f)
if not os.path.exists(MODPATH + ".factorio-modloader"):
    os.makedirs(MODPATH + ".factorio-modloader")

with open(MODPATH + "mod-list.json") as mod_list_file:
    data = json.load(mod_list_file)
for mod in data["mods"]:
    print("{}: {}".format(mod["name"], mod["enabled"]))
mainLoop()

