my_dict = {
    "hello": "world",
    "foo": "bar",
    "age": 26
}

print(my_dict.items())

for key,value in my_dict.items():
    print(f"{key}={value}")