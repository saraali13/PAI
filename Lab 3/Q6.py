def askSentence(sentence):
    try:
        if sentence[len(sentence)-1] == '?':
            with open('file4', 'w') as file:
                file.write(sentence)
                print('\nThe sentence was a Question')
        else:
            print('The sentence was Not a Question')

    except Exception as e:
        print(str(e))

sentence = input('Enter the sentence: ')
askSentence(sentence)
