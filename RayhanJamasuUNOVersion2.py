# Rayhan Jamasi
# Jan 8th 2023
# Description: Create an UNO game with a bot. Have the player able to start with seven cards and they can click on
# a card to play. Ensure that they can only play valid cards and if a valid card is played, then the card is
# put into the middle and removed from there hand. The bot should also be able to play valid cards. If the
# user or bot can not play a valid card, they can draw a card. If the card they draw is still unplayable, then
# they can end there turn. The user should be able to call block if the bot is at one card or UNO if they
# are at one card. The user has access to hints in the helper display box and when the game is over, they can
# choose to quit or go back to the start screen. 

import random
import tkinter

# defining the class and def innit which will be executed at once
class MyUNO:
    def __init__(self):

        # Initializing self. variables
        self.uno_full_deck = []
        self.delete_list = []
        self.bot_delete_list = []
        self.your_hand = []
        self.enemy_hand = []
        self.blank_space_list = []
        self.bot_blank_space_list = []
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
        self.bot_card_choice = ""
        self.bot_card_num = ""
        self.bot_card_color = ""
        self.bot_new_added_card = ""
        self.new_added_card = ""
        self.uno_call = ""
        self.random_bot_block_choice = 0
        self.random_user_block_choice = 0
        self.your_successful_uno_count = 0
        self.enemy_successful_uno_count = 0
        self.repeat = True
        self.card_color_creator_checker = ""
        self.card_num_creator_checker = ""
        self.copy_count = 0
        self.uno_card = ""
        self.counter_for = 1
        self.counter_discard = 1
        self.bot_delete_hand = 1
        self.pass_counter = 0
        self.bot_num_checker = 0
        self.validator = 0
        self.wild_randomizer_choice = 0
        self.challenge_checking = 0
        self.enemy_plus_4 = False
        self.bot_pass_checker = 0
        self.destroy_button_checker = False
        self.user_block_counter = 0
        self.instruction_button_count = 0
        self.save_button_count = 0

        # Creating the main window and title
        self.main_window = tkinter.Tk()
        self.main_window.title("UNO Card Game")

        # Configuring the dimensions of the main window
        self.main_window.minsize(1380,600)
        self.main_window.maxsize(1380,600)

        # Changing the background color of the main window
        self.main_window.config(bg = "#FF6F27")

        # Creating the labels in the start screen
        self.start_label = tkinter.Label(self.main_window,text="",bg="#FF6F27")
        self.start_label_intro = tkinter.Label(self.main_window,text="Welcome To UNO!",bg="#FF6F27",fg="white",font="Times 50 bold")
        self.start_label_intro2 = tkinter.Label(self.main_window,text="Press The Button Below To Begin!",bg="#FF6F27",fg="white",font="Times 50 bold")        
        self.start_game_button = tkinter.Button(self.main_window,text="Start",bg="dark gray",fg="white",font="Times 30 bold",command=self.start_game)
        self.instructions_button = tkinter.Button(self.main_window,text="Rules",bg="dark gray",fg="white",font="Times 30 bold",command=self.instructions)

        # Placing the label at specific coordinates on the main window
        self.start_label.place(x=0,y=0,width=1380,height=600)
        self.start_label_intro.place(x=100,y=150,width=1200,height=100)
        self.start_label_intro2.place(x=100,y=250,width=1200,height=50)
        self.start_game_button.place(x=580,y=350,width=200,height=100)
        self.instructions_button.place(x=580,y=470,width=200,height=100)

        # Creating the StringVar variables that will be used in the discard pile
        self.top_card_num_display_var = tkinter.StringVar()
        self.top_card_color_display_var = tkinter.StringVar()

        # Creating the StringVar variables that will be used in the helper box, uno box, and draw box
        self.uno_display_var = tkinter.StringVar()
        self.draw_display_var = tkinter.StringVar()
        self.helper_display_var = tkinter.StringVar()

        # Creating the frames for the main window
        self.enemy_hand_frame = tkinter.Frame(self.main_window)
        self.discard_pile_frame = tkinter.Frame(self.main_window)
        self.your_hand_frame = tkinter.Frame(self.main_window)

        # Changing the color of the frames created
        self.enemy_hand_frame.config(bg = "#FF6F27")
        self.discard_pile_frame.config(bg = "#FF6F27")
        self.your_hand_frame.config(bg = "#FF6F27")

        # Packing the frames 
        self.enemy_hand_frame.pack()
        self.discard_pile_frame.pack()
        self.your_hand_frame.pack()

        # Opening the file to get the deck
        infile = open("uno_cards_for_deck.txt","r")

        # Reading the lines in the file opened and assigning to self.uno_full_deck
        self.uno_full_deck = infile.readlines()

        # Closing the file
        infile.close()

        # Rstripping of "\n" in the list created from the file's contents
        for i in range(len(self.uno_full_deck)):
            self.uno_full_deck[i] = self.uno_full_deck[i].rstrip("\n")

    # function defined with self as the 1 paramter, destroys all previous button and calling start_game_after_clicked
    def start_game(self):
        self.instructions_button.destroy()
        self.start_label.destroy()
        self.start_label_intro.destroy()
        self.start_label_intro2.destroy()
        self.start_game_button.destroy()
        self.start_game_after_clicked()

    # function defined with self as the 1 paramater, calls the corresponding functions before the game such as shuffling, dealing
    # hands, to choosing the top card, creating labels, and calling create user cards and create bot cards, then starting
    # tkinter main loop
    def start_game_after_clicked(self):

        self.shuffling_deck()  

        self.dealing_hands()      

        self.top_card_chooser()

        self.create_default_labels_and_buttons()

        self.create_discard_pile()

        self.displaying_cards_colors_and_num_your_hand()
        self.displaying_cards_colors_and_num_enemy_hand()
            
        tkinter.mainloop()

    # function with 1 paramater that makes the instructions
    def instructions(self):

        # deleting the instruction window if there are multiple
        if self.instruction_button_count == 1:
            self.instruction_window.destroy()
            self.instruction_button_count = 0

        # counting how many instruction windows there are and creating the variable
        self.instruction_button_count = 1
        instruction_var ="""                     INSTRUCTIONS FOR HOW TO PLAY UNO

                            GAME PLAY: 
                            gameplay usually follows a clockwise direction. Every player views his/her cards and tries to match the card in the Discard Pile.
                            You have to match either by the number, color, or the symbol/Action. For instance, if the Discard Pile has a red card that is an 8
                            you have to place either a red card or a card with an 8 on it. You can also play a Wild card (which can alter current color in play).
                            If the player has no matches or they choose not to play any of their cards even though they might have a match, they
                            must draw a card from the Draw pile.
                            If that card can be played, play it. Otherwise, keep the card, and the game moves on to the next person in turn.

                            You can also play a Wild card, or a +4 card on your turn.
                            The game continues until a player has one card left. The moment a player has just one card they must yell “UNO!”.
                            If they are caught not saying “Uno” by another player before the next player has taken their turn, that player must draw two
                            new cards as a penalty.

                            Assuming that the player is unable to play/discard their last card and needs to draw, but after drawing, is then
                            able to play/discard that penultimate card,
                            the player has to repeat the action of calling out “Uno”. The bottom line is – Announcing “Uno” needs to be repeated
                            every time you are left with one card.
                            Once a player has no cards remaining, the game round is over, points are scored, and the game begins over again.

                            ACTION CARDS
                            REVERSE – If going clockwise, switch to counterclockwise or vice versa. It can only be played on a
                            card that matches by color, or on another Reverse card.
                            If turned up at the beginning of play, the dealer goes first, and the player to the dealer’s right
                            is next (normally it would be the player to the dealer’s left).

                            SKIP CARD – When a player places this card, the next player has to skip their turn. It can only be
                            played on a card that matches by color, or on another Skip card.
                            If turned up at the beginning of play, the first player (to the dealer’s left) loses his/her turn.
                            The next player to that player’s right starts the game instead.

                            +2 CARD – When a person places this card, the next player will have to pick up two cards and forfeit his/her turn.
                            It can only be played on a card that matches by color, or on another Draw Two. If turned up at
                            the beginning of play, the first player draws two cards and gets skipped.

                            WILD CARD – This card represents all four colors, and can be placed on any card. The player
                            has to state which color it will represent for the next player.
                            It can be played regardless of whether another card is available. If turned up at the
                            beginning of play, the first player chooses what color to continue play.

                            +4 CARD – This acts just like the wild card except that the next player also has to draw
                            four cards as well as forfeit his/her turn.
                            With this card, you must have no other alternative cards to play that matches the color of the card previously played.
                            If you play this card illegally, you may be challenged by the other player to show your hand to him/her.

                            If guilty, you need to draw 4 cards. If not, the challenger needs to draw 6 cards instead.
                            If turned up at the beginning of play, return this card to the Draw pile, shuffle, and turn up a new one. """

        # creating the instruction window and naming it
        self.instruction_window = tkinter.Tk()
        self.instruction_window.title("Instructions Window")

        # configuring instruction window dimensions
        self.instruction_window.minsize(1200,800)
        self.instruction_window.maxsize(1200,800)

        # configuring instruction window color
        self.instruction_window.config(bg = "black")

        # creating label used for instructions
        self.instruction_label = tkinter.Label(self.instruction_window,text=instruction_var,fg="white", bg="black", font = "Times 13 bold")
        self.instruction_label.place(x=0,y=10,width=1100,height=800)

        # creating the quit button
        self.instruction_quit_button = tkinter.Button(self.instruction_window,text="QUIT",fg="white",bg="red",font= "Times 40 bold",command = self.quit_instruction)
        self.instruction_quit_button.place(x=950,y=400,width=120,height=100)

    # destroys the window if there are multiple and makes button count = 0. defining functions with 1 paramater as self
    def quit_instruction(self):
        self.instruction_window.destroy()
        self.instruction_button_count = 0

    # defining the defualt labels and buttons that will be used. defining function 1 self as 1 paramter
    def create_default_labels_and_buttons(self):

        # creating uno label display and coordinates
        self.uno_label_display = tkinter.Label(self.main_window,text="UNO display box",bg="#FF6F27",font = "Times 26 bold")
        self.uno_label_display.place(x=1000,y=480,width=350,height=50)

        # creating the variable that will be updated and coordinates
        self.uno_label_widget = tkinter.Label(self.main_window,textvariable = self.uno_display_var, bg = "#52AF48", font = "Times 17 bold")
        self.uno_label_widget.place(x=1000,y=523,width=350,height=50)

        # setting the draw variable and the labels above for pass
        self.draw_display_var.set("Draw")
        self.pass_button = tkinter.Button(self.main_window, textvariable = self.draw_display_var, fg = "#D5BBE2", bg = "black",font = "Times 20 bold", command = self.pass_choice)
        self.pass_button_title = tkinter.Label(self.main_window,text="Click Here To Pass",width=0,bg="#FF6F27",font="Times 25 bold")
        self.pass_button_title2 = tkinter.Label(self.main_window,text="Or End Your Turn",width=0,bg="#FF6F27", font="Times 25 bold")

        # coordinates of the pass buttons and label
        self.pass_button_title.place(x=400,y=135,width=250,height=21)
        self.pass_button.place(x=475,y=170,width=80,height=100)
        self.pass_button_title2.place(x=400,y=285,width=250,height=21)

        # creating label and coordinates of uno label display
        self.call_uno_button = tkinter.Button(self.main_window,text="UNO!",fg="white", bg = "purple",font = "Times 25 bold",command=self.your_uno_has_been_said)
        self.call_uno_button.place(x=470,y=470,width=180,height=85)

        # creating block button and coordinates
        self.call_block_button = tkinter.Button(self.main_window, text="BLOCK!",fg="black", bg = "pink", font = "Times 25 bold",command=self.block_on_bot_has_been_said)
        self.call_block_button.place(x=720,y=470,width=180,height=85)

        # creating helper stringvar variable and coordinates
        self.helper_display = tkinter.Label(self.main_window,textvariable = self.helper_display_var,bg = "#52AF48", font = "Times 17 bold")
        self.helper_display.place(x=24,y=523,width=350,height=53)

        # creating helper title label and coordinates
        self.help_display_title = tkinter.Label(self.main_window,text="Helper Display Box",bg ="#FF6F27",font = "Times 26 bold")
        self.help_display_title.place(x=24,y=480,width=350,height=50)

        # creating instruction button and coordinates
        self.instruction_button = tkinter.Button(self.main_window,text="Rules",bg="dark gray",fg="#D5BBE2",font="Times 35 bold",command=self.instructions)
        self.instruction_button.place(x=200,y=168,width=130,height=100)

        # creating quit button and coordinates
        self.quit_button = tkinter.Button(self.main_window,text="QUIT",bg="dark gray",fg="red",font="Times 35 bold",command=self.quit_main_window)
        self.quit_button.place(x=40,y=168,width=130,height=100)

    # defining winner checker with 1 paramater as self
    def winner_checker(self):

        # checking if someone has won, deleting the windows, opening replay screen and display defeat or victory by using if statements
        # with different variables. 
        if self.enemy_hand_count == 0 or self.your_hand_count == 0:
            self.repeat = False
            
            self.main_window.destroy()
            self.replay_main_window = tkinter.Tk()
            self.replay_main_window.title("UNO Replay Screen")

            self.replay_main_window.minsize(1380,600)
            self.replay_main_window.maxsize(1380,600)

            self.replay_main_window.config(bg = "#FF6F27")

            if self.enemy_hand_count == 0:
                self.replay_game = tkinter.Label(self.replay_main_window,text="DEFEAT! Would you like to go to menu and play again?",fg="white", bg = "#FF6F27", font = "Times 47 bold")
                self.replay_game.place(x=60,y=100,width=1300,height=100)
            else:
                self.replay_game = tkinter.Label(self.replay_main_window,text="VICTORY! Would you like to go to menu and play again?",fg="white", bg = "#FF6F27", font = "Times 47 bold")
                self.replay_game.place(x=60,y=100,width=1300,height=100)

            self.replay_button = tkinter.Button(self.replay_main_window, text="RESTART!",bg="#EC554B", font = "Times 40 bold",fg="white",command=self.restart)
            self.replay_button.place(x=500,y=220,width=300,height=100)

            self.quit_button = tkinter.Button(self.replay_main_window, text="Quit",bg="#EC554B", font = "Times 40 bold",fg="white",command=self.quit)
            self.quit_button.place(x=500,y=340,width=300,height=100)

            tkinter.mainloop()

    # defining quit button that will destroy replay window
    def quit(self):
        self.replay_main_window.destroy()

    # defining quit_main_window function that destroys main window
    def quit_main_window(self):
        self.main_window.destroy()

    # defining restart button that restarts game
    def restart(self):
        self.replay_main_window.destroy()
        play_uno_again = MyUNO()

    # defining uno has been said and seeing if the user called a valid uno, if so then deciding if the bot has already called uno or not.
    # this will either say successful uno or blocked by opponent and either distribute cards to you. 
    def your_uno_has_been_said(self):
        if self.validator == 0:
            if self.your_successful_uno_count == 0:
                self.random_bot_block_choice = random.randint(1,5)
                if self.random_bot_block_choice == 4:
                    self.uno_display_var.set("Blocked By Opponent, Gain 2 cards")
                                             
                    for new_cards in range(2):
                        new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                        self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                        self.uno_full_deck.remove(self.new_added_card)
                        self.your_hand.append(self.new_added_card)
                        self.your_hand_count += 1
                    self.displaying_cards_colors_and_num_your_hand()
                else:
                    self.uno_display_var.set("Successful UNO!")
                    self.your_successful_uno_count = 1

    # defining block on bot which is used when you call the block and seeing if valid and dealing the correct consequences
    def block_on_bot_has_been_said(self):
        if self.validator == 0 and self.enemy_hand_count == 1 and self.user_block_counter == 0:
            self.user_block_counter = 1
            self.random_user_block_choice = random.randint(1,5)
            
            if self.random_user_block_choice == 1 or self.random_user_block_choice == 2: 
                self.uno_display_var.set("Congratulations, Opponent blocked!")
                
                for new_cards in range(2):
                    new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                    self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                    self.uno_full_deck.remove(self.new_added_card)
                    self.enemy_hand.append(self.new_added_card)
                    self.enemy_hand_count += 1
                    self.enemy_successful_uno_count = 0
                    self.displaying_cards_colors_and_num_enemy_hand()
                self.user_block_counter = 0
            else:
                self.uno_display_var.set("Failed block") 
                self.enemy_successful_uno_count = 1

    # seeing if the bot has called uno and if successful
    def bot_has_called_uno(self):
        self.random_bot_uno_choice = random.randint(1,3)
        if self.random_bot_uno_choice == 1 or self.random_bot_uno_choice == 2:
            self.uno_display_var.set("The opponent has called UNO")
            self.enemy_successful_uno_count = 1
        else:
            self.enemy_successful_uno_count = 0

    # dealing the hands to the players for the bot and user
    def dealing_hands(self):

        # initalizing randomizer variable which will be used 
        randomizer = 0
        
        while self.your_hand_count < 7:
            randomizer = random.randint(0,len(self.uno_full_deck) - 1)
            self.card = self.uno_full_deck[randomizer]
            self.your_hand.append(self.card)
            self.uno_full_deck.remove(self.card)
            self.your_hand_count += 1

        while self.enemy_hand_count < 7:
            randomizer = random.randint(0,len(self.uno_full_deck) - 1)
            self.card = self.uno_full_deck[randomizer]
            self.enemy_hand.append(self.card)
            self.uno_full_deck.remove(self.card)
            self.enemy_hand_count += 1

    # creating the buttons for red if the user draws a red card
    def input_r0(self):
        if self.copy_count == 1:
            self.input_r0_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "0"
            user_card_color = "red"
            self.user_chosen_card(user_card_num, user_card_color, self.input_r0_var)

    def input_r1(self):
        if self.copy_count == 1:
            self.input_r1_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "1"
            user_card_color = "red"
            self.user_chosen_card(user_card_num, user_card_color, self.input_r1_var)

    def input_r2(self):
        if self.copy_count == 1:
            self.input_r2_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "2"
            user_card_color = "red"
            self.user_chosen_card(user_card_num, user_card_color, self.input_r2_var)

    def input_r3(self):
        if self.copy_count == 1:
            self.input_r3_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "3"
            user_card_color = "red"
            self.user_chosen_card(user_card_num, user_card_color, self.input_r3_var)

    def input_r4(self):
        if self.copy_count == 1:
            self.input_r4_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "4"
            user_card_color = "red"
            self.user_chosen_card(user_card_num, user_card_color, self.input_r4_var)

    def input_r5(self):
        if self.copy_count == 1:
            self.input_r5_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "5"
            user_card_color = "red"
            self.user_chosen_card(user_card_num, user_card_color, self.input_r5_var)

    def input_r6(self):
        if self.copy_count == 1:
            self.input_r6_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "6"
            user_card_color = "red"
            self.user_chosen_card(user_card_num, user_card_color, self.input_r6_var)

    def input_r7(self):
        if self.copy_count == 1:
            self.input_r7_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "7"
            user_card_color = "red"
            self.user_chosen_card(user_card_num, user_card_color, self.input_r7_var)

    def input_r8(self):
        if self.copy_count == 1:
            self.input_r8_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "8"
            user_card_color = "red"
            self.user_chosen_card(user_card_num, user_card_color, self.input_r8_var)

    def input_r9(self):
        if self.copy_count == 1:
            self.input_r9_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "9"
            user_card_color = "red"
            self.user_chosen_card(user_card_num, user_card_color, self.input_r9_var)

    def input_r_p2(self):
        if self.copy_count == 1:
            self.input_r_p2_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "+2"
            user_card_color = "red"
            self.user_chosen_card(user_card_num, user_card_color, self.input_r_p2_var)

    def input_r_r(self):
        if self.copy_count == 1:
            self.input_r_r_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "⟲"
            user_card_color = "red"
            self.user_chosen_card(user_card_num, user_card_color, self.input_r_r_var)

    def input_r_s(self):
        if self.copy_count == 1:
            self.input_r_s_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "skip"
            user_card_color = "red"
            self.user_chosen_card(user_card_num, user_card_color, self.input_r_s_var)

    # creating the buttons if the user draws a blue card
    def input_b0(self):
        if self.copy_count == 1:
            self.input_b0_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "0"
            user_card_color = "blue"
            self.user_chosen_card(user_card_num, user_card_color, self.input_b0_var)

    def input_b1(self):
        if self.copy_count == 1:
            self.input_b1_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "1"
            user_card_color = "blue"
            self.user_chosen_card(user_card_num, user_card_color, self.input_b1_var)

    def input_b2(self):
        if self.copy_count == 1:
            self.input_b2_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "2"
            user_card_color = "blue"
            self.user_chosen_card(user_card_num, user_card_color, self.input_b2_var)

    def input_b3(self):
        if self.copy_count == 1:
            self.input_b3_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "3"
            user_card_color = "blue"
            self.user_chosen_card(user_card_num, user_card_color, self.input_b3_var)

    def input_b4(self):
        if self.copy_count == 1:
            self.input_b4_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "4"
            user_card_color = "blue"
            self.user_chosen_card(user_card_num, user_card_color, self.input_b4_var)

    def input_b5(self):
        if self.copy_count == 1:
            self.input_b5_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "5"
            user_card_color = "blue"
            self.user_chosen_card(user_card_num, user_card_color, self.input_b5_var)

    def input_b6(self):
        if self.copy_count == 1:
            self.input_b6_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "6"
            user_card_color = "blue"
            self.user_chosen_card(user_card_num, user_card_color, self.input_b6_var)

    def input_b7(self):
        if self.copy_count == 1:
            self.input_b7_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "7"
            user_card_color = "blue"
            self.user_chosen_card(user_card_num, user_card_color, self.input_b7_var)

    def input_b8(self):
        if self.copy_count == 1:
            self.input_b8_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "8"
            user_card_color = "blue"
            self.user_chosen_card(user_card_num, user_card_color, self.input_b8_var)

    def input_b9(self):
        if self.copy_count == 1:
            self.input_b9_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "9"
            user_card_color = "blue"
            self.user_chosen_card(user_card_num, user_card_color, self.input_b9_var)

    def input_b_p2(self):
        if self.copy_count == 1:
            self.input_b_p2_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "+2"
            user_card_color = "blue"
            self.user_chosen_card(user_card_num, user_card_color, self.input_b_p2_var)

    def input_b_r(self):
        if self.copy_count == 1:
            self.input_b_r_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "⟲"
            user_card_color = "blue"
            self.user_chosen_card(user_card_num, user_card_color, self.input_b_r_var)

    def input_b_s(self):
        if self.copy_count == 1:
            self.input_b_s_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "skip"
            user_card_color = "blue"
            self.user_chosen_card(user_card_num, user_card_color, self.input_b_s_var)

    # creating buttons if the user draws a green card
    def input_g0(self):
        if self.copy_count == 1:
            self.input_g0_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "0"
            user_card_color = "green"
            self.user_chosen_card(user_card_num, user_card_color, self.input_g0_var)

    def input_g1(self):
        if self.copy_count == 1:
            self.input_g1_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "1"
            user_card_color = "green"
            self.user_chosen_card(user_card_num, user_card_color, self.input_g1_var)

    def input_g2(self):
        if self.copy_count == 1:
            self.input_g2_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "2"
            user_card_color = "green"
            self.user_chosen_card(user_card_num, user_card_color, self.input_g2_var)

    def input_g3(self):
        if self.copy_count == 1:
            self.input_g3_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "3"
            user_card_color = "green"
            self.user_chosen_card(user_card_num, user_card_color, self.input_g3_var)

    def input_g4(self):
        if self.copy_count == 1:
            self.input_g4_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "4"
            user_card_color = "green"
            self.user_chosen_card(user_card_num, user_card_color, self.input_g4_var)

    def input_g5(self):
        if self.copy_count == 1:
            self.input_g5_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "5"
            user_card_color = "green"
            self.user_chosen_card(user_card_num, user_card_color, self.input_g5_var)

    def input_g6(self):
        if self.copy_count == 1:
            self.input_g6_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "6"
            user_card_color = "green"
            self.user_chosen_card(user_card_num, user_card_color, self.input_g6_var)

    def input_g7(self):
        if self.copy_count == 1:
            self.input_g7_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "7"
            user_card_color = "green"
            self.user_chosen_card(user_card_num, user_card_color, self.input_g7_var)

    def input_g8(self):
        if self.copy_count == 1:
            self.input_g8_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "8"
            user_card_color = "green"
            self.user_chosen_card(user_card_num, user_card_color, self.input_g8_var)

    def input_g9(self):
        if self.copy_count == 1:
            self.input_g9_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "9"
            user_card_color = "green"
            self.user_chosen_card(user_card_num, user_card_color, self.input_g9_var)

    def input_g_p2(self):
        if self.copy_count == 1:
            self.input_g_p2_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "+2"
            user_card_color = "green"
            self.user_chosen_card(user_card_num, user_card_color, self.input_g_p2_var)

    def input_g_r(self):
        if self.copy_count == 1:
            self.input_g_r_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "⟲"
            user_card_color = "green"
            self.user_chosen_card(user_card_num, user_card_color, self.input_g_r_var)

    def input_g_s(self):
        if self.copy_count == 1:
            self.input_g_s_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "skip"
            user_card_color = "green"
            self.user_chosen_card(user_card_num, user_card_color, self.input_g_s_var)

    # creating buttons if the user draws a yellow card 
    def input_y0(self):
        if self.copy_count == 1:
            self.input_y0_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "0"
            user_card_color = "yellow"
            self.user_chosen_card(user_card_num, user_card_color, self.input_y0_var)

    def input_y1(self):
        if self.copy_count == 1:
            self.input_y1_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "1"
            user_card_color = "yellow"
            self.user_chosen_card(user_card_num, user_card_color, self.input_y1_var)

    def input_y2(self):
        if self.copy_count == 1:
            self.input_y2_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "2"
            user_card_color = "yellow"
            self.user_chosen_card(user_card_num, user_card_color, self.input_y2_var)

    def input_y3(self):
        if self.copy_count == 1:
            self.input_y3_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "3"
            user_card_color = "yellow"
            self.user_chosen_card(user_card_num, user_card_color, self.input_y3_var)

    def input_y4(self):
        if self.copy_count == 1:
            self.input_y4_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "4"
            user_card_color = "yellow"
            self.user_chosen_card(user_card_num, user_card_color, self.input_y4_var)

    def input_y5(self):
        if self.copy_count == 1:
            self.input_y5_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "5"
            user_card_color = "yellow"
            self.user_chosen_card(user_card_num, user_card_color, self.input_y5_var)

    def input_y6(self):
        if self.copy_count == 1:
            self.input_y6_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "6"
            user_card_color = "yellow"
            self.user_chosen_card(user_card_num, user_card_color, self.input_y6_var)

    def input_y7(self):
        if self.copy_count == 1:
            self.input_y7_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "7"
            user_card_color = "yellow"
            self.user_chosen_card(user_card_num, user_card_color, self.input_y7_var)

    def input_y8(self):
        if self.copy_count == 1:
            self.input_y8_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "8"
            user_card_color = "yellow"
            self.user_chosen_card(user_card_num, user_card_color, self.input_y8_var)

    def input_y9(self):
        if self.copy_count == 1:
            self.input_y9_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "9"
            user_card_color = "yellow"
            self.user_chosen_card(user_card_num, user_card_color, self.input_y9_var)

    def input_y_p2(self):
        if self.copy_count == 1:
            self.input_y_p2_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "+2"
            user_card_color = "yellow"
            self.user_chosen_card(user_card_num, user_card_color, self.input_y_p2_var)

    def input_y_r(self):
        if self.copy_count == 1:
            self.input_y_r_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "⟲"
            user_card_color = "yellow"
            self.user_chosen_card(user_card_num, user_card_color, self.input_y_r_var)

    def input_y_s(self):
        if self.copy_count == 1:
            self.input_y_s_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "skip"
            user_card_color = "yellow"
            self.user_chosen_card(user_card_num, user_card_color, self.input_y_s_var)

    # creating buttons for wild and +4 card
    def input_wild_plus_four(self):
        if self.copy_count == 1:
            self.input_wild_plus_four_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "+4"
            user_card_color = "black"
            self.user_chosen_card(user_card_num,user_card_color,self.input_wild_plus_four_var)

    def input_wild(self):
        if self.copy_count == 1:
            self.input_wild_var = self.uno_card
            self.copy_count = 0
        else:
            user_card_num = "wild"
            user_card_color = "black"
            self.user_chosen_card(user_card_num,user_card_color,self.input_wild_var)

    # used to ensure it goes through the first if statement first 
    def copy_check_for_removal_later(self,uno_card):
        self.copy_count = 1
        self.uno_card = uno_card

    # displaying the cards on the bottom of the screen for you
    def displaying_cards_colors_and_num_your_hand(self):

        self.random_hints()

        if self.counter_for == 0:
            for card in self.delete_list:
                card.destroy()
            for space in self.blank_space_list:
                space.destroy()

        for card in self.your_hand:
            self.find_command(card)

            self.blank_space = tkinter.Label(self.your_hand_frame,text="",bg="#FF6F27")
                
            self.blank_space.pack(side="left")

            self.blank_space_list.append(self.blank_space)
            
        if self.top_card_num == "+4" and self.enemy_plus_4 == True:
            
            self.challenge_button = tkinter.Button(self.main_window,text="CHALLENGE?",bg="red",fg="white",font = "Impact 30 bold",command=self.user_challenge)
            self.challenge_button.place(x=750,y=168,width=200,height=100)

    # function used for if the user challenges, defined function with 1 paramater as self
    def user_challenge(self):
        for card in self.bot_delete_list:
            card.destroy()
        self.bot_delete_hand = 1
        self.challenged_wild_plus_four_card()

    # makes red, blue, yellow, and green buttons that add to delete list and call specific functions depending on which is called
    def find_command(self,element):

        if "red" in element:
            if "zero" in element:
                self.your_hand_card_creator_r0 = tkinter.Button(self.your_hand_frame,text = "0", \
                                bg = "red", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_r0)
                self.your_hand_card_creator_r0.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_r0)
                self.input_r0()
                
            elif "one" in element:
                self.your_hand_card_creator_r1 = tkinter.Button(self.your_hand_frame,text = "1", \
                                bg = "red", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_r1)
                self.your_hand_card_creator_r1.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_r1)
                self.input_r1()
                
            elif "two" in element:
                self.your_hand_card_creator_r2 = tkinter.Button(self.your_hand_frame,text = "2", \
                                bg = "red", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_r2)
                self.your_hand_card_creator_r2.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_r2)
                self.input_r2()
                
            elif "three" in element:
                self.your_hand_card_creator_r3 = tkinter.Button(self.your_hand_frame,text = "3", \
                                bg = "red", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_r3)
                self.your_hand_card_creator_r3.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_r3)
                self.input_r3()
                
            elif "four" in element:
                self.your_hand_card_creator_r4 = tkinter.Button(self.your_hand_frame,text = "4", \
                                bg = "red", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_r4)
                self.your_hand_card_creator_r4.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_r4)
                self.input_r4()
                
            elif "five" in element:
                self.your_hand_card_creator_r5 = tkinter.Button(self.your_hand_frame,text = "5", \
                                bg = "red", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_r5)
                self.your_hand_card_creator_r5.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_r5)
                self.input_r5()
                
            elif "six" in element:
                self.your_hand_card_creator_r6 = tkinter.Button(self.your_hand_frame,text = "6", \
                                bg = "red", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_r6)
                self.your_hand_card_creator_r6.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_r6)
                self.input_r6()
                
            elif "seven" in element:
                self.your_hand_card_creator_r7 = tkinter.Button(self.your_hand_frame,text = "7", \
                                bg = "red", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_r7)
                self.your_hand_card_creator_r7.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_r7)
                self.input_r7()
                
            elif "eight" in element:
                self.your_hand_card_creator_r8 = tkinter.Button(self.your_hand_frame,text = "8", \
                                bg = "red", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_r8)
                self.your_hand_card_creator_r8.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_r8)
                self.input_r8()
                
            elif "nine" in element:
                self.your_hand_card_creator_r9 = tkinter.Button(self.your_hand_frame,text = "9", \
                                bg = "red", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_r9)
                self.your_hand_card_creator_r9.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_r9)
                self.input_r9()
                
            elif "plus_2" in element:
                self.your_hand_card_creator_r_p2 = tkinter.Button(self.your_hand_frame,text = "+2", \
                                bg = "red", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_r_p2)
                self.your_hand_card_creator_r_p2.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_r_p2)
                self.input_r_p2()
                
            elif "skip" in element:
                self.your_hand_card_creator_r_s = tkinter.Button(self.your_hand_frame,text = "Skip", \
                                bg = "red", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_r_s)
                self.your_hand_card_creator_r_s.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_r_s)
                self.input_r_s()
                
            elif "reverse" in element:
                self.your_hand_card_creator_r_r = tkinter.Button(self.your_hand_frame,text = "⟲", \
                                bg = "red", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_r_r)
                self.your_hand_card_creator_r_r.pack(side="left")
                self.delete_list.append(self.your_hand_card_creator_r_r)
                self.copy_check_for_removal_later(element)
                self.input_r_r()
                
        elif "blue" in element:
            if "zero" in element:
                self.your_hand_card_creator_b0 = tkinter.Button(self.your_hand_frame,text = "0", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_b0)
                self.your_hand_card_creator_b0.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_b0)
                self.input_b0()
                
            elif "one" in element:
                self.your_hand_card_creator_b1 = tkinter.Button(self.your_hand_frame,text = "1", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_b1)
                self.your_hand_card_creator_b1.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_b1)
                self.input_b1()
                
            elif "two" in element:
                self.your_hand_card_creator_b2 = tkinter.Button(self.your_hand_frame,text = "2", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_b2)
                self.your_hand_card_creator_b2.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_b2)
                self.input_b2()
                
            elif "three" in element:
                self.your_hand_card_creator_b3 = tkinter.Button(self.your_hand_frame,text = "3", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_b3)
                self.your_hand_card_creator_b3.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_b3)
                self.input_b3()
                
            elif "four" in element:
                self.your_hand_card_creator_b4 = tkinter.Button(self.your_hand_frame,text = "4", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_b4)
                self.your_hand_card_creator_b4.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_b4)
                self.input_b4()
                
            elif "five" in element:
                self.your_hand_card_creator_b5 = tkinter.Button(self.your_hand_frame,text = "5", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_b5)
                self.your_hand_card_creator_b5.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_b5)
                self.input_b5()
                
            elif "six" in element:
                self.your_hand_card_creator_b6 = tkinter.Button(self.your_hand_frame,text = "6", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_b6)
                self.your_hand_card_creator_b6.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_b6)
                self.input_b6()
                
            elif "seven" in element:
                self.your_hand_card_creator_b7 = tkinter.Button(self.your_hand_frame,text = "7", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_b7)
                self.your_hand_card_creator_b7.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_b7)
                self.input_b7()
                
            elif "eight" in element:
                self.your_hand_card_creator_b8 = tkinter.Button(self.your_hand_frame,text = "8", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_b8)
                self.your_hand_card_creator_b8.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_b8)
                self.input_b8()
                
            elif "nine" in element:
                self.your_hand_card_creator_b9 = tkinter.Button(self.your_hand_frame,text = "9", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_b9)
                self.your_hand_card_creator_b9.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_b9)
                self.input_b9()
                
            elif "plus_2" in element:
                self.your_hand_card_creator_b_p2 = tkinter.Button(self.your_hand_frame,text = "+2", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_b_p2)
                self.your_hand_card_creator_b_p2.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_b_p2)
                self.input_b_p2()

            elif "skip" in element:
                self.your_hand_card_creator_b_s = tkinter.Button(self.your_hand_frame,text = "Skip", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_b_s)
                self.your_hand_card_creator_b_s.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_b_s)
                self.input_b_s()

            elif "reverse" in element:
                self.your_hand_card_creator_b_r = tkinter.Button(self.your_hand_frame,text = "⟲", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_b_r)
                self.your_hand_card_creator_b_r.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_b_r)
                self.input_b_r()

        elif "green" in element:
            if "zero" in element:
                self.your_hand_card_creator_g0 = tkinter.Button(self.your_hand_frame,text = "0", \
                                bg = "blue", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_g0)
                self.your_hand_card_creator_g0.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_g0)
                self.input_g0()
                
            elif "one" in element:
                self.your_hand_card_creator_g1 = tkinter.Button(self.your_hand_frame,text = "1", \
                                bg = "green", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_g1)
                self.your_hand_card_creator_g1.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_g1)
                self.input_g1()
            
            elif "two" in element:
                self.your_hand_card_creator_g2 = tkinter.Button(self.your_hand_frame,text = "2", \
                                bg = "green", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_g2)
                self.your_hand_card_creator_g2.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_g2)
                self.input_g2()
                
            elif "three" in element:
                self.your_hand_card_creator_g3 = tkinter.Button(self.your_hand_frame,text = "3", \
                                bg = "green", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_g3)
                self.your_hand_card_creator_g3.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_g3)
                self.input_g3()
                
            elif "four" in element:
                self.your_hand_card_creator_g4 = tkinter.Button(self.your_hand_frame,text = "4", \
                                bg = "green", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_g4)
                self.your_hand_card_creator_g4.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_g4)
                self.input_g4()
                
            elif "five" in element:
                self.your_hand_card_creator_g5 = tkinter.Button(self.your_hand_frame,text = "5", \
                                bg = "green", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_g5)
                self.your_hand_card_creator_g5.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_g5)
                self.input_g5()
                
            elif "six" in element:
                self.your_hand_card_creator_g6 = tkinter.Button(self.your_hand_frame,text = "6", \
                                bg = "green", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_g6)
                self.your_hand_card_creator_g6.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_g6)
                self.input_g6()
                
            elif "seven" in element:
                self.your_hand_card_creator_g7 = tkinter.Button(self.your_hand_frame,text = "7", \
                                bg = "green", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_g7)
                self.your_hand_card_creator_g7.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_g7)
                self.input_g7()
                
            elif "eight" in element:
                self.your_hand_card_creator_g8 = tkinter.Button(self.your_hand_frame,text = "8", \
                                bg = "green", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_g8)
                self.your_hand_card_creator_g8.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_g8)
                self.input_g8()
                
            elif "nine" in element:
                self.your_hand_card_creator_g9 = tkinter.Button(self.your_hand_frame,text = "9", \
                                bg = "green", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_g9)
                self.your_hand_card_creator_g9.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_g9)
                self.input_g9()

            elif "plus_2" in element:
                self.your_hand_card_creator_g_p2 = tkinter.Button(self.your_hand_frame,text = "+2", \
                                bg = "green", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_g_p2)
                self.your_hand_card_creator_g_p2.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_g_p2)
                self.input_g_p2()

            elif "skip" in element:
                self.your_hand_card_creator_g_s = tkinter.Button(self.your_hand_frame,text = "Skip", \
                                bg = "green", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_g_s)
                self.your_hand_card_creator_g_s.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_g_s)
                self.input_g_s()
                
            elif "reverse" in element:
                self.your_hand_card_creator_g_r= tkinter.Button(self.your_hand_frame,text = "⟲", \
                                bg = "green", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_g_r)
                self.your_hand_card_creator_g_r.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_g_r)
                self.input_g_r()
                
        elif "yellow" in element:
            if "zero" in element:
                self.your_hand_card_creator_y0 = tkinter.Button(self.your_hand_frame,text = "0", \
                                bg = "yellow", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_y0)
                self.your_hand_card_creator_y0.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_y0)
                self.input_y0()
                
            elif "one" in element:
                self.your_hand_card_creator_y1 = tkinter.Button(self.your_hand_frame,text = "1", \
                                bg = "yellow", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_y1)
                self.your_hand_card_creator_y1.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_y1)
                self.input_y1()
                
            elif "two" in element:
                self.your_hand_card_creator_y2 = tkinter.Button(self.your_hand_frame,text = "2", \
                                bg = "yellow", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_y2)
                self.your_hand_card_creator_y2.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_y2)
                self.input_y2()
                
            elif "three" in element:
                self.your_hand_card_creator_y3 = tkinter.Button(self.your_hand_frame,text = "3", \
                                bg = "yellow", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_y3)
                self.your_hand_card_creator_y3.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_y3)
                self.input_y3()
                
            elif "four" in element:
                self.your_hand_card_creator_y4 = tkinter.Button(self.your_hand_frame,text = "4", \
                                bg = "yellow", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_y4)
                self.your_hand_card_creator_y4.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_y4)
                self.input_y4()
                
            elif "five" in element:
                self.your_hand_card_creator_y5 = tkinter.Button(self.your_hand_frame,text = "5", \
                                bg = "yellow", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_y5)
                self.your_hand_card_creator_y5.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_y5)
                self.input_y5()
                
            elif "six" in element:
                self.your_hand_card_creator_y6= tkinter.Button(self.your_hand_frame,text = "6", \
                                bg = "yellow", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_y6)
                self.your_hand_card_creator_y6.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_y6)
                self.input_y6()
                
            elif "seven" in element:
                self.your_hand_card_creator_y7 = tkinter.Button(self.your_hand_frame,text = "7", \
                                bg = "yellow", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_y7)
                self.your_hand_card_creator_y7.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_y7)
                self.input_y7()
                
            elif "eight" in element:
                self.your_hand_card_creator_y8 = tkinter.Button(self.your_hand_frame,text = "8", \
                                bg = "yellow", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_y8)
                self.your_hand_card_creator_y8.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_y8)
                self.input_y8()
                
            elif "nine" in element:
                self.your_hand_card_creator_y9 = tkinter.Button(self.your_hand_frame,text = "9", \
                                bg = "yellow", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_y9)
                self.your_hand_card_creator_y9.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_y9)
                self.input_y9()

            elif "plus_2" in element:
                self.your_hand_card_creator_y_p2 = tkinter.Button(self.your_hand_frame,text = "+2", \
                                bg = "yellow", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_y_p2)
                self.your_hand_card_creator_y_p2.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_y_p2)
                self.input_y_p2()
                
            elif "skip" in element:
                self.your_hand_card_creator_y_s = tkinter.Button(self.your_hand_frame,text = "Skip", \
                                bg = "yellow", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_y_s)
                self.your_hand_card_creator_y_s.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_y_s)
                self.input_y_s()
                
            elif "reverse" in element:
                self.your_hand_card_creator_y_r = tkinter.Button(self.your_hand_frame,text = "⟲", \
                                bg = "yellow", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_y_r)
                self.your_hand_card_creator_y_r.pack(side="left")
                self.copy_check_for_removal_later(element)
                self.delete_list.append(self.your_hand_card_creator_y_r)
                self.input_y_r()
                
        if "wild_plus_four" in element:
            self.your_hand_card_creator_wp4= tkinter.Button(self.your_hand_frame,text = "+4", \
                                bg = "black", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_wild_plus_four)
            self.your_hand_card_creator_wp4.pack(side="left")
            self.copy_check_for_removal_later(element)
            self.delete_list.append(self.your_hand_card_creator_wp4)
            self.input_wild_plus_four()

        elif "wild" in element:
            self.your_hand_card_creator_w = tkinter.Button(self.your_hand_frame,text = "Wild", \
                                bg = "black", fg = "#D5BBE2",font ="Times 20 bold",height=4,width=4, \
                                            command =self.input_wild)
            self.your_hand_card_creator_w.pack(side="left")
            self.copy_check_for_removal_later(element)
            self.delete_list.append(self.your_hand_card_creator_w)
            self.input_wild()

    # determining if the user move was valid
    def user_chosen_card(self,user_card_num_chosen,user_card_color_chosen,user_card_chosen):

        print("YoUR HAND:",self.your_hand)

        if self.validator == 0:
            if (user_card_color_chosen == self.top_card_color) or (user_card_num_chosen == self.top_card_num) or ("wild" in user_card_chosen):

                self.bot_pass_checker = 0
                self.random_hints()
                self.pass_counter = 0
                self.draw_display_var.set("Draw")

                self.counter_for = 0
                
                self.top_card_color = user_card_color_chosen
                self.top_card_num = user_card_num_chosen
                self.top_card = user_card_chosen

                self.your_hand_count -= 1

                self.your_hand.remove(user_card_chosen)
                
                self.top_card_color_display_var.set(self.top_card_color)
                self.top_card_num_display_var.set(self.top_card_num)
                self.discard_pile_card.after(100)

                self.displaying_cards_colors_and_num_your_hand()
                self.create_discard_pile()

                if user_card_num_chosen == "⟲" or user_card_num_chosen == "skip":
                    self.winner_checker()
                    self.displaying_cards_colors_and_num_your_hand()
                    
                elif user_card_num_chosen == "+2":
                    for i in range(2):
                        new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                        self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                        self.uno_full_deck.remove(self.new_added_card)
                        self.enemy_hand.append(self.new_added_card)
                        self.enemy_hand_count += 1
                        self.user_block_counter = 0
                    self.displaying_cards_colors_and_num_your_hand()
                    self.checking_if_bot_gained_cards_after_uno()

                elif user_card_num_chosen == "wild":
                    self.validator = 1
                                                     
                    self.red_choice = tkinter.Button(self.main_window,text="RED",fg="#D5BBE2",bg="red",font="Times 26 bold",command=self.red_chosen)
                    self.blue_choice = tkinter.Button(self.main_window,text="BLUE",fg="#D5BBE2",bg="blue",font="Times 26 bold",command=self.blue_chosen)
                    self.green_choice = tkinter.Button(self.main_window,text="GREEN",fg="#D5BBE2",bg="green",font="Times 26 bold",command=self.green_chosen)
                    self.yellow_choice = tkinter.Button(self.main_window,text="YELLOW",fg="#D5BBE2",bg="yellow",font="Times 26 bold",command=self.yellow_chosen)
                    self.choose_color = tkinter.Label(self.main_window,text="Choose A Color To Switch To!", fg="white", bg="#FF6F27", font = "Impact 30 bold")

                    self.red_choice.place(x=1000,y=110,width=160,height=80)
                    self.blue_choice.place(x=1170,y=110,width=160,height=80)
                    self.green_choice.place(x=1000,y=200,width=160,height=80)
                    self.yellow_choice.place(x=1170,y=200,width=160,height=80)
                    self.choose_color.place(x=965,y=285,width=400,height=40)
                    
                if user_card_num_chosen == "+4":
                    self.checking_if_bot_gained_cards_after_uno()
                    self.user_block_counter = 0
                    bot_challenge_decider = 0
                    bot_challenge_decider = random.randint(1,3)
                    if bot_challenge_decider == 2:
                        self.bot_challenge_user()
                    else:
                        for i in range(4):
                            new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                            self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                            self.uno_full_deck.remove(self.new_added_card)
                            self.enemy_hand.append(self.new_added_card)
                            self.enemy_hand_count += 1
                            self.enemy_successful_uno_count = 0
                        self.bot_delete_hand = 0
                        self.displaying_cards_colors_and_num_enemy_hand()
                  
                        self.validator = 1

                        self.red_choice = tkinter.Button(self.main_window,text="RED",fg="#D5BBE2",bg="red",font="Times 26 bold",command=self.red_chosen)
                        self.blue_choice = tkinter.Button(self.main_window,text="BLUE",fg="#D5BBE2",bg="blue",font="Times 26 bold",command=self.blue_chosen)
                        self.green_choice = tkinter.Button(self.main_window,text="GREEN",fg="#D5BBE2",bg="green",font="Times 26 bold",command=self.green_chosen)
                        self.yellow_choice = tkinter.Button(self.main_window,text="YELLOW",fg="#D5BBE2",bg="yellow",font="Times 26 bold",command=self.yellow_chosen)
                        self.choose_color = tkinter.Label(self.main_window,text="Choose A Color To Switch Too!", fg="white", bg="#FF6F27", font = "Impact 30 bold")

                        self.red_choice.place(x=1000,y=110,width=160,height=80)
                        self.blue_choice.place(x=1170,y=110,width=160,height=80)
                        self.green_choice.place(x=1000,y=200,width=160,height=80)
                        self.yellow_choice.place(x=1170,y=200,width=160,height=80)
                        self.choose_color.place(x=965,y=285,width=400,height=40)
                    
                if self.your_hand_count == 0 and self.your_successful_uno_count != 1:
                    self.uno_display_var.set("You forgot to call UNO!")
                    
                    for new_cards in range(2):
                        new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                        self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                        self.uno_full_deck.remove(self.new_added_card)
                        self.your_hand.append(self.new_added_card)
                        self.your_hand_count += 1
                    self.displaying_cards_colors_and_num_your_hand()

                    self.winner_checker()

                if self.repeat == True and self.validator == 0 and (user_card_num_chosen != "skip" and user_card_num_chosen != "⟲"):

                    if self.destroy_button_checker == True:
                        self.challenge_validator.destroy()
                        self.destroy_button_checker = False
        
                    self.bot_pass_checker = 0
                    self.bot_choice()
            else:
                self.helper_display_var.set("Play same color, number, or wild!")

    # determining if the bot can challenge user
    def bot_challenge_user(self):
        
        for_loop_challenge_counter = 0
        card_num_creator_checker = ""
        card_color_creator_checker = ""
        
        for element in self.your_hand:

            if "zero" in element:
                card_num_creator_checker = "0"
            if "one" in element:
                card_num_creator_checker = "1"
            if "two" in element:
                card_num_creator_checker = "2"
            if "three" in element:
                card_num_creator_checker = "3"
            if "four" in element:
                card_num_creator_checker = "4"
            if "five" in element:
                card_num_creator_checker = "5"
            if "six" in element:
                card_num_creator_checker = "6"
            if "seven" in element:
                card_num_creator_checker = "7"
            if "eight" in element:
                card_num_creator_checker = "8"
            if "nine" in element:
                card_num_creator_checker = "9"

            if "red" in element:
                card_color_creator_checker = "red"
            if "blue" in element:
                card_color_creator_checker = "blue"
            if "green" in element:
                card_color_creator_checker = "green"
            if "yellow" in element:
                card_color_creator_checker = "yellow"
                
            if "wild_plus_four" in element:
                card_color_creator_checker = "black"
                card_num_creator_checker = "+4"
            elif "wild" in element:
                card_color_creator_checker = "black"
                card_num_creator_checker = "Wild"
                
            if "plus_2" in element:
                card_num_creator_checker = "+2"
            elif "reverse" in element:
                card_num_creator_checker = "⟲"
            elif "skip" in element:
                card_num_creator_checker = "Skip"

            if card_color_creator_checker == self.top_card_color:
                for_loop_challenge_counter = 1

        if for_loop_challenge_counter == 1:
            self.challenge_validator = tkinter.Label(self.main_window,text="USER BLOCKED!",bg="red",fg="white",font = "Impact 20 bold")
            self.challenge_validator.place(x=750,y=168,width=200,height=100)

            self.destroy_button_checker = True
            for cards in range(4):
                new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                self.uno_full_deck.remove(self.new_added_card)
                self.your_hand.append(self.new_added_card)
                self.your_hand_count += 1
                self.displaying_cards_colors_and_num_your_hand()
             
        elif for_loop_challenge_counter == 1:
            self.challenge_validator = tkinter.Label(self.main_window,text="USER SAFE!",bg="red",fg="white",font = "Impact 30 bold")
            self.challenge_validator.place(x=750,y=168,width=200,height=100)

            self.destroy_button_checker = True
            for cards in range(6):
                new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                self.uno_full_deck.remove(self.new_added_card)
                self.enemy_hand.append(self.new_added_card)
                self.enemy_hand_count += 1
                self.displaying_cards_colors_and_num_enemy_hand()

    # creating discard pile
    def create_discard_pile(self):

        if self.counter_discard == 0:
            self.discard_pile_card.destroy()
            self.blank_space_for_formatting1.destroy()
            self.blank_space_for_formatting2.destroy()

        print("top color?:",self.top_card_color_display_var.get())
        
        self.discard_pile_card = tkinter.Label(self.discard_pile_frame,textvariable = self.top_card_num_display_var, \
                                    bg = self.top_card_color_display_var.get(), fg = "#D5BBE2", font ="Times 20 bold",height=4,width=7)
        self.blank_space_for_formatting1 = tkinter.Label(self.discard_pile_frame,text="",height=4,bg="#FF6F27")
        self.blank_space_for_formatting2 = tkinter.Label(self.discard_pile_frame,text="",height=4,bg="#FF6F27")

        self.blank_space_for_formatting1.pack()
        self.discard_pile_card.pack()
        self.blank_space_for_formatting2.pack()

        self.counter_discard = 0

    # creating the function that the bot can use
    def bot_choice(self):

        self.helper_display_var.set("")
        print("\nBOT HAND:",self.enemy_hand)
        print()

        if self.challenge_checking == 10:
            self.challenge_button.destroy()
            self.displaying_cards_colors_and_num_enemy_hand()

        if self.enemy_hand_count == 1 and self.enemy_successful_uno_count == 0:
            self.bot_has_called_uno()

        self.bot_num_checker = 0
        for element in self.enemy_hand:
            if "zero" in element:
                self.bot_card_num = "0"
            if "one" in element:
                self.bot_card_num = "1"
            elif "two" in element:
                self.bot_card_num = "2"
            elif "three" in element:
                self.bot_card_num = "3"
            elif "four" in element:
                self.bot_card_num = "4"
            elif "five" in element:
                self.bot_card_num = "5"
            elif "six" in element:
                self.bot_card_num = "6"
            elif "seven" in element:
                self.bot_card_num = "7"
            elif "eight" in element:
                self.bot_card_num = "8"
            elif "nine" in element:
                self.bot_card_num = "9"
            elif "plus_2" in element:
                self.bot_card_num = "+2"
            elif "reverse" in element:
                self.bot_card_num = "⟲"
            elif "skip" in element:
                self.bot_card_num = "skip"
            elif "wild_plus_four" in element:
                self.bot_card_num = "+4"
                self.bot_card_color = "black"
            elif "wild" in element:
                self.bot_card_num = "wild"
                self.bot_card_color = "black"

            if "red" in element:
                self.bot_card_color = "red"
            elif "blue" in element:
                self.bot_card_color = "blue"
            elif "green" in element:
                self.bot_card_color = "green"
            elif "yellow" in element:
                self.bot_card_color = "yellow"
                
            if self.bot_num_checker == 0:
                self.displaying_and_changing_info_after_bot_turn(element)

        if self.bot_num_checker == 0 and self.bot_pass_checker == 0:
            self.user_block_counter = 0
            self.bot_pass_choice()

            self.winner_checker()
            
        if self.repeat == True:
            self.displaying_cards_colors_and_num_your_hand()

    # creating the function if valid move from bot
    def displaying_and_changing_info_after_bot_turn(self,element_taken):
        if (self.bot_card_color == self.top_card_color) or (self.bot_card_num == self.top_card_num) or ("wild" in element_taken):

            wild_randomizer_num = 0

            wild_randomizer_num = random.randint(1,3)
            if self.enemy_hand_count == 1 and ("wild_plus_four" in element_taken):
                wild_randomizer_choice = 1
            elif wild_randomizer_num == 1 or wild_randomizer_num == 2:
                self.wild_randomizer_choice = 1
            else:
                self.wild_randomizer_choice = 0
            
            self.bot_num_checker = 1
            self.bot_delete_hand = 0

            if self.bot_card_num == "wild" or "+4":
                self.bot_card_color == "black"
                
            self.top_card_color = self.bot_card_color
            self.top_card_num = self.bot_card_num
            self.top_card = element_taken

            self.enemy_hand_count -= 1
            self.enemy_hand.remove(element_taken)
            
            self.discard_pile_card.after(200)
            self.top_card_color_display_var.set(self.top_card_color)
            self.top_card_num_display_var.set(self.top_card_num)
            self.discard_pile_card.after(400)

            print("\nTop color:",self.top_card_color,"        Top num:",self.top_card_num,"         Top Card:",self.top_card)
            print()

            self.displaying_cards_colors_and_num_enemy_hand()
            self.create_discard_pile()

            if self.bot_card_num == "⟲" or self.bot_card_num == "skip":
                self.winner_checker()
                self.bot_pass_checker = 0
                self.bot_choice()
                
            elif self.bot_card_num == "+2":
                for i in range(2):
                    new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                    self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                    self.uno_full_deck.remove(self.new_added_card)
                    self.your_hand.append(self.new_added_card)
                    self.your_hand_count += 1
                self.displaying_cards_colors_and_num_your_hand()

            elif self.bot_card_num == "wild":
                if "red" in self.enemy_hand[0]:
                    self.bot_card_color = "red"
                elif "blue" in self.enemy_hand[0]:
                    self.bot_card_color = "blue"
                elif "yellow" in self.enemy_hand[0]:
                    self.bot_card_color = "yellow"
                elif "green" in self.enemy_hand[0]:
                    self.bot_card_color = "green"
                self.top_card_color = self.bot_card_color

                self.top_card_color_display_var.set(self.bot_card_color)
                self.create_discard_pile()
                
            if self.bot_card_num == "+4" and self.wild_randomizer_choice == 1:
                self.enemy_plus_4 = True
                for i in range(4):
                    new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                    self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                    self.uno_full_deck.remove(self.new_added_card)
                    self.your_hand.append(self.new_added_card)
                    self.your_hand_count += 1
                self.displaying_cards_colors_and_num_your_hand()
                
                if "red" in self.enemy_hand[0]:
                    self.bot_card_color = "red"
                elif "blue" in self.enemy_hand[0]:
                    self.bot_card_color = "blue"
                elif "yellow" in self.enemy_hand[0]:
                    self.bot_card_color = "yellow"
                elif "green" in self.enemy_hand[0]:
                    self.bot_card_color = "green"
                self.top_card_color = self.bot_card_color
                self.top_card_color_display_var.set(self.bot_card_color)
                self.create_discard_pile()

        if self.enemy_hand_count == 0 and self.enemy_successful_uno_count == 0:
            self.uno_display_var.set("Opponent forgot to call UNO!")
            for new_cards in range(2):
                new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                self.uno_full_deck.remove(self.new_added_card)
                self.enemy_hand.append(self.new_added_card)
                self.enemy_hand_count += 1
                self.enemy_successful_uno_count = 0
            self.displaying_cards_colors_and_num_enemy_hand()

        self.winner_checker()

    # if you challenge the cards from bot        
    def challenged_wild_plus_four_card(self):

        self.challenge_button.destroy()
        for card in self.bot_delete_list:
            card.destroy()
        for space in self.bot_blank_space_list:
            space.destroy()
        
        for_loop_challenge_counter = 0
        bot_card_num_creator_checker = ""
        bot_card_color_creator_checker = ""
        self.challenge_checking = 10
        
        for element in self.enemy_hand:

            if "zero" in element:
                bot_card_num_creator_checker = "0"
            if "one" in element:
                bot_card_num_creator_checker = "1"
            if "two" in element:
                bot_card_num_creator_checker = "2"
            if "three" in element:
                bot_card_num_creator_checker = "3"
            if "four" in element:
                bot_card_num_creator_checker = "4"
            if "five" in element:
                bot_card_num_creator_checker = "5"
            if "six" in element:
                bot_card_num_creator_checker = "6"
            if "seven" in element:
                bot_card_num_creator_checker = "7"
            if "eight" in element:
                bot_card_num_creator_checker = "8"
            if "nine" in element:
                bot_card_num_creator_checker = "9"

            if "red" in element:
                bot_card_color_creator_checker = "red"
            if "blue" in element:
                bot_card_color_creator_checker = "blue"
            if "green" in element:
                bot_card_color_creator_checker = "green"
            if "yellow" in element:
                bot_card_color_creator_checker = "yellow"
                
            if "wild_plus_four" in element:
                bot_card_color_creator_checker = "black"
                bot_card_num_creator_checker = "+4"
            elif "wild" in element:
                bot_card_color_creator_checker = "black"
                bot_card_num_creator_checker = "Wild"
                
            if "plus_2" in element:
                bot_card_num_creator_checker = "+2"
            elif "reverse" in element:
                bot_card_num_creator_checker = "⟲"
            elif "skip" in element:
                bot_card_num_creator_checker = "Skip"

            if bot_card_num_creator_checker == "⟲":
                bot_enemy_hand_card_creator = tkinter.Label(self.enemy_hand_frame,text = bot_card_num_creator_checker, \
                                bg = bot_card_color_creator_checker, fg = "#D5BBE2",font ="Times 26 bold",height=3,width=4)
                self.bot_blank_space = tkinter.Label(self.enemy_hand_frame,text="",bg="#FF6F27")
                
            else:
                bot_enemy_hand_card_creator = tkinter.Label(self.enemy_hand_frame,text = bot_card_num_creator_checker, \
                                    bg = bot_card_color_creator_checker, fg = "#D5BBE2",font ="Times 20 bold",height=4,width=5)
                self.bot_blank_space = tkinter.Label(self.enemy_hand_frame,text="",bg="#FF6F27")

            self.bot_blank_space_list.append(self.bot_blank_space)
                
            if bot_card_color_creator_checker == self.top_card_color:
                for_loop_challenge_counter = 1

            self.enemy_hand_card_creator.pack(side="left")
            self.blank_space.pack(side="left")

        if for_loop_challenge_counter == 0:
            self.challenge_validator = tkinter.Label(self.main_window,text="Fail!",bg="red",fg="white",font = "Impact 30 bold")
            self.challenge_validator.place(x=750,y=168,width=200,height=100)

            for cards in range(6):
                new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                self.uno_full_deck.remove(self.new_added_card)
                self.your_hand.append(self.new_added_card)
                self.your_hand_count += 1
                self.displaying_cards_colors_and_num_your_hand()
             
        elif for_loop_challenge_counter == 1:
            self.challenge_validator = tkinter.Label(self.main_window,text="Success!",bg="red",fg="white",font = "Impact 30 bold")
            self.challenge_validator.place(x=750,y=168,width=200,height=100)
            
            for cards in range(4):
                new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
                self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
                self.uno_full_deck.remove(self.new_added_card)
                self.enemy_hand.append(self.new_added_card)
                self.enemy_hand_count += 1
                self.displaying_cards_colors_and_num_enemy_hand()

    # displaying cards in bot hand
    def displaying_cards_colors_and_num_enemy_hand(self):

        if self.bot_delete_hand == 0:
            for element in self.bot_delete_list:
                element.destroy()
            for space in self.bot_blank_space_list:
                space.destroy()
                
        for element in self.enemy_hand:
            self.enemy_hand_card_creator = tkinter.Label(self.enemy_hand_frame,text = "UNO", \
                                bg = "black", fg = "white",font = "Times 20 bold",height=4,width=7)

            self.bot_delete_list.append(self.enemy_hand_card_creator)
            
            self.bot_blank_space = tkinter.Label(self.enemy_hand_frame,text="",bg="#FF6F27")

            self.bot_blank_space_list.append(self.bot_blank_space)
            self.enemy_hand_card_creator.pack(side="left")
            self.bot_blank_space.pack(side="left")

    # shuffling deck
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

    # choose top card
    def top_card_chooser(self):

        top_card_num_chooser = 0
        top_card_num_chooser = random.randint(0,len(self.uno_full_deck) - 1)
        self.top_card = self.uno_full_deck[top_card_num_chooser]
        
        while ("plus" in self.top_card) or ("reverse" in self.top_card) or ("wild" in self.top_card) or ("skip" in self.top_card):
            top_card_num_chooser = random.randint(0,len(self.uno_full_deck) - 1)
            self.top_card = self.uno_full_deck[top_card_num_chooser]

        if "red" in self.top_card:
            self.top_card_color = "red"
        elif "blue" in self.top_card:
            self.top_card_color = "blue"
        elif "yellow" in self.top_card:
            self.top_card_color = "yellow"
        elif "green" in self.top_card:
            self.top_card_color = "green"

        if "zero" in self.top_card:
            self.top_card_num = "0"
        elif "one" in self.top_card:
            self.top_card_num = "1"
        elif "two" in self.top_card:
            self.top_card_num = "2"
        elif "three" in self.top_card:
            self.top_card_num = "3"
        elif "four" in self.top_card:
            self.top_card_num = "4"
        elif "five" in self.top_card:
            self.top_card_num = "5"
        elif "six" in self.top_card:
            self.top_card_num = "6"
        elif "seven" in self.top_card:
            self.top_card_num = "7"
        elif "eight" in self.top_card:
            self.top_card_num = "8"
        elif "nine" in self.top_card:
            self.top_card_num = "9"

        self.top_card_color_display_var.set(self.top_card_color)
        self.top_card_num_display_var.set(self.top_card_num)

    # passing and drawing card, defining the function with 1 paramater
    def pass_choice(self):
        if self.pass_counter == 0 and self.validator == 0 and self.your_hand_count < 16:
            new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
            self.new_added_card = self.uno_full_deck[new_card_added_to_hand]
            self.uno_full_deck.remove(self.new_added_card)
            self.your_hand.append(self.new_added_card)
            self.your_hand_count += 1
            self.your_successful_uno_count = 0
            self.uno_display_var.set("")
            self.pass_counter = 1
            self.counter_for = 0
            self.bot_pass_checker = 0
            self.draw_display_var.set("End")
            self.displaying_cards_colors_and_num_your_hand()
        elif self.pass_counter == 1 and self.validator == 0:
            self.pass_counter = 0
            self.bot_pass_checker = 0  
            self.draw_display_var.set("Draw")
            self.bot_choice()

        else:
            self.helper_display_var.set("Please play a valid card")

    # funtion with 1 paramter is used when the bot has no valid cards and decides to pass
    def bot_pass_choice(self):
        bot_new_card_added_to_hand = random.randint(0,len(self.uno_full_deck) - 1)
        self.bot_new_added_card = self.uno_full_deck[bot_new_card_added_to_hand]
        self.uno_full_deck.remove(self.bot_new_added_card)
        self.enemy_hand.append(self.bot_new_added_card)
        self.enemy_hand_count += 1
        self.enemy_successful_uno_count = 0
        self.displaying_cards_colors_and_num_enemy_hand()
        self.bot_pass_checker = 1
        self.checking_if_bot_gained_cards_after_uno()
        self.bot_choice()

    # function called when the red card is chosen from wild card
    def red_chosen(self):
        self.top_card_color = "red"
        self.top_card_color_display_var.set(self.top_card_color)
        self.validator = 0
        self.create_discard_pile()
        self.destroy_wild_buttons()
        self.bot_choice()

    # function called when te blue card is chosen from wild card
    def blue_chosen(self):
        self.top_card_color = "blue"
        self.top_card_color_display_var.set(self.top_card_color)
        self.validator = 0
        self.create_discard_pile()
        self.destroy_wild_buttons()
        self.bot_choice()

    # function chosen when green card is chosen from wild card
    def green_chosen(self):
        self.top_card_color = "green"
        self.top_card_color_display_var.set(self.top_card_color)
        self.validator = 0
        self.create_discard_pile()
        self.destroy_wild_buttons()
        self.bot_choice()

    # function chosen when yellow card is chosen from wild card
    def yellow_chosen(self):
        self.top_card_color = "yellow"
        self.top_card_color_display_var.set(self.top_card_color)
        self.validator = 0
        self.create_discard_pile()
        self.destroy_wild_buttons()
        self.bot_choice()

    # random hints deciding function
    def random_hints(self):
        random_hint_choice = 0
        random_hint_choice = random.randint(1,5)

        if random_hint_choice == 1:
            self.helper_display_var.set("Play cards of same color, number, or wild")
        elif random_hint_choice == 2:
            self.helper_display_var.set("Draw a card if no playable cards!")
        elif random_hint_choice == 3:
            self.helper_display_var.set("Play a skip or reverse card to play instantly!")
        elif random_hint_choice == 4:
            self.helper_display_var.set("Make sure to call UNO when having one card!")
        elif random_hint_choice == 5:
            self.helper_display_var.set("Call block when your opponent is at one card!")

    # destorying wild button
    def destroy_wild_buttons(self):
        self.red_choice.destroy()
        self.blue_choice.destroy()
        self.green_choice.destroy()
        self.yellow_choice.destroy()
        self.choose_color.destroy()

    def checking_if_bot_gained_cards_after_uno(self):
        if self.uno_display_var.get == "The opponent has called UNO":
            self.uno_display_var.set(" ")
        
UNO_card_game = MyUNO()
