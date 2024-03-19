'''Notes:
1) Use the following username and password to access the admin rights
Username: admin
Password: password
2) Ensure you open the whole folder for this task in VS Code otherwise the
program will look in your root directory for the text files.'''

# ---- Import required libraries ----
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't already exist.
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", 'w') as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


# menu = defining a function to display user menu.
def menu():
    while True:
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
        print()
        menu = input('''
Select one of the following Options below:
__________________________________________
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
__________________________________________
: ''').lower()
        
        if menu == 'r':
            # Call reg_user to register user.
            reg_user()
        
        elif menu == 'a':
            # Call add_task to add task.
            add_task()

        elif menu == 'va':
            # Call view_all to view all tasks.
            view_all()

        elif menu == 'vm':
            # Call view_mine to view user assigned tasks.
            view_mine()

        elif menu == 'gr':
            # Call generate_reports to generate task and user reports.
            generate_reports()
        
        elif menu == 'ds':
            if curr_user == 'admin': 
                # Call display_statistics if the user is an admin they can display
                # statistics about number of users and tasks.
                display_statistics()
            
            else:
                print("User not a administrator, please log in as administrator.")

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")


# reg_user = defining a function to add a new user.
def reg_user():
    # Add a new user to the user.txt file, via new username.
    new_username = input("Please enter a new username to add: ")

    # Check username not already registered
    if new_username in username_password.keys():
        print("Invalid choice, username already taken.")
        # Check if user wishes to return to menu.
        return_menu = input("Return to the menu? yes / no: \n")
        if return_menu.lower() == "yes":
            return("Returning to menu.")
        
        else:
            new_username = input("Please enter another username: ")
    
    # Request input of password for new user.
    new_password = input("Please enter a password: ")

    # Request confirmation of new user password.
    confirm_password = input("Please enter again to confirm password: ")

    # Confirm new password & confirmed password match.
    if new_password == confirm_password:
        # If they match add to user.txt file.
        username_password[new_username] = new_password

        with open("user.txt", 'w') as out_file:
            user_data = []
            for key in username_password:
                user_data.append(f"{key};{username_password[key]}")
            out_file.write("\n".join(user_data))
        print("New user successfully registered.")
    # If they don't match print relevant error message.
    else:
        print("Passwords do not match, try again.")


# add_task = add a new task when user selects 'a'
def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.'''
    
    task_username = input("Name of person assigned to task: ")
    while task_username not in username_password.keys():
        print("User does not exist.")
        task_username = input("Please enter a valid username: ")
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    return "Task successfully added."


# view_all = view all tasks in 'tasks.txt' when user selects 'va'
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
       format of Output 2 presented in the task pdf (i.e. includes spacing
       and labelling)'''
    for task in task_list:
        disp_str = f'''
___________________________________________________________
Task: \t\t {task['title']}
Assigned to: \t {task['username']}
Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}
Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}
Task Description: \n {task['description']}
___________________________________________________________'''
        print(disp_str)


# view_mine = view all tasks assigned to user when user selects 'vm'
def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)'''
    for item, task in enumerate(task_list, 1):
        if task['username'] == curr_user:
            disp_str = f'''      
___________________________________________________________
Task {item}: \t {task['title']}
Assigned to: \t {task['username']}
Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}
Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}
Task Description: \n {task['description']}
___________________________________________________________'''
            print(disp_str)

    # Request user to select a task to modify.
    task_selection = int(input('''Please select a task to modify,
or enter '-1' to return to main menu: \n'''))
    # Allow -1 selection to return user to main menu.
    if task_selection == -1:
        return("Returning to main menu.")

    else:
        # Ask user if they wish to mark as complete or edit task..
        task_complete_edit = int(input('''
___________________________________
Please select one of the following:
1) Mark task as complete.
2) Mark task as incomplete.
3) Edit task.
___________________________________
'''))
        # Mark the task as complete.
        if task_complete_edit == 1:
            # Mark the task as complete.
	        # Edit task list
            task_list[task_selection - 1]["completed"] = True
	        # Edit task.txt file by calling function.
            task_complete_incomplete()           

        # Mark the task as incomplete.
        elif task_complete_edit == 2:
            # Mark the task as incomplete.
            # Edit task list
            task_list[task_selection - 1]["completed"] = False
            # Edit task.txt file by calling function.
            task_complete_incomplete()

        # Editing a task.
        elif task_complete_edit == 3:
            # Check if task is already completed.
            # If complete user is unable to make changes.
            if task_list[task_selection - 1]["completed"] == True:
                print("Task complete cannot modify, returning to main menu.")
                return

            else:
		    # Check with user if want to change the user assigned to task or due date.
                username_or_date = int(input('''
