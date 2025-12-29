from functions.add_guest import add_guest
from functions.remove_guest import remove_guest
from functions.view_guests import view_guest_names
from functions.guest_count import see_total_count
from functions.data import save_lists  # if needed


def show_menu():
    print("\n--- Wedding Guest List ---")
    print("1. Add guest")
    print("2. Remove guest")
    print("3. View guest names")
    print("4. See total count")
    print("5. Exit")

# case 5 exits the while loop
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