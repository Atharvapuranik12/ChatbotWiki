import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')

# ----- OpenWeatherMap API Initialization (Kapilesh Pennichetty) -----
from pyowm import OWM
owm = OWM('YOUR_OWM_API_KEY')

# ----- ipstack Geolocation API Initialization (Kapilesh Pennichetty) -----
import urllib.request
from ipstack import GeoLookup
geo_lookup = GeoLookup("YOUR_IPSTACK_API_KEY")

# ----- Regular Modules -----
import sys
import time

# ---------- Function and List Definitions ----------

# ----- Figuring out how users might respond (Sanjay Balasubramanian) -----
answer_A = ["A", "a", "A.", "a."]
answer_B = ["B", "b", "B.", "b."]
answer_C = ["C", "c", "C.", "c."]
yes = ["Y", "y", "Yes", "yes", "YES"]
no = ["N", "n", "No", "no", "NO"]


# ----- Return Name (Kapilesh Pennichetty) -----
def returnname():
    print("What's your name? (Enter your name only)")
    global name
    name = input(">>> ")
    if name == "exit":
        print("Goodbye!")
        sys.exit()
    elif name == "help":
        instructions()
    elif name == "return":
        mainmenu()
    else:
        print("Wow! Cool name,", name, "!")


# ----- Instructions (Kapilesh Pennichetty) -----
def instructions():
    """Prints instructions on how to operate the chatbot."""
    print(
        "I am a robot with a wide feature set!\nFirst off, I returned your name at the beginning of the program!\nFurthermore, I can:"
    )
    print(
        "- Find Information about something you want to learn "
    )

    print("- Play an Interactive Story")



# ---------- Main Menu (Kapilesh Pennichetty) ----------
def main_menu_validate(x):
    """Input validation for mainmenu() function"""
    if x == "1":
        wikichat()
    elif x == "2":
        weatherchat()
    elif x == "3":
        intro()
    elif x == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif x == "help":
        instructions()
        time.sleep(1)
        mainmenu()
    elif x == "return":
        mainmenu()
    else:
        return False


def mainmenu():  # Main Function
    """Asks the user what they want to do and redirects accordingly"""
    print(
        "\nWhat do you want to do? Type the number that corresponds to the action."
    )
    time.sleep(1)
    print(
        "\n\n[1] Find Information about something you want to learn"
    )
    print("[2] Play an Interactive story mode")
    x = input(">>> ")
    main_menu_result = main_menu_validate(x)
    if main_menu_result == False:
        while main_menu_result == False:
            print("Please enter a valid input:")
            x = input(">>> ")
            main_menu_result = main_menu_validate(x)


# -- Return to Main Menu (Kapilesh Pennichetty) --
def wiki_return_validate(x):
    """Validates input for wiki_return() function."""
    if x in yes:
        mainmenu()
    elif x in no:
        wikichat()
    else:
        return False


def wiki_return():
    """Returns to the mainmenu() function from the wikichat() function"""
    print("Do you want to return to the main menu?")
    x = input(">>> ")
    if x == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif x == "help":
        instructions()
    elif x == "return":
        mainmenu()
    else:
        wiki_validation_result = wiki_return_validate(x)
        if wiki_validation_result == False:
            while wiki_validation_result == False:
                print("Please enter a valid input (yes or no):")
                x = input(">>> ")
                wiki_validation_result = wiki_return_validate(x)








def story_return_validate(x):
    """Validates the input for the story_return() function"""
    if x in yes:
        mainmenu()
    elif x in no:
        intro()
    else:
        return False


def story_return():
    """Returns to the mainmenu() function from the intro() function"""
    print("Do you want to return to the main menu?")
    x = input(">>> ")
    if x == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif x == "help":
        instructions()
    elif x == "return":
        mainmenu()
    else:
        story_validation_result = story_return_validate(x)
        if story_validation_result == False:
            while story_validation_result == False:
                print("PLease enter a valid input (yes or no)")
                x = input(">>> ")
                story_validation_result = story_return_validate(x)


