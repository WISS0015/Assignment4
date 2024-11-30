#WISS0015
import random #This will be used to randomly pick a word from the wordbank


#Word bank for the game
Wordbank = {1: "table", 2: "grape", 3: "crane", 4: "plant",
            5: "stone", 6: "apple", 7: "bread", 8: "flame", 9: "chair", 10: "plane"}

random_number = random.randint(1,10) #this will be used to choose the dictionary key from 1-10 randomly
random_word = Wordbank[random_number] #Selecting a random word from the dictionary for the game

def game():
    print ("Welcome to the guess the word game, all words are 5 letters or less. To exit the game, type end")

    #print(random_word) #For testing!!

    Guess = ""
    while True:
        Guess = input("Please enter a 5 letter word, your guess will identify the letters you mentioned: ")
        if Guess == "end": #This is to exit the game
            print("-------Ending game!--------")
            break

        if len(Guess) != len(random_word):
            #This will restart the guess, if the word is not 5 letters long
            print("The word must be 5 letters long, please try again!")
            continue

        if Guess == random_word: #if the word is guessed perfectly, then it ends the game, printing well done
            print("Well done! You have guessed the correct word!")
            break

        position = 0
        if len(Guess) == len(random_word):
            for letter in Guess: #checks each value to see if the letter guessed is in that position
                    if letter == random_word[position]: #This will say if the letter is in that position
                        print(letter + " is the number" , (position+1) , "letter in the word")

                    if letter in random_word: #checks if the letter is in the word
                        print(letter + " is in the word, but not in the correct position")

                    if letter not in random_word:#if not in word, then it will print that it's not in the word
                        print(letter + " is not in the word")

                    position += 1



game()
