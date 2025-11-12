import json # brings in python json module
import os # lets you interact with your os

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

def show_menu():
    print("\n--- Wedding Guest List ---")
    print("1. Add guest")
    print("2. Remove guest")
    print("3. View guest lists")
    print("4. See total count")
    print("5. Exit")

def case1_grooms_choice():
    while True:
        guest_name = input("Who would you like to add? (or enter nothing to stop) ").strip()
        if guest_name == '':
            break
        else:
            grooms_list.append(guest_name)
            save_lists()
            print(f"{guest_name} added to the list")

def case1_brides_choice():
    while True:
        guest_name = input("Who would you like to add? (or enter nothing to stop) :").strip()
        if guest_name == '':
            break
        else:
            brides_list.append(guest_name)
            save_lists()
            print(f"{guest_name} added to the list")


#case 1
def add_guest():
    list_choice = input("Add to the groom or bride list? ").strip()
    if list_choice.lower() in "groom":
        case1_grooms_choice()
        return None
    elif list_choice.lower() in "bride":
        case1_brides_choice()
        return None
    else:
        return False
    
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



#case 3
def view_guest_names():
    view_lists = input("View groom or bride list? ")
    if view_lists.lower() in "groom":
        print(grooms_list)
    elif view_lists.lower() in "bride":
        print(brides_list)
    # print(grooms_list + brides_list)

# case 4
def see_total_count():
    print(f"{len(grooms_list) + len(brides_list)} guests are coming") # print the total of guests from both husband and wife guest list

# case 5 just exits the while loop
def goodbye_message():
    print("Goodbye!")
    
while True:
    show_menu()
    choice = input("Choose choices 1-5: ")

    match choice:
        case "1":
            add_guest()
        case "2":
            remove_guest()
        case "3":
            view_guest_names()
        case "4":
            see_total_count()
        case "5":
            goodbye_message()
            break

