user1 = {
    "role": "HR"
}

user2 = {
    "role": "Software Developer"
}

def has_access_to_employee_records(role):
    if role == "HR":
        return True
    else:
        return False

def print_employee_records(user):
    if not has_access_to_employee_records(user['role']):
        print("You don't have access")
        return

    print(user1)
    print(user2)


# user is trying to access employee records
print_employee_records(user1)
print_employee_records(user2)