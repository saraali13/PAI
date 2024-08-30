def count_words_and_characters(filename):
    with open(filename, 'r') as file:
        text = file.read()

        num_characters = len(text)
        num_words = len(text.split())

        print(f"Number of characters: {num_characters}")
        print(f"Number of words: {num_words}")

count_words_and_characters("samplefile.txt")
#text file should have the same directory as the python project one
