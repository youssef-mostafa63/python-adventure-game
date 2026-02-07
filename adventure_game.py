# Import time library to pause the game for a period between statements.
import time
# Import random library to add some random factors.
import random
# Import a function from Pyfiglet library to format text in a beautiful style.
from pyfiglet import figlet_format

# Defining a function to pause the game for 3 seconds after print the text.
def print_with_pause (text:str, time_to_pause:int = 3):
    """pause the game for seconds after the text has been printed.

    Args:
        text (str): the text to print.
        time_to_pause (int): number of seconds to pause (default: 3).
    """

    print(f"\n{text}")
    time.sleep(time_to_pause)

# A random place where the player will start the game.
random_place=random.choice(["city's castle","king's palace","princess palace"])

# The scenario of the beginning of the game.
def start_game():
    """The player will see where he is and start his journy to escape.
    """
    # Print the title of the game with a format from Pyfiglet library.
    print_with_pause("Welcome to ....")
    print_with_pause(figlet_format("Escape From The Middle Ages"), 5)

    # Writing the scenario.
    print_with_pause(f"In the middle ages, you find yourself wrongly \
imprisoned in a {random_place}, sentenced to death.", 5)

    print_with_pause("You must escape before the sentence is carried out.")
    print_with_pause(f"You are looking for escape opportunities within the \
{random_place}\nwhether finding an exit or seeking \
help from the other prisoners.", 5)

    print_with_pause(f"When you get out of the {random_place}, you can \
go back to your era in the 21th century through the portal of time")

    print_with_pause(f"You have {total_score} points")
    print_with_pause("If your score becomes zero you will lose the game")
    print_with_pause(f"When your score becomes 10 you can cast a spell with an\
 old magical wand you found in the {random_place} prison.", 5)

    print_with_pause(f"The spell can get you out of the {random_place}")
    print_with_pause(f"When you get out of the {random_place}, \
a time portal will appear in front of you, taking you to the current era.")

    print_with_pause("The old magical wand is hidden inside your shoes")
    print_with_pause(f"Your friend in the prison told you that there is an \
opening in a wall leads to a tunnel leading outside the {random_place}", 4)

    print_with_pause(f"The {random_place} soldiers are transporting \
you from the prison to the courtyard of \
the {random_place} to carry out the death sentence", 4)

    print_with_pause("You were able to break the chains tied around \
your hands but you hid that from the soldiers", 4)

    print_with_pause("You can pull out the dagger of the soldier holding \
you and stab him [1]\nOr you can just run away [2]", 4)

    print_with_pause(f"Your score now: {total_score}")

# A function to print the scenario when run away from the sodiers.
def when_run_away():
    """When the player run away from soldiers he will lose the game.
    """
    print_with_pause("You run away to look for the tunnel entrance")
    print_with_pause("One of the soldiers shot you with an arrow in \
your leg and you fell to the ground")

    print_with_pause("They took you to the courtyard and \
carry out the sentence")

    # To modify the variable "total_score" inside the function.
    global total_score
    total_score = 0
    print_with_pause(f"Your score: {total_score}")


# The scenario if the player pull out the dagger of the soldier and stab him.
def when_stab_soldier():
    """The things that will happens after the player stabs the soldier.
    """

    # To modify the variable "total_score" inside the function.
    global total_score

    print_with_pause("You stabbed the soldier holding you in the shoulder \
and ran away, the other soldiers were surprised and could not catch you", 4)

    # Choose the room owner randomly.
    random_room_owner =random.choice(["prince", "cooking", "princess", "maid"])

    print_with_pause(f"You fled to one of the {random_place}'s large rooms \
and hid there .... this is the room of the {random_room_owner} \
in the {random_place}", 5)

    total_score += 2
    print_with_pause(f"Nice work! you got 2 points\nYour score: {total_score}")

    # If the score becomes 10 the player can use the
    # magic wand and the function will stop.
    if total_score >= 10:
        return "Now you can use your magical wand"

    print_with_pause("In front of you there is a soldier uniform hanged \
near the door and your eyes fall on a map on a table", 4)

    print_with_pause("Suddenly, you hear raised voices and the sound \
of footsteps approaching the room.", 4)

    print_with_pause("You can look for a place to hide [1]")
    print_with_pause("Or you can disguise yourself as a soldier [2]")
    print_with_pause(f"Your score now: {total_score}")

    choice2 = input("\nWhat would you like to do. Enter 1 or 2 : ")

    # The loop will works until the user enters 1 or 2
    while choice2 not in ["1", "2"]:
        choice2 = input("Invalid choice, please type 1 or 2 : ")

    if choice2 == "2":
        # Call the function when the player choose to dusguise as a soldier.
        when_disguise()

    else:
        # Call the function when the player choose to hide in the room.
        when_hide()


