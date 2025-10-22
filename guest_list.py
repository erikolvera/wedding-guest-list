import json # brings in python json module
import os # lets you interact with your os

grooms_list = []
brides_list = []

if os.path.exists("guest_lists.json"):
    with open("guest_lists.json", "r") as file:
        data = json.load(file)
        grooms_list = data.get("husband", [])
        brides_list = data.get("wife", [])

def save_lists():
    with open("guest_lists.json", "w") as file:
        json.dump({"husband": grooms_list, "wife": brides_list}, file)

def show_menu():
    print("\n--- Wedding Guest List ---")
    print("1. Add guest")
    print("2. Remove guest")
    print("3. View guest lists")
    print("4. See total count")
    print("5. Exit")

def case1_husband_choice():
    guest_name = input("Who would you like to add? ")
    grooms_list.append(guest_name)
    save_lists()
    print(f"{guest_name} added to the list")

def case1_wife_choice():
    guest_name = input("Who would you like to add? ")
    brides_list.append(guest_name)
    save_lists()
    print(f"{guest_name} added to the list")


#case 1
def add_guest():
    list_choice = input("Would you like to add to the husband's or wife's list? ")
    if list_choice.lower() == "husband":
        case1_husband_choice()
    elif list_choice.lower() == "wife":
        case1_wife_choice()
    else:
        return False
    
#case 2
def remove_guest():
    pass
#case 3
def view_guest_names():
    # print(grooms_list)
    pass

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
            break
        case "3":
            view_guest_names()
        case "4":
            see_total_count()
        case "5":
            goodbye_message()
            break

