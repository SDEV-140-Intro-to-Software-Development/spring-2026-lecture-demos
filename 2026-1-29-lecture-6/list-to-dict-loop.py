# As an input, I will have a list of users.
# As an output, i need a dictionary of users where the email is the key and the value is the whole user dictionary

def map_users_by_email(users):
    users_dict = {}

    for user in users:
        users_dict[user['email']] = user

    return users_dict

user_list = [
    {
        "id": 12314,
        "name": "Eric Sexton",
        "email": "esexton15@ivytech.edu"
    },
    {
        "id": 51312,
        "name": "John Doe",
        "email": "john@ivytech.edu"
    }
]

users_by_email = map_users_by_email(user_list)
print(users_by_email)