# ----- Retrieve Summary of Wikipedia Article (Kapilesh Pennichetty) -----
def wiki_article_validate(articlename):
    """Validates the input for the wikichat() function"""
    page_py = wiki_wiki.page(articlename)
    if page_py.exists() == True:
        print("Here you go,", name, ":")
        print(
            "Page - Title: %s" % page_py.title
        )  # This line was done with assistance from Sanjay Balasubramanian
        print(
            "Page - Summary: %s" % page_py.summary
        )  # This line was done with assistance from Sanjay Balasubramanian
    else:
        return False
    return page_py


def wikichat():  # Main Function
    """Prompts the user to enter the name of a Wikipedia article to retrieve the summary of said article."""
    print("What do you want to learn about?")
    x = input(">>> ")
    if x == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif x == "help":
        instructions()
    elif x == "return":
        mainmenu()
    else:
        wiki_validation_result = wiki_article_validate(x)
        if wiki_validation_result == False:
            while wiki_validation_result == False:
                print("Please enter a valid input:")
                x = input(">>> ")
                wiki_validation_result = wiki_article_validate(x)
        wiki_return()


# ---------- Retrieve Local Weather (Kapilesh Pennichetty with assistance from Sanjay Balasubramanian) ----------




# ----- Definitions for Interactive Story (Sanjay Balasubramanian and Kapilesh Pennichetty) -----

# -- Grabbing Objects --
flower = 0

# -- Cutting down on Duplication --
required = ("\nUse only A, B, or C\n")

# ----- Story Functions -----
"The story is broken into sections, starting with the intro."


def introvalidate():
    """Validates the input for the intro() function."""
    choice = input(">>> ")
    if choice == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif choice == "help":
        instructions()
    elif choice == "return":
        mainmenu()
    else:
        if choice in answer_A:
            boystory()
            return True
        elif choice in answer_B:
            girlstory()
            return True
        else:
            return False


def intro():
    """Prompts the user to choose whether the character is a boy or a girl."""
    print("Would you like to be a boy or a girl?")
    print("A. Boy\nB. Girl")
    isvalid = introvalidate()
    if isvalid == False:
        while isvalid == False:
            print("Please enter a valid input:")
            isvalid = introvalidate()
    story_return()


# ----- The Male Version for the Story -----
def boystory_validate(choice):
    """Validates the input for the boystory() function"""
    if choice == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif choice == "help":
        instructions()
    elif choice == "return":
        mainmenu()
    elif choice in answer_A:
        option_rockb()
    elif choice in answer_B:
        print("\nWelp, that was quick.", "\n\n", name, "died.")
        story_return()
    elif choice in answer_C:
        option_runb()
    else:
        print(required)
        return False


def boystory():
    """Introduction to the male interactive story."""
    print(
        name,
        "is on a vacation with his friends. He is alone right now because he wanted to take a midnight stroll. THUNK! Something hits him, on the head. His eyes close and he slumps down. Head spinning and fighting the pain on his head, he wakes up. He is in a big dark cave. There are bones all over the place. He tries to find the exit and he does. He sees a light shining from somewhere. He follows the light until he reaches this dark room. He hears a groan behind him. Slowly turning, he sees a big green ogre with a club. He is scared to death. What will",
        name, "do?")
    time.sleep(1)
    print(' A.', name, "will grab a nearby rock and throw it at the ogre\n",
          'B.', name, "will lie down and wait to be mauled\n", 'C.', name,
          "will run")
    choice = input(">>> ")
    boystory_validation_result = boystory_validate(choice)
    if boystory_validation_result == False:
        while boystory_validation_result == False:
            choice = input(">>> ")
            boystory_validation_result = boystory_validate(choice)


# -- Options for the Male Interactive Story --
def option_rockb_validate(choice):
    if choice == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif choice == "help":
        instructions()
    elif choice == "return":
        mainmenu()
    elif choice in answer_A:
        option_runb()
    elif choice in answer_B:
        print(
            "\n", name,
            "decided to throw another rock, as if the first rock thrown did much damage. The rock flew well over the ogre's head. He missed.\n\n",
            name, "died.")
        story_return()
    else:
        print("Use only A or B.")
        return False


def option_rockb():
    print(
        "\nThe ogre is stunned, but regains control. He begins running towards",
        name, "again. What will", name, "do?")
    time.sleep(1)
    print("A.", name, "will run\nB.", name, "will throw another rock")
    choice = input(">>> ")
    option_rockb_validation_result = option_rockb_validate(choice)
    if option_rockb_validation_result == False:
        while option_rockb_validation_result == False:
            choice = input(">>> ")
            option_rockb_validation_result = option_rockb_validate(choice)


