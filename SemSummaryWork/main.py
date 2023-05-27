import json
import datetime

# empty list of notes
notes = []


# save notes in json file
def save_notes():
    with open("SemSummaryWork/notes.json", "w") as f:
        json.dump(notes, f, indent=4)


# load notes from json file
def load_notes():
    global notes
    try:
        with open("SemSummaryWork/notes.json") as f:
            notes = json.load(f)
    except FileNotFoundError:
        pass


# create note and save in json format
def create_note():
    title = input("Enter note title: ")
    body = input("Enter note body: ")
    timestamp = str(datetime.datetime.now())
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp,
    }
    notes.append(note)
    print(f"Note was added with id: {len(notes)}")
    save_notes()


# delete note and save list of notes
def delete_note():
    note_id = int(input("Enter note id to delete: "))
    if len(notes) != 0:
        for note in notes:
            if note["id"] == note_id:
                notes.remove(note)
                save_notes()
                break
            else:
                print("This note doesn't exist")
    else:
        print("Notes list is empty")


# print note from list of notes
def print_notes():
    if len(notes) != 0:
        for note in notes:
            print(f"{note['id']}: {note['title']} ({note['timestamp']})")
            print(note["body"])
            print()
    else:
        print("Notes list is empty")


# edit note from list of notes
def edit_note():
    note_id = int(input("Enter note id to edit: "))
    if len(notes) != 0:
        for note in notes:
            if note["id"] == note_id:
                note["title"] = input("Enter new note title: ")
                note["body"] = input("Enter new note body: ")
                note["timestamp"] = str(datetime.datetime.now())
                save_notes()
                break
            else:
                print("This note doesn't exist")
    else:
        print("Notes list is empty")


# list of commands
def load_notes():
    while True:
        print("Enter a command: add, delete, edit, list, exit")
        command = input().lower()
        if command == "add":
            create_note()
        elif command == "delete":
            delete_note()
        elif command == "edit":
            edit_note()
        elif command == "list":
            print_notes()
        elif command == "exit":
            break
        else:
            print("This command doesn't exist")


# run programm
load_notes()
