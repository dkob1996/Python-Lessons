import json
import datetime

# empty list of notes
notes = []


# save notes in json file
def save_notes():
    try:
        with open("SemSummaryWork/notes.json", "w") as f:
            json.dump(notes, f, indent=4)
    except FileNotFoundError:
        print("File doesn't found")


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
    date_of_edit =""
    simpleYear = timestamp[0:4]
    simpleMonth = timestamp[5:7]
    simpleDay = timestamp[8:10]
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp,
        "date_of_edit": date_of_edit,
        "simpleYear": simpleYear,
        "simpleMonth": simpleMonth,
        "simpleDay": simpleDay
    }
    notes.append(note)
    print(f"Note was added with id: {len(notes)}")
    save_notes()


# delete note and save list of notes
def delete_note():
    try:
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
    except ValueError:
        print('Incorrect format of id')


# clear json file
def delete_all_notes():
    if len(notes) != 0:
            active = True
            while active:
                if len(notes) != 0:
                    for note in notes:
                        notes.remove(note)
                        save_notes()
                else:
                    active = False
    else:
        print("Notes list is empty")


# print note from list of notes
def print_notes():
    if len(notes) != 0:
        for note in notes:
            simple_print(note)
    else:
        print("Notes list is empty")


# print ceratain one note
def print_certain_note():
    try:
        note_id = int(input("Enter note id to print: "))
        if len(notes) != 0:
            for note in notes:
                if note["id"] == note_id:
                    simple_print(note)
                    break
                else:
                    print("This note doesn't exist")
        else:
            print("Notes list is empty")
    except ValueError:
        print('Incorrect format of id')


# structure for print notes
def simple_print(note):
    print(f"{note['id']}: {note['title']}")
    print(note["body"])
    print(f"(creation date: {note['timestamp']})")
    if (len(note['date_of_edit']) != 0):
        print(f"(edition date: {note['date_of_edit']})")
    print()


# filter by start year to end year, or from infinity to end, or form start to infinity
def filter_by_year():
    print("Year format - XXXX")
    year_start = input("Enter start year or press Enter: ")
    year_end = input("Enter end year or press Enter: ")
    lenYearStart = len(year_start)
    lenYearEnd = len(year_end)
    try:
        if (lenYearStart == 0) and (lenYearEnd == 0):
            print("All task:")
            print_notes()
        elif (lenYearStart != 0) and (lenYearEnd ==0 ):
            if (lenYearStart != 4) or (int(year_start) < 0):
                print("Inorrect year format from notice")
            else:
                for note in notes:
                    if int(note["simpleYear"]) == int(year_start):
                        simple_print(note)
                    elif int(note["simpleYear"]) > int(year_start):
                        simple_print(note)
                    elif int(note["simpleYear"]) < int(year_start):
                        continue
                else:
                    print("End of notes list")
        elif (lenYearStart == 0) and (lenYearEnd != 0):
            if (lenYearEnd != 4) or (int(year_end) < 0):
                print("Incorrect year format from notice")
            else:
                for note in notes:
                    if int(note["simpleYear"]) == int(year_end):
                        simple_print(note)
                    elif int(note["simpleYear"]) > int(year_end):
                        continue
                    elif int(note["simpleYear"]) < int(year_end):
                        simple_print(note)
                else:
                    print("End of notes list")
        elif (lenYearStart != 0) and (lenYearEnd != 0):
            if (lenYearStart != 4) or (lenYearEnd != 4) or (int(year_start) > 0 < int(year_end)):
                print("Incorrect year format from notice")
            else:
                intYearStart = int(year_start)
                intYearEnd = int(year_end)
                if intYearStart > intYearEnd:
                    print("Start cannot be later than end year")
                else:
                    for note in notes:
                        if (int(note["simpleYear"]) == int(year_start)) and (int(note["simpleYear"]) == int(year_end)):
                            simple_print(note)
                        elif (int(note["simpleYear"]) > int(year_start)) and (int(note["simpleYear"]) == int(year_end)):
                            simple_print(note)
                        elif (int(note["simpleYear"]) == int(year_start)) and (int(note["simpleYear"]) < int(year_end)):
                            simple_print(note)
                        elif (int(note["simpleYear"]) > int(year_start)) and (int(note["simpleYear"]) < int(year_end)):
                            simple_print(note)
                    else:
                        print("End of notes list")
    except ValueError:
        print('Incorrect format of year')
    

