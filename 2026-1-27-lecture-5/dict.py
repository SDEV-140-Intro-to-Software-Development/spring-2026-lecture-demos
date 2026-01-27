caffine_content = {
    "soda": 30,
    "tea": 60,
    "coffee": 95    
}

users = {
    5131141: {
        "id": 5131141, 
        "name": "Eric",
        "posts": [
            {
                "content": "Hey Guys!",
                "post_at": "1/27/2026 14:59"
            } 
        ]
    },
    123415: {
        "id": 123415,
        "name": "Lee",
        "posts": [
            {
                "content": "Hey Guys!",
                "post_at": "1/27/2026 14:59"
            }
        ]
    }
}

def get_users_name(id):
    return users.get(id, { "name": "" }).get("name", "")

def get_all_user_names():
    return [user["name"] for user in users.values()]

def print_all_user_information():
    for user in users.values():
        for key,value in user.items():
            print(f"{key}: {value}")
        print()

print(get_users_name(5131141))
print(get_all_user_names())
print_all_user_information()

# for key in caffine_content.keys():
#     caffine_content[key] = caffine_content[key] * 2

# for item,caffine in caffine_content.items():
#     print(item, caffine)

