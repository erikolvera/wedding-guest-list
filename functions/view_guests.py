from functions.data import grooms_list, brides_list

#case 3
def view_guest_names():
    view_lists = input("View the groom's or bride's list? Enter 1 or 2 "
                        "\n 1. Groom "
                        "\n 2. Bride \n" )
    if view_lists == "1":
        print(grooms_list)
    elif view_lists == "2":
        print(brides_list)
    else:
        print("Invalid choice: Enter 1 or 2")
    
    # print(grooms_list + brides_list)
