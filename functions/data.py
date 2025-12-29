import json
import os

grooms_list = []
brides_list = []

if os.path.exists("guest_lists.json"):
    with open("guest_lists.json", "r") as file:
        data = json.load(file)
        grooms_list = data.get("groom", [])
        brides_list = data.get("bride", [])

def save_lists():
    with open("guest_lists.json", "w") as file:
        json.dump(dict(groom=grooms_list,
                       bride=brides_list), file, indent=2)