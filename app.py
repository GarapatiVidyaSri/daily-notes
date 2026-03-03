def add_note(note):
    with open("notes.txt", "a") as f:
        f.write(notes + "\n")

def view_notes():
    with open("notes.txt", "r") as f:
        print(f.read())
def delete_functionality():
    return "delete_node"

if __name__ == "__main__":
    while True:
        choice = input("1. Add Note  2. View Notes  3. Exit: ")
        
        if choice == "1":
            note = input("Enter note: ")
            add_note(note)
        elif choice == "2":
            view_notes()
        else:
            break