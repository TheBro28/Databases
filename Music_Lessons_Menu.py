# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'Music_Lessons.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

menu_choice =""
while menu_choice != 'Z':
    menu_choice = input('Welcome to the music lesson database\n\n'
                        'Type the letter for the information you want to see:\n'
                        'A - Children with lessons on Mondays\n'
                        'B - Children with lessons on Wednesdays\n'
                        'C - Parents who owe money\n'
                        'D - Parent and child personal information\n'
                        'Z - Exit\n\n'
                        'Type option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query("Children with lessons on Mondays")
    elif menu_choice == 'B':
        print_query("Children with lessons on Wednesdays")
    elif menu_choice == 'C':
        print_query("Parents who owe money")
    elif menu_choice == 'D':
        print_query("Personal parent and child information")
    elif menu_choice == 'E':
        print_query("All male students on a Monday, Wednesday, Friday")
    elif menu_choice == 'Z':
        print('Goodbye')
    else:
        print('Invalid choice, please try again')