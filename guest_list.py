husband_list = []
wife_list = []
combined_lists = []

def show_menu():
    print("\n--- Wedding Guest List ---")
    print("1. Add guest")
    print("2. Remove guest")
    print("3. View guest lists")
    print("4. See total count")
    print("5. Exit")


#case 1
def add_guest():
    list_choice = input("Would you like to add to the husband's or wife's list? ")
    if list_choice == "husband":
        print("Passed")
    elif list_choice == "wife":
        print("Passed as well")
    else:
        return False
    
#case 2
def remove_guest():
    pass
#case 3
def view_guest_names():
    pass

# case 4
def see_total_count():
    print(len(combined_lists)) # print the total of guests from both husband and wife guest list

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
            break
        case "4":
            see_total_count()
        case "5":
            goodbye_message()
            break

