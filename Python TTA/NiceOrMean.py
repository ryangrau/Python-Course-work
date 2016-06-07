nice = 0
mean = 0

def main():
    start()

def start():
    print "Hello and Welcome to nice or mean!"
    name = raw_input ("What's you name? : ")
    print "Hi and Welcome, "+name+"!"
    print "In this game, you will be greeted by several different people.  You can treat them however you'd like, nice or mean!"
    print "By the end of the game your fate will be determined by how you act."

    choice = raw_input("Do you want to play? y/n ")

    if choice == "y":
        print "Greet, use 'm' for mean and 'n' for nice!"
        begin()

    if choice == "n":
        print "Ok Bye!"

def begin():
    global nice
    global mean

    if nice > 2:
        print "Nice job! - you Win! Everyone loves you and you live in a palace!"
        choice = raw_input("Do you want to play again? y/n ")

        if choice == "y":
            print "Okay lets go!"
            nice = 0
            begin()

        if choice == "n":
            print "Nice playing with you, byeeeeee!"
            exit()

    if mean > 2:
        print "Too bad - game over you big meanie! You live in a van down by the river...with no friends!"
        
        choice = raw_input("Do you want to play again? y/n ")

        if choice == "y":
             print "Okay lets go!"
             mean = 0
             begin()


        if choice == "n":
             print "Off ya go then mate!"
             exit()

        elif choice != "y"+"n":
             print "please enter y or n"

             if choice == "y":
                 begin()
             if choice == "n":
                 print "check ya later homie"
                 exit()

             if choice != "y"+"n":
                 choice = raw_input("do you really want to play the game? y/n ")


    pick = raw_input("Someone approaches you to talk.  Will you be nice or mean? n/m ")

    if pick == "n":
        print "They smile, wave and walk away."
        nice = nice+1
        print "You currently have " +str(nice) + " nice."
        begin()

    if pick == "m":
        print "They frown, flip you off and walk away."
        mean = mean+1
        print "You currently have " +str(mean) + " mean."
        begin()


        
                 
                 
















start()