def option_runb_validate(choice):
    if choice == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif choice == "help":
        instructions()
    elif choice == "return":
        mainmenu()
    elif choice in answer_A:
        print("He is easily spotted.\n\n", name, "died.")
        story_return()
    elif choice in answer_B:
        print("\nHe is no match for an ogre.\n\n", name, "died.")
        story_return()
    elif choice in answer_C:
        option_run2b()
    else:
        print(required)
        return False


def option_runb():
    print(
        "\n", name,
        "runs as quickly as possible, but the ogre's speed is too great. What will",
        name, "do?")
    time.sleep(1)
    print("A.", name, "will hide behind a boulder\nB.", name, "will fight\nC.",
          name, "will run")
    choice = input(">>> ")
    option_runb_validate_result = option_runb_validate(choice)
    if option_runb_validate_result == False:
        while option_runb_validate_result == False:
            choice = input(">>> ")
            option_runb_validate_result = option_runb_validate(choice)


def option_run2b_validate(choice):
    if choice == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif choice == "help":
        instructions()
    elif choice == "return":
        mainmenu()
    elif choice in answer_A:
        print(
            "\n", name,
            "takes the left trusting the arrow. He ends up in a dead end. He looks behind to run, but the ogre is there waiting for him. He realizes that the arrow is a trap. The ogre grabs his club and kills him.\n\n",
            name, "died.")
        story_return()
    elif choice in answer_B:
        option_rightb()
    else:
        print("Use only A or B")
        return False


def option_run2b():
    print(
        "\n", name,
        "runs as fast as he can. He ends up in a fork. He can either take a left or a right. He notices a battered sign with burnt edges. It is point towards the left. He can hear the ogre coming behind him and he has to make a decision fast. Does",
        name, "choose left or right?")
    time.sleep(1)
    print("A. Left\nB. Right")
    choice = input('>>> ')
    option_run2b_validation_result = option_run2b_validate(choice)
    if option_run2b_validation_result == False:
        while option_run2b_validation_result == False:
            choice = input(">>> ")
            option_run2b_validation_result = option_run2b_validate(choice)


def option_rightb_validate(choice):
    if choice == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif choice == "help":
        instructions()
    elif choice == "return":
        mainmenu()
    elif choice in answer_A:
        print(
            "\n", name,
            "jumps off the cliff into the mud. It is a soft landing. He tries to get out but he can't, and he slowly starts sinking into the mud. Realizing that it sinking mud, he screams until he sinks fully\n\n",
            name, "died.")
        story_return()
    elif choice in answer_B:
        option_townb()
    elif choice in answer_C:
        print(
            "\n", name,
            "takes the left into the Cave Entrance. No clue why he would go back into the cave, but he does. He comes back to the fork."
        )
        option_run2b()
    else:
        print(required)
        return False


def option_rightb():
    print(
        "\n", name,
        "instincts tell him that the arrow is a trap so he takes a right. He runs as fast as he can. He comes to a cliff. When he looks down from the cliff he sees a pool of mud. He looks to his right and there are steps leading toward a town. On his left is another entrance into the cave. What will",
        name, "do?")
    time.sleep(1)
    print("A.", name, "will jump off the cliff into the pool of mud\nB.", name,
          "runs towards the Town\nC.", name,
          "takes the entrance back into the cave")
    choice = input('>>> ')
    option_rightb_validation_result = option_rightb_validate(choice)
    if option_rightb_validation_result == False:
        while option_rightb_validation_result == False:
            choice = input(">>> ")
            option_rightb_validation_result = option_rightb_validate(choice)


def option_townb_validate(choice):
    if choice == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif choice == "help":
        instructions()
    elif choice == "return":
        mainmenu()
    if choice in yes:
        flower = 1
    elif choice not in yes:
        flower = 0
    print(
        "\n", name,
        "hears its heavy footsteps and readies himself for the impending ogre. What will",
        name, "do?")
    time.sleep(1)
    if flower > 0:
        print(
            "\nHe quickly held out the purple flower, somehow hoping it will stop the ogre. It does! The ogre was looking for love.",
            "\n\nThis got weird, but he survived!")
        story_return()
    elif choice in no:  # If the user didn't grab the flower
        print("\nMaybe he should have picked up the flower."
              "\n\n", name, "died.")
        story_return()
    else:
        print("Please enter a valid input:")
        return False


