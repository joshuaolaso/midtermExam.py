def display_data(data):
    """Display the current data entries."""
    if not data:
        print("No data available.")
    else:
        print("Current Data Entries:")
        for index, entry in enumerate(data):
            print(f"{index + 1}: {entry}")

def main():
    data = []  # Initialize an empty list to store data entries
    
    while True:
        print("\nChoose an action:")
        print("1. Add a single data entry")
        print("2. Add multiple data entries")
        print("3. Display data")
        print("4. Delete data")
        print("5. Update data")
        print("6. Reverse data")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            entry = input("Enter the data entry: ")
            data.append(entry)
            print(f"Added: {entry}")
        
        elif choice == '2':
            entries = input("Enter multiple data entries separated by commas: ")
            entries_list = [entry.strip() for entry in entries.split(',')]
            data.extend(entries_list)
            print(f"Added: {entries_list}")
        
        elif choice == '3':
            display_data(data)
        
        elif choice == '4':
            display_data(data)
            try:
                index = int(input("Enter the index of the entry to delete (1-based index): ")) - 1
                if 0 <= index < len(data):
                    removed_entry = data.pop(index)
                    print(f"Deleted: {removed_entry}")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '5':
            display_data(data)
            try:
                index = int(input("Enter the index of the entry to update (1-based index): ")) - 1
                if 0 <= index < len(data):
                    new_entry = input("Enter the new data entry: ")
                    data[index] = new_entry
                    print(f"Updated index {index + 1} to: {new_entry}")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '6':
            data.reverse()
            print("Data has been reversed.")
        
        elif choice == '7':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()