def shapemain(attempts):
    if attempts == 6:
        print("""
                |
                |
                |
                |
                |
            """)
    elif attempts == 5:
        print("""
                |---0
                |
                |
                |
                |
            """)
    elif attempts == 4:
        print("""
                |---0
                |   ^ 
                |
                |
                |
            """)    
    elif attempts == 3:
        print("""
                |---0
                |   ^ 
                |   |
                |
                |
            """)    
    elif attempts == 2:
        print("""
                |---0
                |   ^ 
                |   |
                |   ^
                |
            """)    
    elif attempts == 1:
        print("""
                |---0
                |   ^ 
                |   |
                |   ^
                |
                ^
            """)    
    elif attempts == 0:
        print("""
                |---0
                |   ^ 
                |   |
                |   ^
                |
                ^
                ^
            """)   

       
def hangman():
    word = input("Enter word to guess: ")
    word_length = len(word)
    guessed_word = ["_"] * word_length
    guessed_letters = []
    attempts = 6

    print("Let's play Hangman!")
    print(" ".join(guessed_word))

    while attempts > 0:
        guess = input("Guess a word: ").lower()

        if guess in guessed_letters:
            print("You already guessed this letter. Try again!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
            shapemain(attempts)

        else:
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
            print(" ".join(guessed_word))

        if "_" not in guessed_word:
            print("Congratulations! You won!")
            break

    if attempts == 0:
        print(f"Game over! The word was {word}.")
        shapemain(attempts)
        
hangman()