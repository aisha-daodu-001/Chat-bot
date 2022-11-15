# Write your code here
from random import *
# import ANSI color formatting for output in terminal
from termcolor import colored, cprint
# Import ASCII Art Library For Python
from art import *

#print ASCII text (bubblehead font)
user_name= input("Please enter your name: ")
tprint(f"    {user_name}     ", font="bubblehead")
tprint("        Welcome    ", font="bubbleheead")
tprint("To the Code_Genin", font= "bubblehead")
tprint("        Chatbot      ", font="bubblehead")

#List of available options
available_options= ["Tell me about the team", "Ask me a programming riddle", "Tell me a programming joke", "Exit"]

#List of all team members
team_members= ["AbdulAfeez A", "Aisha D", "Mercy", "Shakira D"]
team_members_info = ["bio", "superpower", "home country", "hobbies"]

#List of team members info
members_bio=["Born more than 2 decades ago, AbdulAfeez is the second child of a family of 5 children. He is currentry a semi-finalist student of the Mechatronics department of the Federal University of Agriculture and a computer science student at kibo school of technology. He's an artificial intelligence enthusiast and loves robot as well.", 
              "Aisha is a junior UI designer and developer.  She is a student at Kibo school studying Computer Science and also a community manager at Try Kibo. She's currently a design intern at Center for Journalism and Innovation development.",
              "Mercy is an environmental engineer who's passionate about data. She currently study computer science at kibo school of technology. Shes loves playing with her dogs during her free time and dancing salsa!",
              "Daodu Sakira is a poet and a junior UI designer. She's a student of Kibo school of technology. She also study Mechatronics Engineering at a tertiary institution in Nigeria."]
members_superpower = ["I am Limitless", "Multitasking", " I achieve whatever it is I set my mind to","Singing"]
members_homecountry= ["Nigeria", "Nigeria", "Kenya", "Nigeria"]
members_hobbies= ["Playing football, travelling, listening to music and reading books",
                  "Travelling and reading",
                  "Reading novels and watching movies",
                  "Singing, Teaching, Writing poems, Designing."]
#list of riddle questions
riddle_questions=["The more you code, the more of me there is. I may be gone for now but you can’t get rid of me forever. What am I?",
                   "I’m a language for everything yet I have no real identity of my own. Good luck trying to compile me. What am I?",
                   "As a developer I’m your eyes, showing you the result of your code in your language of choice. What am I?",
                   "I’m fundamental and used to build larger structures. While you’ll find many different kinds of me, we all just mess with information in different ways. What am I?",
                   "As a developer, you usually get mad at me because I complain a lot, although I’m usually right. What am I?",
                   "I’m a simple thing, nothing special. While I have many cousins we’re all very similar because we set your project up. What am I?",
                   "I’m pretty focused so I don’t do too much. However whatever you wish is my command. What am I?",
                   "I’m your “waiter” for information. What I am?",
                   "I come small, as small as you can get in fact. With many well-thought-out versions of me I bring stability. What am I?",
                   ]

#list of answers to the riddles
riddle_answers= ["Bug", "Pseudocode", "Print statement", "data structure", "compiler", "configuration file",
                 "command", "server", "unit test"]

#list of programming jokes
programming_jokes = ["Question: What's the object oriented way to become wealthy?  Ans: Inheritance",
                     "Question: What do you call a programmer from Finland?  Ans: Nerdic",
                     "Question: What is a programmer's favourite hangout place?  Ans: Foobar",
                     "Question: Why did the programmer quit his job?  Ans: Because he didn't get arrays(a raise).",
                     "Question: What do computers and air conditioners have in common?  Ans: They both become useless when you open windows.",
                     "Question: Why do java programmers have to wear glasses?   Ans: Because they don't C#(see sharp)",
                     "Real Programmer's count from 0",
                     "The programmer got stuck in the bathroom because the instruction on the shampoo bottle said....  Lather, Rinse, Repeat",
                     "I'd like to make the world a better place but they won't give me the source code",
                     "Question: What’s a better name for Frontend Developers?  Ans: <div>elopers",
                     "Question: Which Hogwarts house is able to communicate securely?  Ans: SSLytheryn",
                     "Question: You know how a hacker escapes the FBI?  Ans: \FBI",
                     "Question: Why aren't frontend developers humble?  Ans: They display: flex;",
                     "Question: What’s the easiest way to find a public bathroom?  Ans: Look up the IP address"]