# filter by months in certain year
def filter_by_month():
    try:
        print("Year format - XXXX")
        CertanYear = input("Enter certain year or press Enter: ")
        lenCertanYear = len(CertanYear)
        if (lenCertanYear == 0):
            print_notes()
        else:
            if (lenCertanYear != 4) or (int(CertanYear) < 0):
                print("Incorrect year format from notice")
            else:
                print("Month format - XX")
                month_start = input("Enter start month or press Enter: ")
                month_end = input("Enter end month or press Enter: ")
                lenMonthStart = len(month_start)
                lenMonthEnd = len(month_end)
                if (lenMonthStart == 0) and (lenMonthEnd == 0):
                    for note in notes:
                        if int(note["simpleYear"]) == int(CertanYear):
                            simple_print(note)
                    else:
                        print("End of notes list")
                if (lenMonthStart != 0) and (lenMonthEnd == 0):
                    if (2 < lenMonthStart < 1) or (12 < int(month_start) < 0):
                        print("Incorrect month format from notice")
                    else:
                        for note in notes:
                            if int(note["simpleYear"]) == int(CertanYear):
                                if int(note["simpleMonth"]) == int(month_start):
                                    simple_print(note)
                                elif int(note["simpleMonth"]) > int(month_start):
                                    simple_print(note)
                                elif int(note["simpleMonth"]) < int(month_start):
                                    continue
                            else:
                                continue
                        else:
                            print("End of notes list")
                elif (lenMonthStart == 0) and (lenMonthEnd != 0):
                    if (2 < lenMonthEnd < 1) or (12 < int(month_end) < 0):
                        print("Incorrect month format from notice")
                    else:
                        for note in notes:
                            if int(note["simpleYear"]) == int(CertanYear):
                                if int(note["simpleMonth"]) == int(month_end):
                                    simple_print(note)
                                elif int(note["simpleMonth"]) > int(month_end):
                                    continue
                                elif int(note["simpleMonth"]) < int(month_end):
                                    simple_print(note)
                            else:
                                continue
                        else:
                            print("End of notes list")
                elif (lenMonthStart != 0) and (lenMonthEnd != 0):
                    if (2 < lenMonthStart < 1) or (2 < lenMonthEnd < 1) or (12 < int(month_start) < 0) or (12 < int(month_end) < 0):
                        print("Incorrect month format from notice")
                    else:
                        intMonthStart = int(month_start)
                        intMonthEnd = int(month_end)
                        if (intMonthStart > intMonthEnd):
                            print("Start cannot be later than end month")
                        else:
                            for note in notes:
                                if int(note["simpleYear"]) == int(CertanYear):
                                    if (int(note["simpleMonth"]) == int(month_start)) and (int(note["simpleMonth"]) == int(month_end)):
                                        simple_print(note)
                                    elif (int(note["simpleMonth"]) > int(month_start)) and (int(note["simpleMonth"]) == int(month_end)):
                                        simple_print(note)
                                    elif (int(note["simpleMonth"]) == int(month_start)) and (int(note["simpleMonth"]) < int(month_end)):
                                        simple_print(note)
                                    elif (int(note["simpleMonth"]) > int(month_start)) and (int(note["simpleMonth"]) < int(month_end)):
                                        simple_print(note)
                                else:
                                    continue
                            else:
                                print("End of notes list")
    except ValueError:
        print('Incorrect format of month')


