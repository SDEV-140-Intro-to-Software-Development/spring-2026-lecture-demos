english = {
    "country": "United States",
    "langauge": "English",
    "currency": "$"
}

japanese = {
    "country": "日本",
    "langauge": "日本語",
    "currency": "¥"
}

def print_welcome_message(lang_dict):
    print("In %(country)s we speak %(langauge)s" % lang_dict)

def print_price(lang):
    print("%(currency)s50" % lang)

# some logic to determine user langauge

print_welcome_message(english)
print_welcome_message(japanese)
print_price(english)
print_price(japanese)