#Infinite loop
while True:
    input("Press [enter] to  continue. ")
    #Loop through the available available_options
    for option in range(len(available_options)):
        print(f"{option + 1}. {available_options[option]}")
    
    

    #prompt user for their choices 
    user_choice = input("choose a number: ")
    try:
        user_choice = int(user_choice)
    except:
        print("Invalid type of choice")
        continue
    #if user's choice is 1[about the team]
    if user_choice == 1:
        #print an output with a red color on white background
        cprint("Code_Genin's mission is to build world class programmers through collaboration", "red", "on_white", attrs=["bold"])
        print("Learn more about the team members")

        
        #loop through the team members
        for members in range(len(team_members)):
            print(f"{members + 1}. {team_members[members]}")
        #prompt the user to select a member
        while True:
            try:
                select_member= int(input("Select a team member: "))
            except:
                print("Invalid type of choice")
                continue
            #if member is part of the team members
            if select_member <= len(team_members):
                for info in range(len(team_members_info)):
                    print(f"{info + 1}. {team_members_info[info]}")
                while True:
                    try:
                        select_info = int(input(f"Please enter a number to know more about {team_members[select_member-1]}: "))
                    except:
                        print("Invalid type of choice")
                        continue
                    if select_info == 1:
                        cprint(members_bio[select_member - 1], "blue", "on_white", attrs=["bold"])
                        break
                    elif select_info == 2:
                        cprint(members_superpower[select_member-1], "red", "on_white", attrs=["bold"] )
                        break
                    elif select_info == 3:
                        cprint(members_homecountry[select_member-1], "green", "on_white", attrs=["bold"])
                        break
                    elif select_info == 4:
                        cprint(members_hobbies[select_member -1], "yellow", "on_white", attrs=["bold"])
                        break
                    else:
                        print("Invalid input. Ensure the number entered is part of the options available")
                break
        # if memeber is not part of the team members
            else:
                print("Invalid input. Ensure the number entered is part of the list of members")
            
        
    
    #if user's choice is 2[Ask me a programming riddle]
    #user are allowed to answer the riddle 3 times
    elif user_choice == 2:
        count = 1
        # select a random question from the riddle list 
        question = choice(riddle_questions)
        print(question)
        # assign the answer to the riddle from the riddle_answers list
        answer = riddle_answers[riddle_questions.index(question)].lower()
        while count <= 3:
            # prompt the users for their answers
            user_answer = input("Enter your answer: ").lower()
            #if the answer provided by the user is the same as the riddle answer
            if user_answer == answer:
                print("Good Job!")
                break
            #if the answer provided by the user is not the same as the riddle answe
            else:
                if count < 3:
                    print("wrong answer")
                else:
                    print(f"The correct answer is {answer}")
                    print("Game Over!")
            count += 1
    
    #if user's choice is 3[Tell me a joke.]
    elif user_choice == 3:
        #print out a random joke from the list of programming jokes
        print(choice(programming_jokes))
    
    # if user's choice is 4[exit], break out of the loop   
    elif user_choice == 4:
        exit = True
        while exit:
            end_program = input("Are you sure you want to exit? Enter(y/n): ").lower()
            if end_program == "y":
                print(f"{user_name} thank you for using code_genin's bot")
                exit = False
            elif end_program == "n":
                break
            else:
                print("You can only enter 'y' or 'n'.")
                continue
        if exit == False:
            break
        else:
            continue
    
    #if the number entered is not in the option list
    else:
        print(f"Invalid option. Please enter a number between 1 - {len(available_options)}")
