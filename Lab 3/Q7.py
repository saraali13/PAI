def replace_letter(letter_x,letter_y):
    try:
        with open('replacement_needed.txt', 'r') as file:
            content = file.read()
            print(f"The original content is:\n{content}")

        new_content = content.replace(letter_x, letter_y)

        with open('replacement_needed.txt', 'w') as file:
            file.write(new_content)

        print("File updated successfully")
        print(f"The Updated content is:\n{new_content}")
    except FileNotFoundError:
        print("The file not found")
    except Exception as e:
        print("Error: ", e)


replace_letter("z","e")
