employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Amit', 'age': 30, 'department': 'IT', 'salary': 60000}
}

def add_employee():
    emp_id = int(input("Enter Employee ID: "))

    if emp_id in employees:
        print("ID already exists!")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print("Employee added successfully!")

def view_employees():
    if not employees:
        print("No employees available.")
        return

    print("\nID\tName\tAge\tDepartment\tSalary")
    print("-"*50)

    for emp_id, data in employees.items():
        print(emp_id, data['name'], data['age'], data['department'], data['salary'])

def search_employee():
    emp_id = int(input("Enter Employee ID: "))

    if emp_id in employees:
        print(employees[emp_id])
    else:
        print("Employee not found.")

# ⭐ NEW FUNCTION
def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))

    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")

# ⭐ NEW FUNCTION
def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))

    if emp_id in employees:
        print("1. Name\n2. Age\n3. Department\n4. Salary")
        choice = input("What do you want to update? ")

        if choice == "1":
            employees[emp_id]['name'] = input("Enter new name: ")
        elif choice == "2":
            employees[emp_id]['age'] = int(input("Enter new age: "))
        elif choice == "3":
            employees[emp_id]['department'] = input("Enter new department: ")
        elif choice == "4":
            employees[emp_id]['salary'] = float(input("Enter new salary: "))
        else:
            print("Invalid choice!")
            return

        print("Employee updated successfully!")
    else:
        print("Employee not found.")

def main_menu():
    while True:
        print("\n===== EMS =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Update Employee")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            update_employee()
        elif choice == "6":
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid choice!")

main_menu()
