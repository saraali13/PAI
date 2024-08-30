def build_message(**info):
    message = ""
    for key, value in info.items():
        message +=f"{key.capitalize()}: {value}, "

    return message

summary = build_message(name="Sara", age=18, city="Karachi")
print(f"Summary Message: {summary}")

