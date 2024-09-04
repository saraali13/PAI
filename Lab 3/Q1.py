try:
    with open("example", 'r') as file:
        character_count = 0
        word_count = 0


        for i in file:
            character_count += len(i)
            word_count += len(i.split())

    print(f"Total characters: {character_count}")
    print(f"Total words: {word_count}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