___________________________________________
Please select one of the following options:
1) Change the user assigned to the task.
2) Change the due date of the task.
___________________________________________
'''))
                # Change to user assign to the task.
                if username_or_date == 1:
                    # Edit the username of a task.
	                # Make sure the username is valid and in username dictionary via while loop.
                    new_username = input("Enter the username to assign the task to: ")
                    while new_username not in username_password.keys():
                        new_username = input("Username invalid, please try again: ")
        
                    # Update username in task list.
                    task_list[task_selection - 1]["username"] = new_username
                    # Edit task.txt file
                    with open("tasks.txt", 'w') as task_file:
                        task_list_to_write = []
                        for t in task_list:
                            str_atters = [
                                t['username'],
                                t['title'],
                                t['description'],
                                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                "Yes" if t['completed'] else "No"
                            ]
                            task_list_to_write.append(";".join(str_atters))
                        task_file.write("\n".join(task_list_to_write))
                    print ("Username updated, returning to main menu.")
                    return

                # Change the due date of the task.
                elif username_or_date == 2:
                    # Edit the due date of the task.
	                # Make sure the new due date is in a valid format.
                    while True:
                        try:
                            new_due_date = input("Enter the new due date for the task (YYYY-MM-DD): ")
                            new_due_date_time = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                            break
                        except ValueError:
                            print("Invalid datetime format. Please use specified format.")
                    # Update the due date in task list.
                    task_list[task_selection - 1]["due_date"] = new_due_date_time
                    # Edit task.txt file.
                    with open("tasks.txt", 'w') as task_file:
                        task_list_to_write = []
                        for t in task_list:
                            str_attrs = [
                                t['username'],
                                t['title'],
                                t['description'],
                                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                "Yes" if t['completed'] else "No"
                            ]
                            task_list_to_write.append(";".join(str_attrs))
                        task_file.write("\n".join(task_list_to_write))
                    print("Due date updated, returning to main menu.")
                    return   
                
                else:
                    print("Invalid input, returning to main menu.")
                    return
        else:
            print("Invlaid input, returning to main menu.")
            return   


def task_complete_incomplete():
    # Edit task.txt file.
    with open("tasks.txt", 'w') as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
				t['username'],
        	    t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
    	        t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
			]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task updated, returning to main menu.")
    return  


# generate_reports = to generate task and user reports.
def generate_reports():
    # When generating reports two text files should be generated.
    # task_overview.txt and user_overview.txt

    # Call task_overview function to generate task_overview.txt.
    task_overview()

    # Call task_overview function to generate task_overview.txt.
    user_overview()


# task_overview = Defining a function for task_overview.txt generation.
def task_overview():
    # task_overview.txt, defining required variables:
    # Total number of tasks generated and tracked
    total_tasks = len(task_list)
    # Total number of completed tasks.
    total_complete_tasks = 0
    # Total number of incomplete tasks.
    total_incomplete_tasks = 0
    # Total number of tasks incomplete and overdue.
    total_incomplete_overdue_tasks = 0

    # Create loop for task_list to check  if task complete or overdue to current date
    current_date = datetime.now()
    for task in task_list:
        if task['completed'] == True:
            total_complete_tasks += 1
        elif task['completed'] == False and task['due_date'] < current_date:
            total_incomplete_tasks += 1
            total_incomplete_overdue_tasks += 1
        else:
            total_incomplete_tasks += 1 
    # Percentage of tasks that are incomplete to 1 decimal place.
    percent_incomplete = round((total_complete_tasks / total_tasks) * 100, 1)
    # Percentage of tasks that are overdue to 1 decimal place.
    percent_overdue = round((total_incomplete_overdue_tasks / total_tasks) * 100, 1)

    # Creating dictionary to store task reports in.
    task_report_dict = {
        'tasks': total_tasks,
        'tasks_complete': total_complete_tasks,
        'tasks_incomplete': total_incomplete_tasks,
        'tasks_incomplete_overdue': total_incomplete_overdue_tasks,
        'percent_incomplete': percent_incomplete,
        'percent_overdue': percent_overdue
    }

    # Write task_report_dict to task_overview.txt.
    with open("task_overview.txt", 'w') as task_reports:
        task_reports.write(f"""
______________________________________________________________________________
Task overview:
______________________________________________________________________________
Total number of tasks: \t\t\t\t\t\t\t{task_report_dict['tasks']}
Total number of completed tasks: \t\t\t\t{task_report_dict['tasks_complete']}
Total number of incomplete tasks: \t\t\t\t{task_report_dict['tasks_incomplete']}
Total number of incomplete and overdue tasks: \t{task_report_dict['tasks_incomplete_overdue']}
Percentage of incomplete tasks: \t\t\t\t{task_report_dict['percent_incomplete']}
Percentage of incomplete and overdue tasks: \t{task_report_dict['percent_overdue']}
______________________________________________________________________________
        """)
        print("Task overview report generated.")


# user_overview = Defining a function for user_overview.txt generation.
def user_overview():
    # user_overview, defining required variables:
    # Total number of tasks generated and tracked
    total_tasks = len(task_list)
    # Total number over users registered in task_manager.py
    total_users = len(username_password.keys())
    # Creating new text file user_overview.txt and writing user overview to it.
    with open("user_overview.txt", 'w') as user_reports:
    # Total number of tasks that have been generated and tracked in task_manager.py
        user_reports.write(f"""
______________________________________________________________________________
User overview:
______________________________________________________________________________
Total number of users: \t {total_users}
Total number of tasks: \t {total_tasks}
______________________________________________________________________________                           
""")

    # For each user:
        # Total number of tasks assigned.
        # Percentage of the total number of tasks assigned to that user.
        # Percentage of tasks assign to the user that are completed.
        # Percentage of tasks assign to the user that are incomplete.
        # Percentage of tasks assign to the user that are incomplete and overdue.
    for user in username_password.keys():
        # Total number of users tasks.
        user_total_tasks = 0
        # Total number of users completed tasks.
        user_total_complete_tasks = 0
        # Total number of users incompleted tasks.
        user_total_incomplete_tasks = 0
        # Total number of tasks incomplete and overdue.
        user_total_incomplete_overdue_tasks = 0
        # Create loop for task_list to check  if task complete or overdue to current date
        current_date = datetime.now()
        for task in task_list:
            if task['username'] == user:
                user_total_tasks += 1
                if task['completed'] == True:
                    user_total_complete_tasks += 1
                elif task['completed'] == False and task['due_date'] < current_date:
                    user_total_incomplete_tasks += 1
                    user_total_incomplete_overdue_tasks += 1
                else:
                    user_total_incomplete_tasks += 1
        # Calculate the percentage of tasks assigned to the user to 1 decimal place.
        user_percent_tasks = round((user_total_tasks / total_tasks) * 100, 1)
        # Percentage of tasks that are incomplete to 1 decimal place.
        user_percent_complete = round((user_total_complete_tasks / user_total_tasks) * 100, 1)
        # Percentage of tasks that are overdue to 1 decimal place.
        user_percent_overdue = round((user_total_incomplete_overdue_tasks / user_total_tasks) * 100, 1)

        # Write user tasks to user_overview.txt.
        with open("user_overview.txt", 'a') as user_reports:
            user_reports.write(f"""
______________________________________________________________________________
User: {user.upper()}
______________________________________________________________________________
Total number of tasks: \t\t\t\t\t\t\t{user_total_tasks}
Percentage of completed tasks: \t\t\t\t\t{user_percent_complete}
Percentage of incomplete tasks: \t\t\t\t{100 - user_percent_tasks}
Percentage of incomplete and overdue tasks: \t{user_percent_overdue}
______________________________________________________________________________
\n""")
    print("Task overview and user overview report generated.")


# display_statistics = 
def display_statistics():
    # Printing out task_overview.txt in user friendly manner.
    input_file = "task_overview.txt"
    output_file = "task_overview_display.txt"
    # Open input file in read mode.
    with open(input_file, "r+") as file:
        lines = file.readlines()
    
    # Open output file in write mode to save modified content, removing tabs.
    with open(output_file, 'w') as file:
        for line in lines:
            new_line = line.replace('\t', '')
            file.write(new_line)

    # Printing modified file
    with open(output_file, 'r') as file:
        print(file.read())

    # Printing out user_overview.txt in user friendly manner.
    input_file = "user_overview.txt"
    output_file = "user_overview_display.txt"
    # Open input file in read mode.
    with open(input_file, "r+") as file:
        lines = file.readlines()

    # Open output file in write mode to save modified content, removing tabs.   
    with open(output_file, 'w') as file:
        for line in lines:
            new_line = line.replace('\t', '')
            file.write(new_line)

    # Printing modified file
    with open(output_file, 'r') as file:
        print(file.read())


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
# This code reads usernames and password from the user.txt file to 
# allow a user to login.

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:
    print("""
LOGIN SCREEN
_______________________________________
""")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    print("""_______________________________________""")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True
        # If login successful display menu to user.
        menu()
