# Dec 19th 2023

import random

class MyUNO:
    def __init__(self):
        
        self.uno_full_deck = []
        self.uno_add_later_deck = []
        randomizer = 0
        self.your_hand = []
        self.enemy_hand = []
        self.enemy_hand_count = 0
        self.your_hand_count = 0
        self.card = ""
        self.top_card = ""
        self.top_card_num = ""
        self.top_card_color = ""
        self.random_card_chosen = ""
        self.user_card_choice = ""
        self.user_card_color = ""
        self.user_card_num = ""
        self.user_card_action = ""
        self.bot_card_action = ""
        self.bot_card_choice = ""
        self.bot_card_num = ""
        self.bot_card_color = ""
        self.bot_new_added_card = ""
        self.new_added_card = ""
        self.bot_has_no_playable_cards = 0
        self.counter = 0
        self.uno_call = ""
        self.random_bot_block_choice = 0
        self.random_user_block_choice = 0
        self.your_successful_uno_count = 0
        self.enemy_successful_uno_count = 0
        self.win_or_lost_count = 0
        self.repeat = True
        self.wild_card_color_changer = ""
        
        infile = open("uno_cards_for_deck.txt","r")

        self.uno_full_deck = infile.readlines()

        infile.close()

        for i in range(len(self.uno_full_deck)):
            self.uno_full_deck[i] = self.uno_full_deck[i].rstrip("\n")

        self.dealing_hands()

        self.shuffling_deck()

        self.top_card_chooser()

        while self.repeat == True:
            self.user_chosen_card()
            self.winner_checker()

            while self.user_card_action == "reverse" or self.user_card_action == "skip":
                self.user_chosen_card()
                self.winner_checker()

            self.counter = 0
            self.bot_choice()
            self.bot_draws_card()
            while self.bot_card_action == "reverse" or self.bot_card_action == "skip":
                self.counter = 0
                self.bot_choice()
                self.bot_draws_card()
                self.winner_checker()

            self.winner_checker()

    def bot_draws_card(self):
        if self.counter == 0:
            self.bot_has_no_playable_cards = 1
            self.pass_choice()
            self.bot_choice()

    def winner_checker(self):
        if self.enemy_hand_count == 0: 
            self.repeat = False
            print("\nYOU HAVE LOST!!!!!")
            self.win_or_lost_count = 1
        elif self.your_hand_count == 0 and self.win_or_lost_count == 0:
            self.repeat = False
            print("\nCONGRATULATIONS, YOU HAVE WON!")
            self.win_or_lost_count = 1


    def dealing_hands(self):
        
        while self.your_hand_count < 7:
            randomizer = random.randint(0,len(self.uno_full_deck) - 1)
            self.card = self.uno_full_deck[randomizer]
            self.your_hand.append(self.card)
            self.uno_add_later_deck.append(self.card)
            self.uno_full_deck.remove(self.card)
            self.your_hand_count += 1

        while self.enemy_hand_count < 7:
            randomizer = random.randint(0,len(self.uno_full_deck) - 1)
            self.card = self.uno_full_deck[randomizer]
            self.enemy_hand.append(self.card)
            self.uno_add_later_deck.append(self.card)
            self.uno_full_deck.remove(self.card)
            self.enemy_hand_count += 1

    def shuffling_deck(self):          

        shuffler_count = 0
        card_chosen_for_swapping1 = 0
        card_chosen_for_swapping2 = 0
        while shuffler_count != 93:
            card_chosen_for_swapping1 = random.randint(0,len(self.uno_full_deck) - 1)
            card_chosen_for_swapping2 = random.randint(0,len(self.uno_full_deck) - 1)
            self.uno_full_deck[card_chosen_for_swapping1] , self.uno_full_deck[card_chosen_for_swapping2] = self.uno_full_deck[card_chosen_for_swapping2] , \
                self.uno_full_deck[card_chosen_for_swapping1]
            shuffler_count += 1

    def top_card_chooser(self):

        top_card_num_chooser = 0
        self.top_card = self.uno_full_deck[top_card_num_chooser]
        
        while ("plus" in self.top_card) or ("reverse" in self.top_card) or ("wild" in self.top_card) or ("skip" in self.top_card):
            top_card_num_chooser += 1
            self.top_card = self.uno_full_deck[top_card_num_chooser]
            
        print("The first card is:",self.top_card)
        print()

        if "red" in self.top_card:
            self.top_card_color = "red"
        elif "blue" in self.top_card:
            self.top_card_color = "blue"
        elif "yellow" in self.top_card:
            self.top_card_color = "yellow"
        elif "green" in self.top_card:
            self.top_card_color = "green"

        if "zero" in self.top_card:
            self.top_card_num = "zero"
        elif "one" in self.top_card:
            self.top_card_num = "one"
        elif "two" in self.top_card:
            self.top_card_num = "two"
        elif "three" in self.top_card:
            self.top_card_num = "three"
        elif "four" in self.top_card:
            self.top_card_num = "four"
        elif "five" in self.top_card:
            self.top_card_num = "five"
        elif "six" in self.top_card:
            self.top_card_num = "six"
        elif "seven" in self.top_card:
            self.top_card_num = "seven"
        elif "eight" in self.top_card:
            self.top_card_num = "eight"
        elif "nine" in self.top_card:
            self.top_card_num = "nine"

        print(self.enemy_hand)

    def user_chosen_card(self):

        self.user_card_action = ""

        if self.your_hand_count == 1 and self.your_successful_uno_count != 1:
            print("You forgot to call UNO!")
            for new_cards in range(2):
                new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                self.uno_full_deck.remove(self.new_added_card)
                self.uno_add_later_deck.append(self.new_added_card)
                self.your_hand.append(self.new_added_card)
                self.your_hand_count += 1
        
        print("YOUR HAND:")
        print(self.your_hand)
        self.user_card_choice = input("\nEnter the card you want to play: ")
        if self.user_card_choice == "pass" or self.user_card_choice == "Pass":
            self.pass_choice()
            self.user_card_choice = input("Enter the card you want to play (if none, enter 'end' : ")
            
        if self.user_card_choice != "end":

            if "red" in self.user_card_choice:
                self.user_card_color = "red"
            elif "blue" in self.user_card_choice:
                self.user_card_color = "blue"
            elif "yellow" in self.user_card_choice:
                self.user_card_color = "yellow"
            elif "green" in self.user_card_choice:
                self.user_card_color = "green"


            if "zero" in self.user_card_choice:
                self.user_card_num = "zero"
            if "one" in self.user_card_choice:
                self.user_card_num = "one"
            if "two" in self.user_card_choice:
                self.user_card_num = "two"
            if "three" in self.user_card_choice:
                self.user_card_num = "three"
            if "four" in self.user_card_choice:
                self.user_card_num = "four"
            if "five" in self.user_card_choice:
                self.user_card_num = "five"
            if "six" in self.user_card_choice:
                self.user_card_num = "six"
            if "seven" in self.user_card_choice:
                self.user_card_num = "seven"
            if "eight" in self.user_card_choice:
                self.user_card_num = "eight"
            if "nine" in self.user_card_choice:
                self.user_card_num = "nine"

            if "plus_2" in self.user_card_choice:
                self.user_card_action = "plus_2"
            elif "reverse" in self.user_card_choice:
                self.user_card_action = "reverse"
            elif "skip" in self.user_card_choice:
                self.user_card_action = "skip"
            elif "wild_plus_four" in self.user_card_choice:
                self.user_card_action = "wild_plus_four"
            elif "wild" in self.user_card_choice:
                self.user_card_action = "wild"

            
            if (self.user_card_color == self.top_card_color and self.user_card_action == "skip") or (self.top_card_num == "skip" and self.user_card_action == "skip"):
                print("You have skipped your opponents turn!\n")
                print("The new top card is:",self.user_card_choice,"\n")

            elif (self.user_card_color == self.top_card_color and self.user_card_action == "reverse") or (self.top_card_num == "reverse" and self.user_card_action == "reverse"):
                print("You have reversed the order of cards back to you!\n")
                print("The new top card is:",self.user_card_choice,"\n")

            if (self.user_card_color == self.top_card_color and self.user_card_action == "plus_2") or (self.top_card_num == "plus_2" and self.user_card_action == "plus_2"):
                print("\nYour opponent has gained 2 cards!")

                for i in range(2):
                    new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                    self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                    self.uno_full_deck.remove(self.new_added_card)
                    self.uno_add_later_deck.append(self.new_added_card)
                    self.enemy_hand.append(self.new_added_card)
                    self.enemy_hand_count += 1
                    self.enemy_successful_uno_count = 0

            elif self.user_card_action == "wild_plus_four":
                
                self.wild_card_color_changer = input("\nYou may now change the color, what is your new chosen color: ")
                
                if "red" in self.wild_card_color_changer:
                    self.user_card_color = "red"
                elif "blue" in self.wild_card_color_changer:
                    self.user_card_color = "blue"
                elif "yellow" in self.wild_card_color_changer:
                    self.user_card_color = "yellow"
                elif "green" in self.wild_card_color_changer:
                    self.user_card_color = "green"
                print("New top color is now:",self.user_card_color)

                print("\nThe opponent has gained 4 cards!")

                for i in range(4):
                    new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                    self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                    self.uno_full_deck.remove(self.new_added_card)
                    self.uno_add_later_deck.append(self.new_added_card)
                    self.enemy_hand.append(self.new_added_card)
                    self.enemy_hand_count += 1
                self.enemy_successful_uno_count = 0

            elif self.user_card_action == "wild":
                self.wild_card_color_changer = input("\nYou may now change the color, what is your new chosen color: ")
                if "red" in self.wild_card_color_changer:
                    self.user_card_color = "red"
                elif "blue" in self.wild_card_color_changer:
                    self.user_card_color = "blue"
                elif "yellow" in self.wild_card_color_changer:
                    self.user_card_color = "yellow"
                elif "green" in self.wild_card_color_changer:
                    self.user_card_color = "green"
                print("New top card color is now:",self.user_card_color)
            
            self.displaying_top_card_and_other_user_options()

    def displaying_top_card_and_other_user_options(self):
                
        if (self.user_card_color == self.top_card_color) or (self.user_card_num == self.top_card_num) or ("wild" in self.user_card_choice) or (self.user_card_action == self.top_card_num):
            if self.user_card_choice in self.your_hand:
                self.winner_checker()

                if self.user_card_action == "":
                    self.top_card_num = self.user_card_num
                else:
                    if self.user_card_action == "reverse":
                        self.top_card_num = "reverse"
                    elif self.user_card_action == "skip":
                        self.top_card_num = "skip"
                    elif self.user_card_action == "plus_2":
                        self.top_card_num = "plus_2"
                    elif self.user_card_action == "wild" or "wild_plus_four":
                        self.top_card_num = "wild"
                
                self.top_card = self.user_card_choice
                self.top_card_color = self.user_card_color
                    
                self.uno_add_later_deck.append(self.user_card_choice)
                self.your_hand.remove(self.user_card_choice)
                
                print("\nthe top card is now:",self.user_card_choice)
                self.your_hand_count -= 1
                print()

                self.uno_call = input("Would you like to call uno? or block?: ")
                if self.uno_call == "uno" and self.your_hand_count == 1:
                    self.your_uno_has_been_said()
                elif self.uno_call == "block" and self.enemy_hand_count == 1:
                    self.block_on_bot_has_been_said()
            else:
                print("NO CARD IN HAND ERROR")
                print(self.user_card_color,self.top_card_color,self.user_card_num,self.top_card_num,self.user_card_choice)
        else:
            print("ERROR, CARD DOES NOT MATCH CONDITIONS TO BE PLAYED")
        print("top card color:",self.top_card_color,"      top num:",self.top_card_num,"    self.top_card:",self.top_card)
        

    def pass_choice(self):
        if self.user_card_choice == "pass" or self.user_card_choice == "Pass":
            new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
            self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
            self.uno_full_deck.remove(self.new_added_card)
            self.uno_add_later_deck.append(self.new_added_card)
            self.your_hand.append(self.new_added_card)
            self.your_hand_count += 1
            self.your_successful_uno_count = 0
            print()
            print("YOUR NEW HAND:")
            print(self.your_hand)

        if self.bot_has_no_playable_cards == 1:
            print("Your opponent has decided to draw a new card!\n")
            bot_new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
            self.bot_new_added_card = self.uno_full_deck[bot_new_card_added_to_hand]
            self.uno_full_deck.remove(self.bot_new_added_card)
            self.uno_add_later_deck.append(self.bot_new_added_card)
            self.enemy_hand.append(self.bot_new_added_card)
            self.enemy_hand_count += 1
            self.bot_has_no_playable_cards = 0
            self.enemy_successful_uno_count = 0
            
    def bot_choice(self):

        print("This is enemy_hand before card in middle",self.enemy_hand)
        print()

        if self.enemy_hand_count == 1 and self.enemy_successful_uno_count == 0:
            self.bot_has_called_uno()

        if self.enemy_hand_count == 1 and self.enemy_successful_uno_count == 0:
            print("The opponent has forgotten to say UNO!")
            print("They must now draw 2 new cards")
            for new_cards in range(2):
                new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                self.uno_full_deck.remove(self.new_added_card)
                self.uno_add_later_deck.append(self.new_added_card)
                self.enemy_hand.append(self.new_added_card)
                self.enemy_hand_count += 1
                self.enemy_successful_uno_count = 0

        self.bot_card_action = ""    
        element = 0
        for element in self.enemy_hand:
            if self.counter == 0:
                if "zero" in element:
                    self.bot_card_num = "zero"
                if "one" in element:
                    self.bot_card_num = "one"
                if "two" in element:
                    self.bot_card_num = "two"
                if "three" in element:
                    self.bot_card_num = "three"
                if "four" in element:
                    self.bot_card_num = "four"
                if "five" in element:
                    self.bot_card_num = "five"
                if "six" in element:
                    self.bot_card_num = "six"
                if "seven" in element:
                    self.bot_card_num = "seven"
                if "eight" in element:
                    self.bot_card_num = "eight"
                if "nine" in element:
                    self.bot_card_num = "nine"

                if "red" in element:
                    self.bot_card_color = "red"
                if "blue" in element:
                    self.bot_card_color = "blue"
                if "green" in element:
                    self.bot_card_color = "green"
                if "yellow" in element:
                    self.bot_card_color = "yellow"

                self.bot_card_action = ""
                if "plus_2" in element:
                    self.bot_card_action = "plus_2"
                elif "reverse" in element:
                    self.bot_card_action = "reverse"
                elif "skip" in element:
                    self.bot_card_action = "skip"
                elif "wild_plus_four" in element:
                    self.bot_card_action = "wild_plus_four"
                elif "wild" in element:
                    self.bot_card_action = "wild"
                

                if (self.top_card_color == self.bot_card_color and self.bot_card_action == "plus_2") or (self.top_card_num == self.bot_card_action):
                    print("\nYou have have gained 2 cards!")

                    for i in range(2):
                        new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                        self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                        self.uno_full_deck.remove(self.new_added_card)
                        self.uno_add_later_deck.append(self.new_added_card)
                        self.your_hand.append(self.new_added_card)
                        self.your_hand_count += 1
                        
                    self.your_successful_uno_count = 0

                elif (self.top_card_color == self.bot_card_color and self.bot_card_action == "skip") or (self.top_card_num == self.bot_card_action):
                    print("Your turn has been skipped!\n")
                    print("The new top card is:",element,"\n")

                elif (self.top_card_color == self.bot_card_color and self.bot_card_action == "reverse") or (self.top_card_num == self.bot_card_action):
                    print("The opponent has reversed the order of cards back to them!\n")
                    print("The new top card is:",element,"\n")

                if self.bot_card_action == "wild_plus_four":

                    checker_for_bot_color_changer = 0
                    print("\The opponent will now change the color!")
                    while "wild" in self.enemy_hand[checker_for_bot_color_changer]:
                        checker_for_bot_color_changer += 1
                    if "red" in self.enemy_hand[checker_for_bot_color_changer]:
                        self.bot_card_color = "red"
                    elif "blue" in self.enemy_hand[checker_for_bot_color_changer]:
                        self.bot_card_color = "blue"
                    elif "yellow" in self.enemy_hand[checker_for_bot_color_changer]:
                        self.bot_card_color = "yellow"
                    elif "green" in self.enemy_hand[checker_for_bot_color_changer]:
                        self.bot_card_color = "green"
                    print("New top card color is now:",self.bot_card_color)

                    for i in range(4):
                        new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                        self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                        self.uno_full_deck.remove(self.new_added_card)
                        self.uno_add_later_deck.append(self.new_added_card)
                        self.your_hand.append(self.new_added_card)
                        self.your_hand_count += 1
                    self.your_successful_uno_count = 0
                          
                    print("\nThe opponent has gave you 4 cards!")

                elif self.bot_card_action == "wild":
                                        
                    print("\The opponent will now change the color!")
                    if "red" in self.enemy_hand[0]:
                        self.bot_card_color = "red"
                    elif "blue" in self.enemy_hand[0]:
                        self.bot_card_color = "blue"
                    elif "yellow" in self.enemy_hand[0]:
                        self.bot_card_color = "yellow"
                    elif "green" in self.enemy_hand[0]:
                        self.bot_card_color = "green"
                    print("New top card color is now:",self.bot_card_color)


                 # DELETE THIS, JUST FOR CHECKING PURPOSES:
                if self.bot_card_action != "":
                    print("ACTION:",self.bot_card_action)
                self.displaying_and_changing_info_after_bot_turn(element)

            if self.counter == 0 and self.bot_card_action != "":
                self.bot_card_action = ""
                    
    def displaying_and_changing_info_after_bot_turn(self,element):
        
        if (self.bot_card_color == self.top_card_color) or (self.bot_card_num == self.top_card_num) or ("wild" in element) or (self.top_card_num == self.bot_card_action):
            self.counter = 1
            if self.bot_card_action == "":
                self.top_card_num = self.bot_card_num
            else:
                if self.bot_card_action == "reverse":
                    self.top_card_num = "reverse"
                elif self.bot_card_action == "skip":
                    self.top_card_num = "skip"
                elif self.bot_card_action == "plus_2":
                    self.top_card_num = "plus_2"
                elif self.bot_card_action == "wild" or "wild_plus_four":
                    self.top_card_num = "wild"
            
            self.top_card = element
            self.top_card_color = self.bot_card_color
            self.uno_add_later_deck.append(element)
            self.enemy_hand.remove(element)
            self.enemy_hand_count -= 1

            print()
            print(self.top_card)
            print(self.enemy_hand)
            print()

    def your_uno_has_been_said(self):
        if self.your_successful_uno_count != 1:
            self.random_bot_block_choice = random.randint(1,5)
            if self.random_bot_block_choice == 4:
                print("Oh no! The opponent has blocked your UNO!")
                for new_cards in range(2):
                    new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                    self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                    self.uno_full_deck.remove(self.new_added_card)
                    self.uno_add_later_deck.append(self.new_added_card)
                    self.your_hand.append(self.new_added_card)
                    self.your_hand_count += 1
            else:
                print("Successful UNO has been called!")
                self.your_successful_uno_count = 1

    def block_on_bot_has_been_said(self):

        self.random_user_block_choice = random.randint(1,5)
        
        if self.random_user_block_choice == 1 or self.random_user_block_choice == 2: 
            print("Congratulations, You have blocked your opponent!")
            
            for new_cards in range(2):
                new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                self.uno_full_deck.remove(self.new_added_card)
                self.uno_add_later_deck.append(self.new_added_card)
                self.enemy_hand.append(self.new_added_card)
                self.enemy_hand_count += 1
                self.enemy_successful_uno_count = 0
        else:
            print("your block has failed")
            self.enemy_successful_uno_count = 1

    def bot_has_called_uno(self):
        self.random_bot_uno_choice = random.randint(1,3)
        if self.random_bot_uno_choice == 1 or self.random_bot_uno_choice == 2:
            print("The opponent has called UNO!")
            self.enemy_successful_uno_count = 1
        else:
            self.enemy_successful_uno_count = 0

my_uno_game = MyUNO()

# -----------/ SYMBOL MEANS FINISHED

# Get the decks -------------/
# Distribute to the two hands ---------------/
# Randomize the deck ---------/ 
# Draw random card to start game (flip up) -----------/
# You put your move and ensure they can only do correct ones -----------/
# Create a Pass Button -----------/
# Bot does their move -------------/
# When card hits one, they can type UNO ---------/
# you can block for the bot ------------/
# Declare winner ------------/
                         