def option_townb():
    print(
        "\nWhile frantically running towards the town,", name,
        "notices a rusted sword lying in the mud. He reaches down to grab it, but misses. He tries to calm his heavy breathing as he hides behind a boulder, waiting for the ogre to come charging around the corner. He notices a purple flower near his foot. Will",
        name, "pick it up? Y/N")
    choice = input(">>> ")
    option_townb_validation_result = option_townb_validate(choice)
    if option_townb_validation_result == False:
        while option_townb_validation_result == False:
            choice = input(">>> ")
            option_townb_validation_result = option_townb_validate(choice)


# ----- The Female Version of the Story -----
def girlstory_validate(choice):
    """Validates the input for the girlstory() function."""
    if choice == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif choice == "help":
        instructions()
    elif choice == "return":
        mainmenu()
    elif choice in answer_A:
        option_rockg()
    elif choice in answer_B:
        print("\nWelp, that was quick.\n\n", name, "died.")
        story_return()
    elif choice in answer_C:
        option_rung()
    else:
        print(required)
        return False


def girlstory():
    """Introduction to the female interactive story."""
    print(
        name,
        "is on a vacation with her friends. She is alone right now because she wanted to take a midnight stroll. THUNK! Something hits her, on the head. Her eyes close and she slumps down. Head spinning and fighting the pain on her head, she wakes up. She is in a big dark cave. There are bones all over the place. She tries to find the exit and she does. She sees a light shining from somewhere. She follows the light until she reaches this dark room. She hears a groan behind her. Slowly turning, she sees a big green ogre with a club. She is scared to death. What will",
        name, "do?")
    time.sleep(1)
    print("A.", name, "will grab a nearby rock and throw it at the ogre\n"
          'B.', name, "will lie down and wait to be mauled\n"
          'C.', name, "will run")
    choice = input(">>> ")
    girlstory_validation_result = girlstory_validate(choice)
    if girlstory_validation_result == False:
        while girlstory_validation_result == False:
            choice = input(">>> ")
            girlstory_validation_result = girlstory_validate(choice)


# -- Options for the Female Interactive Story --
def option_rockg_validate(choice):
    if choice == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif choice == "help":
        instructions()
    elif choice == "return":
        mainmenu()
    elif choice in answer_A:
        option_rung()
    elif choice in answer_B:
        print(
            "\n", name,
            "decided to throw another rock, as if the first rock thrown did much damage. The rock flew over the ogre's head. She missed.\n\n",
            name, "died.")
        story_return()
    else:
        print("Use only A or B")
        return False


def option_rockg():
    print(
        "\nThe ogre is stunned, but regains control. He begins running towards",
        name, "again. What will", name, "do?")
    time.sleep(1)
    print("A.", name, "will run\nB.", name, "will throw another rock")
    choice = input(">>> ")
    option_rockg_validation_result = option_rockg_validate(choice)
    if option_rockg_validation_result == False:
        while option_rockg_validation_result == False:
            choice = input(">>> ")
            option_rockg_validation_result = option_rockg_validate(choice)


def option_rung_validate(choice):
    if choice == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif choice == "help":
        instructions()
    elif choice == "return":
        mainmenu()
    elif choice in answer_A:
        print("\nShe is easily spotted.\n\n", name, "died.")
        story_return()
    elif choice in answer_B:
        print("\nShe is no match for an ogre.\n\n", name, "died.")
        story_return()
    elif choice in answer_C:
        option_run2g()
    else:
        print(required)
        return False


def option_rung():
    print(
        "\n", name,
        "runs as quickly as possible, but the ogre's speed is too great. What will",
        name, "do?")
    time.sleep(1)
    print("A.", name, "will hide behind a boulder\nB.", name, "will fight\nC.",
          name, "will run")
    choice = input(">>> ")
    option_rung_validate_result = option_rung_validate(choice)
    if option_rung_validate_result == False:
        while option_rung_validate_result == False:
            choice = input(">>> ")
            option_rung_validate_result = option_rung_validate(choice)


