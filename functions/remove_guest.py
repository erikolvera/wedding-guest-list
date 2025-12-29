from functions.data import grooms_list, brides_list, save_lists

#case 2
def remove_guest():
    while True:
        name_to_remove = input('Who are we removing? (or enter nothing to stop): ').strip()
        if name_to_remove == '':
            break
        name_lower = name_to_remove.lower()

        for name in grooms_list[:]:
            if name.lower() == name_lower:
                grooms_list.remove(name)
                save_lists()
                print(f"{name} removed from the groom's list")
                break
        else:
            for name in brides_list[:]:
                if name.lower() == name_lower:
                    brides_list.remove(name)
                    save_lists()
                    print(f"{name} removed from the bride's list")
                    break
            else:
                print("Name not in list")