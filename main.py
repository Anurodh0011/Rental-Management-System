from read import *
from operations import *

def display_main():
        print("***************************************************************")
        print("           Welcome to Techno Property Nepal                    ")
        print("---------------------------------------------------------------")
        print("               trusted service provider                        ")
        print("***************************************************************")
        print("\n Please select an option:")
        print("1. Enter 1 to Rent land")
        print("2. Enter 2 to Return land")
        print("3. Enter 3 to Exit")
        

        

def main():
    lands = read_lands("lands.txt")
    
    while True:

        display_main()
        choice = input("\nSelect your choice : ")
        if choice == "1":
            land_rent(lands)
        elif choice == "2":
            return_land(lands)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("\nInvalid choice. Please enter valid choice.\n")


if __name__ == "__main__":
    main()
