def add_note(note):
    with open("notes.txt", "a") as f:
        f.write(notes + "\n")

def view_notes():
    with open("notes.txt", "r") as f:
        print(f.read())

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