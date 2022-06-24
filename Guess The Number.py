import random   #This allows the use of the "random" function
import sys      #This allows the use of the system.exit function

number_of_guesses = 0
new_game = 0

print("Welcome to the number guessing game!")
player_name = input("What's your name?\n")

print("\nNice to meet you " + player_name)
print("\nPlease enter the range you'd like for the game:\n")
game_version = int(input("\t1) 1 - 10\n"
                     "\t2) 1 - 50\n"
                     "\t3) 1 - 100\n"
                     "\nGame version: "))

while new_game == str("yes"):   #Trying to add an option to restart the game again.

    if game_version == 1:
        number = random.randint(1,10)

        while number_of_guesses < 5:
            print("Enter your guess: ")
            guess = int(input())
            number_of_guesses += 1
        
            if guess < number:
                print("Your guess is too low")
            if guess > number:
                print("Your guess is too high")
            if guess > 10 or guess < 1:
                print("Your guess is out of range")
            if guess == number:
                print("Congratulation! You guessed the number in " + str(number_of_guesses) + " tries")
                print("Thanks for playing")
                new_game = str(input("Would you like to play again? "))
                sys.exit()
        else:
            print("You did not guess the number, the number was " + str(number))
            sys.exit()

    elif game_version == 2:
        number = random.randint(1,50)

        while number_of_guesses < 10:
            print("Enter your guess: ")
            guess = int(input())
            number_of_guesses += 1
        
            if guess < number:
                print("Your guess is too low")
            if guess > number:
                print("Your guess is too high")
            if guess > 50 or guess < 1:
                print("Your guess is out of range")    
            if guess == number:
                print("Congratulation! You guessed the number in " + str(number_of_guesses) + " tries")
                print("Thanks for playing")
                sys.exit()
        else:
            print("You did not guess the number, the number was " + str(number))
            sys.exit()

    elif game_version == 3:
        number = random.randint(1,100)

        while number_of_guesses < 15:
            print("Enter your guess: ")
            guess = int(input())
            number_of_guesses += 1
        
            if guess < number:
                print("Your guess is too low")
            if guess > number:
                print("Your guess is too high")
            if guess > 100 or guess < 1:
                print("Your guess is out of range")    
            if guess == number:
                print("Congratulation! You guessed the number in " + str(number_of_guesses) + " tries")
                print("Thanks for playing")
                sys.exit()
        else:
            print("You did not guess the number, the number was " + str(number))
            sys.exit()
      
