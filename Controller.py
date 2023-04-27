import datetime
import Functions as f
import View

def run():
    user_command = ''
    while user_command != '5':
        View.menu()
        user_command = input().strip()
        if user_command == '1':
            f.display_notes(f.load_notes())
        if user_command == '2':
            f.add_note()
        if user_command == '3':
            f.delete_note()
        if user_command == '4':
            f.edit_note()
        if user_command == '5':
            View.goodbuy()
            break