# The scenario if the player disguise himself as a soldier.
def when_disguise():
    """Things that will happens when the player try to disguise as a soldier.
    """
    print_with_pause("You quickly put on the soldier's uniform \
and the helmet so that no one knows you")

    print_with_pause("The sounds of footsteps get closer .... \
the tension increases", 4)

    print_with_pause("The door opens ............", 4)
    print_with_pause("The tension is increasing more and more .......", 5)

    print_with_pause(f"This is the {random_place} maid, \
It looks like she came to clean the room")

    print_with_pause("The maid : Let me clean this room, sir")
    print_with_pause("You : Of course!")
    print_with_pause(f"And you quickly leave the room with \
the map you found and walk into the corridors of the large {random_place}", 5)

    # To modify the variable "total_score" inside the function.
    global total_score
    total_score += 2
    print_with_pause("Good job! +2 points ")
    print(f"Your score : {total_score}")

    if total_score >= 10:
        return "Now you can use your magical wand"

    print_with_pause(f"You open the map and find that this is the map \
of the secret tunnels in the {random_place}!", 4)

    print_with_pause("You chose to exit through the tunnel that your friend \
told you about because it is the closest to you now", 5)

    print_with_pause("You go to the location of the tunnel opening, \
but when you arrive,\nYou find that there are three guards guarding the secret\
 tunnel.", 6)


    print_with_pause("You can confront the guards with the dagger \
and sword you have in the soldier,s suit [1]", 4)

    print_with_pause("Or you can try to fool them into \
believing that you are a soldier [2]")

    print_with_pause(f"Your score now: {total_score}")

    choice3 = input("\nWhat would you like to do. Enter 1 or 2 : ")

    # The loop will works until the user enters 1 or 2
    while choice3 not in ["1", "2"]:
        choice3 = input("Invalid choice, please type 1 or 2 : ")

    if choice3 == "1":
        #Call the function when the player chose to confront the tunnel guards.
        confront_tunnel_guards()

    else:
        #Call the function when the player chose to deceive the tunnel guards.
        deceive_tunnel_guards()


# The scenario if the player hide himself in the room.
def when_hide():
    """Things that will happen if the player choose to hide in the room.
    """
    # To modify the variable "total_score" inside the function.
    global total_score

    print_with_pause(f"Your score now is: {total_score}")
    print_with_pause("You are looking for a place to hide, \
but the room is empty and there is not much furniture", 4)

    print_with_pause("You hid behind a large box in the corner of the room")
    print_with_pause("The sounds of footsteps get closer .... \
the tension increases", 4)

    print_with_pause("The door opens ............")
    print_with_pause("You try to look to see who came ...", 6)

    # Choose the person who will enter the room randomly.
    random_person = random.choice([f"maid of the {random_place}","young \
girl",f"princess of the {random_place}"])

    print_with_pause(f"This is the {random_person} you saw before\
in the {random_place}")

    print_with_pause("When she entered the room, she saw you \
behind the box and she scream loudly")

    print_with_pause("Then ran to tell the guards that \
she saw one of the prisoners in the room.")

    print_with_pause("The guards came into the room at the \
same time you were leaving")

    print_with_pause("When the guards saw you, you ran as \
fast as possible. And the soldiers started chasing you", 4)

    total_score -= 2
    print_with_pause(f"You lost 2 points, Your score : {total_score}")

    print_with_pause("You narrowly escaped from the guards to a safe place")
    print_with_pause("You opened the map you took from the room")
    print_with_pause("You see that the tunnel is very close to you now")

    print_with_pause("You can go back to the room after the soldiers leave it \
to disguise yourself as a soldier [1]", 2)

    print_with_pause("Or you can complete your path to find the tunnel [2]")
    print_with_pause(f"Your score now is: {total_score}")

    choice_hidden =input("\nWhat would you like to do\nEnter 1 or 2: ")

    # The loop will works until the player types 1 or 2.
    while choice_hidden not in ["1", "2"]:
        choice_hidden = input("Invalid choice, please type 1 or 2 : ")

    if choice_hidden == "1":
        print("\nYou returned back to the room ....")
        when_disguise()
    else:
        complete_path_to_tunnel()