def option_run2g_validate(choice):
    if choice == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif choice == "help":
        instructions()
    elif choice == "return":
        mainmenu()
    elif choice in answer_A:
        print(
            "\n", name,
            "takes the left trusting in the arrow. She ends up in a dead end. She looks  behind to run, but the ogre is there waiting for her. She realizes that the  arrow is a trap. The ogre grabs his club and kills her.\n\n",
            name, "died.")
        story_return()
    elif choice in answer_B:
        option_rightg()
    else:
        print("Use only A or B")
        return False


def option_run2g():
    print(
        "\n", name,
        "runs as fast as she can. She ends up in a fork. She can either take a left or a right. She notices a battered sign with burnt edges. It is point towards the left. She can hear the ogre coming behind her and she has to make a decision fast. Does she choose left or right?"
    )
    time.sleep(1)
    print("A. Left\nB. Right")
    choice = input('>>> ')
    option_run2g_validation_result = option_run2g_validate(choice)
    if option_run2g_validation_result == False:
        while option_run2g_validation_result == False:
            choice = input(">>> ")
            option_run2g_validation_result = option_run2g_validate(choice)


def option_rightg_validate(choice):
    if choice == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif choice == "help":
        instructions()
    elif choice == "return":
        mainmenu()
    elif choice in answer_A:
        print(
            "\n", name,
            "jumps off the cliff into the mud. It is a soft landing. She tries to get out but she can't, and she slowly starts sinking into the mud. Realizing that it sinking mud she screams until she sinks fully\n\n",
            name, "died.")
        story_return()
    elif choice in answer_B:
        option_towng()
    elif choice in answer_C:
        print(
            "\n", name,
            "takes the left into the cave entrance. No clue why she would go back into the cave, but she does. She comes back to the fork."
        )
        option_run2g()
    else:
        print(required)
        return False


def option_rightg():
    print(
        "\n", name,
        "instincts tell her that the arrow is a trap so she takes a right. She runs as fast as she can. She comes to a cliff. When she looks down from the cliff she sees a pool of mud. She looks to her right and there are steps leading toward a town. On her left is another entrance into the cave. What will",
        name, "do?")
    time.sleep(1)
    print("A.", name, "will jump off the cliff into the pool of mud\nB.", name,
          "will run towards the Town\nC.", name,
          "will take the entrance back into the cave")
    choice = input('>>> ')
    option_rightg_validation_result = option_rightg_validate(choice)
    if option_rightg_validation_result == False:
        while option_rightg_validation_result == False:
            choice = input(">>> ")
            option_rightg_validation_result = option_rightg_validate(choice)


def option_towng_validate(choice):
    if choice == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif choice == "help":
        instructions()
    elif choice == "return":
        mainmenu()
    if choice in yes:
        flower = 1
    elif choice not in yes:
        flower = 0
    print(
        "\n", name,
        "hears its heavy footsteps and readies herself for the impending ogre."
    )
    time.sleep(1)
    if flower > 0:
        print(
            "\nShe quickly held out the purple flower, somehow hoping it will stop the ogre. It does! The ogre was looking for love.\n\nThis got weird, but she survived!"
        )
        story_return()
    elif choice in no:  # If the user didn't grab the flower
        print("\nMaybe she should have picked up the flower.\n\n", name,
              "died.")
        story_return()
    else:
        print("Please enter a valid input:")
        return False


def option_towng():
    print(
        "\nWhile frantically running towards the town,", name,
        "notices a rusted sword lying in the mud. She reaches down to grab it, but misses. She tries to calm her heavy breathing as she hides behind a boulder, waiting for the ogre to come charging around the corner. She notices a purple flower near her foot. Will",
        name, "pick it up? Y/N")
    choice = input(">>> ")
    option_towng_validation_result = option_towng_validate(choice)
    if option_towng_validation_result == False:
        while option_towng_validation_result == False:
            choice = input(">>> ")
            option_towng_validation_result = option_towng_validate(choice)


# ---------- Main Code ----------

print(
    "Hello, my name is AP Chatbot!\nI was created by Atharva Puranik.")
time.sleep(1)
returnname()
instructions()
print("Now, let's get started!")
mainmenu()


import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