# filter by days in certain month and year
def filter_by_day():
    try:
        print("Year format - XXXX")
        CertanYear = input("Enter certain year or press Enter: ")
        lenCertanYear = len(CertanYear)
        if (lenCertanYear == 0):
            print_notes()
        else:
            if (lenCertanYear != 4) or (int(CertanYear) < 0):
                print("Incorrect year format from notice")
            else:
                print("Month format - XX")
                CertanMonth = input("Enter certain month: ")
                lenCertanMonth = len(CertanMonth)
                if (lenCertanMonth == 0):
                    for note in notes:
                        if (int(note["simpleYear"]) == int(CertanYear)):
                            simple_print(note)
                    print("End of notes list")
                else:
                    if (2 < lenCertanMonth < 1) or (12 < int(CertanMonth) < 0):
                        print("Incorrect month format from notice")
                    else:
                        print("Day format - XX")
                        day_start = input("Enter start day or press Enter: ")
                        day_end = input("Enter end day or press Enter: ")
                        lenDayStart = len(day_start)
                        lenDayEnd = len(day_end)
                        if (lenDayStart == 0) and (lenDayEnd == 0):
                            for note in notes:
                                if (int(note["simpleYear"]) == int(CertanYear)) and (int(note["simpleMonth"]) == int(CertanMonth)):
                                    simple_print(note)
                            else:
                                print("End of notes list")
                        if (lenDayStart != 0) and (lenDayEnd == 0):
                            if (2 < lenDayStart < 1) or (31 < int(day_start) < 0):
                                print("Incorrect day format from notice")
                            else:
                                for note in notes:
                                    if (int(note["simpleYear"]) == int(CertanYear)) and (int(note["simpleMonth"]) == int(CertanMonth)):
                                        if int(note["simpleDay"]) == int(day_start):
                                            simple_print(note)
                                        elif int(note["simpleDay"]) > int(day_start):
                                            simple_print(note)
                                        elif int(note["simpleDay"]) < int(day_start):
                                            continue
                                    else:
                                        continue
                                else:
                                    print("End of notes list")
                        elif (lenDayStart == 0) and (lenDayEnd != 0):
                            if (2 < lenDayEnd < 1) or (31 < int(day_end) < 0):
                                print("Incorrect day format from notice")
                            else:
                                for note in notes:
                                    if (int(note["simpleYear"]) == int(CertanYear)) and (int(note["simpleMonth"]) == int(CertanMonth)):
                                        if int(note["simpleDay"]) == int(day_end):
                                            simple_print(note)
                                        elif int(note["simpleMonth"]) > int(day_end):
                                            continue
                                        elif int(note["simpleDay"]) < int(day_end):
                                            simple_print(note)
                                    else:
                                        continue
                                else:
                                    print("End of notes list")
                        elif (lenDayStart != 0) and (lenDayEnd != 0):
                            if (2 < lenDayStart < 1) or (2 < lenDayEnd < 1) or (31 < int(day_start) < 0) or (31 < int(day_end) < 0):
                                print("Incorrect month format from notice")
                            else:
                                intDayStart = int(day_start)
                                intDayEnd = int(day_end)
                                if (intDayStart > intDayEnd):
                                    print("Start cannot be later than end day")
                                else:
                                    for note in notes:
                                        if (int(note["simpleYear"]) == int(CertanYear)) and (int(note["simpleMonth"]) == int(CertanMonth)):
                                            if (int(note["simpleDay"]) == int(day_start)) and (int(note["simpleDay"]) == int(day_end)):
                                                simple_print(note)
                                            elif (int(note["simpleDay"]) > int(day_start)) and (int(note["simpleDay"]) == int(day_end)):
                                                simple_print(note)
                                            elif (int(note["simpleDay"]) == int(day_start)) and (int(note["simpleDay"]) < int(day_end)):
                                                simple_print(note)
                                            elif (int(note["simpleDay"]) > int(day_start)) and (int(note["simpleDay"]) < int(day_end)):
                                                simple_print(note)
                                        else:
                                            continue
                                    else:
                                        print("End of notes list")
    except ValueError:
        print('Incorrect format of day')


# edit note from list of notes
def edit_note():
    try:
        note_id = int(input("Enter note id to edit: "))
        if len(notes) != 0:
            for note in notes:
                if note["id"] == note_id:
                    note["title"] = input("Enter new note title: ")
                    note["body"] = input("Enter new note body: ")
                    note["date_of_edit"] = str(datetime.datetime.now())
                    save_notes()
                    break
                else:
                    print("This note doesn't exist")
        else:
            print("Notes list is empty")
    except ValueError:
        print('Incorrect format of id')


# list of commands and start programm
def start_page():
    print("Command notice:")
    print("   add - add task to list (task title, task body)")
    print("   delete - delete certain task from list")
    print("   edit - edit  certain task in list")
    print("   filter - filter tasks by data and print")
    print("   list - print task/tasks from list")
    print("   clear - delete all tasks from list")
    print("   exit - exit from programm")
    while True:
        print("Enter a command: add, delete, edit, filter, list, clear, exit")
        command = input().lower()
        if command == "add":
            create_note()
        elif command == "delete":
            delete_note()
        elif command == "edit":
            edit_note()
        elif command == "list":
            print("Commanddd notice: ")
            print("   all - show all tasks")
            print("   one - show certain task")
            commandList = input().lower()
            if commandList == "all":
                print_notes()
            elif commandList == "one":
                print_certain_note()
            else:
                print("This command doesn't exist")
        elif command == "filter":
            print("Commanddd notice: ")
            print("   y - year - filter by years")
            print("   m - month - filter by months in certain year")
            print("   d - day - filter by days in certain month and year")
            commandFilter = input().lower()
            if (commandFilter == "year") or (commandFilter == "y"):
                filter_by_year()
            elif (commandFilter == "month") or (commandFilter == "m"):
                filter_by_month()
            elif (commandFilter == "day") or (commandFilter == "d"):
                filter_by_day()
            else:
                print("This command doesn't exist")
        elif command == "clear":
            print("Are you sure? All tasks from your list will be deleted!")
            print("Enter YES or NO: ")
            commandClear = input().lower()
            if commandClear == "yes":
                delete_all_notes()
            elif commandClear == "no":
                continue
            else:
                print("This command doesn't exist")
        elif command == "exit":
            break
        else:
            print("This command doesn't exist")


# run load notes frome json file
load_notes()


# run programm
start_page()