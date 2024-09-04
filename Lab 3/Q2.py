try:
    with open("example", 'r') as file:
        content = file.read()

    NewContent = content.replace("jbw", "chin tapak dam dam")

    with open("example", 'w') as file:
        file.write(NewContent)

    print("Replacement successful.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
