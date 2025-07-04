#!/usr/bin/env python3
"""
A simple command-line shopping list manager.
"""

def display_menu():
    """Prints the main menu options to the console."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list manager application."""
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added to the list.")
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"Item not found.")
        elif choice == '3':
            print("\n--- Shopping List ---")
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                for idx, item_in_list in enumerate(shopping_list, 1):
                    print(f"{idx}. {item_in_list}")
            print("---------------------")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