# The scenario if the player chooses to complete his path to the tunnel.
def complete_path_to_tunnel():
    """Things that will happen if the player chooses to
    complete his path to the tunnel.
    """
    # To modify the variable "total_score" inside the function.
    global total_score

    print_with_pause("You continue your journey towards the tunnel")
    print_with_pause(f"You find that the corridors of the {random_place} are \
empty because all the guards are looking for you in other places.")

    print_with_pause("And you continue walking cautiously towards the tunnel")
    print_with_pause("Fortunately, you find that there are no guards \
at the tunnel opening door")

    print_with_pause(f"Your score now is: {total_score}")
    print_with_pause("You enter the tunnel through a hidden hole in the \
wall and continue walking")

    print_with_pause(f"Finally, you exited from the other side of the tunnel, \
and now you are outside the {random_place}.\n\
You have been waiting for this moment", 5)

    print_with_pause("At the same time you exited the tunnel, the time \
portal appeared in front of you.\nYou returned to your era .... to your home.")

    print_with_pause(figlet_format("You Win"))

    print_with_pause(f"Your sore: {total_score}")


# The scenario if the player chooses to confront the guards.
def confront_tunnel_guards():
    """Things will happen when the player choose to confront the tunnel guards.
    """
    print_with_pause("You rushed towards the guards")
    print_with_pause("But they were more numerous and armed with \
shields and swords")

    print_with_pause("Abundance overcome courage")
    print_with_pause("The soldiers attacked you until they knocked \
you down and then arrested you and took you to implement the death sentence")

    # To modify the variable "total_score" inside the function.
    global total_score
    total_score = 0

    print_with_pause(f"Your score: {total_score}")
    print_with_pause("You lost")


# The scenario if the player chooses to deceive the guards.
def deceive_tunnel_guards():
    """Things will happen when the player choose to deceive the tunnel guards.
    """
    print_with_pause("You turned towards the tunnel guards anxiously")
    print_with_pause("You pretended to be in a hurry and told them:")
    print(f"that Commander \"Youssef\" sent you outside the {random_place} \
through the tunnel to look for the escaped prisoner in the forest.")

    print_with_pause("You knew the name of that leader when \
you were in prison")

    print_with_pause("One of the guards: Your order, sir. \
And they left you to enter the tunnel")

    # To modify the variable "total_score" inside the function.
    global total_score
    total_score += 5

    print_with_pause("Excellent work! you got 5 points")
    print(f"Your score: {total_score}")

    print_with_pause("You started walking into the tunnel but discovered \
that you took the wrong path")

    print_with_pause("No problem, you collected ten or more points")
    print_with_pause("Now you can use your magic wand \
hidden inside your shoes")


# Starting the game with a random score.
total_score = random.choice([5, 3, 6, 4])


#The loop will work until the player wins, ends the game or the score becomes 0
while True:
    # Start the game
    start_game()

    # Taking the choice from the user.
    choice1 = input("\nWhat do you want to do ?\nPlease enter 1 or 2 : ")

    # The loop will work until the player enters 1 or 2.
    while choice1 not in ["1", "2"]:
        choice1 = input("Invalid choice, please type 1 or 2 : ")

    if choice1 == "1":
        # Run the function that makes the player stab the soldier holding him.
        when_stab_soldier()

    else:
        # Run the function that makes the player run away from the soldiers.
        when_run_away()

    # The player wins when he collect 10 points.
    if total_score >= 10:
        print_with_pause(f"You get out the magical wand from your \
shoes and use it to get out of the {random_place}.")

        print_with_pause(f"Your sore now is {total_score}")

        print_with_pause(f"You cast a spell to get out of the{random_place}")
        print_with_pause("Finally, you found yourself in front of the \
tunnel exit")

        print_with_pause("At the same time you exited the tunnel, the time \
portal appeared in front of you.\nYou returned to your era .... to \
your home.",7)
        print_with_pause(figlet_format("You Win"))
        print_with_pause(f"Your sore: {total_score}")


    # Check if the total score is zero or not to end the game.
    if total_score == 0:
        print_with_pause("Your score becomes zero")
        print(figlet_format("Game Over"))

    # Check if the player wants to play again or not.
    play_again = input("\nWould you like to play again? (y/n) : ").lower()

    # The loop will work until the player enters yes or no (y/n)
    while play_again not in ["yes", "no", "y", "n"]:
        play_again = input("\nInvalid input, Please type Yes or No (y/n) \
: ").lower()
    # If yes the score will update else, the game will end.
    if play_again == "yes" or play_again == "y":
        total_score = random.choice([5, 3, 6, 4])

    else:
        print("\nThank you for trying game, We hope you enjoyed it\n")
        break