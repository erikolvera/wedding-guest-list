from functions.data import grooms_list, brides_list, save_lists

#case 1
def add_guest():
    list_choice = input("Add to the groom or bride list? Enter 1 or 2 "
                        "\n 1. Groom "
                        "\n 2. Bride \n" )
    if list_choice == "1":
        case1_grooms_choice()
    elif list_choice == "2":
        case1_brides_choice()
    else:
        print("Invalid choice: Enter 1 or 2")


def case1_grooms_choice():
    while True:
        guest_name = input("Who would you like to add? (or enter nothing to stop): ").strip()
        if guest_name == '':
            break
        else:
            grooms_list.append(guest_name)
            save_lists()
            print(f"{guest_name} added to the list")

def case1_brides_choice():
    while True:
        guest_name = input("Who would you like to add? (or enter nothing to stop): ").strip()
        if guest_name == '':
            break
        else:
            brides_list.append(guest_name)
            save_lists()
            print(f"{guest_name} added to the list")
