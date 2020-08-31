import pygame
import random
import time

class Card(object):
    numb_direct = {
        # an ace can be either 1 or 11
        "Ace" : 11,
        "Two" : 2,
        "Three" : 3,
        "Four" : 4,
        "Five" : 5,
        "Six" : 6,
        "Seven" : 7,
        "Eight" : 8,
        "Nine" : 9,
        "Ten" : 10,
        "Jack" : 10,
        "Queen" : 10,
        "King" : 10,
    }


    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
        self.number_val()

    def show(self):
        print(f"{self.val} of {self.suit}")

    def number_val(self):
        self.numb = Card.numb_direct.get(self.val)

    def call_numb_val(self):
        return self.numb


#Creates a many_decks number of decks of cards, 4 suites, 13 cards per suite, ranging from ace to king.
class Deck(object):

    def __init__(self):
        self.cards = []
        self.build()

    #Automatically called when an instance is initiated.
    def build(self):
        all_suits = ["spade", "club", "diamond", "heart"]
        all_val = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        for i in range(1, 7): #makes 6
            for s in all_suits:
                for v in all_val:
                    self.cards.append(Card(s, v))
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        #Starts at the furthest number and stops at zero, and iterates by -1 each time.
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            # Swap elements by index in a list. use list[index] to access the element
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()



class Player(object):
    def __init__(self):
        self.hand = []
        self.hand_score = 0

    def draw(self, deck):
        self.hand.append(deck.drawCard())
    
    
    def addCards(self):
        total = 0
        for card in self.hand:
            total += card.call_numb_val()
            #print(card.call_numb_val())
        self.hand_score = total

    def clear_hand(self):
        self.hand = []
        
class Dealer(object):
    def __init__(self):
        self.hand = []
        self.hand_score = 0
    
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()
    
    def addCards(self):
        total = 0
        for card in self.hand:
            total += card.call_numb_val()
            #print(card.call_numb_val())
        self.hand_score = total
    
    def clear_hand(self):
        self.hand = []


#  class PlayHand(object):
    #     score_board = {
    #         "player" : 0,
    #         "dealer" : 0
    #     }

    #     def __init__(self):
    #         self.deck = Deck()
    #         self.player = Player()
    #         self.dealer = Dealer()
    #         self.play()

    #     def play(self):
    #         self.player.clear_hand()
    #         self.dealer.clear_hand()
    #         self.deck.shuffle()
    #         #self.deck.show()
    #         #deal to player then dealer from the top of the deck, iterates twice. If modulus is 0 then it deals to player, if not, then it deals to the dealer
    #         for i in range(0,4):
    #             if i % 2 == 0:
    #                 self.player.draw(self.deck)
    #             else:
    #                 self.dealer.draw(self.deck)

    #         self.player.showHand()
    #         self.player.addCards()
    #         self.dealer.showTopCard()


    #     def playerChoice(self):
    #         if pygame.KEYDOWN == K_h:
    #             self.player.draw(self.deck)
    #             self.player.addCards()
    #             if self.player.hand_score > 21:
    #                 self.dealerwins()
    #             return "hit"
    #         elif pygame.KEYDOWN == K_s:
    #             self.dealerChoice()
    #             return "stay"

        
    #     def dealerChoice(self):
    #         self.dealer.showHand()
    #         self.dealer.addCards()
    #         dealer_choice = ""
    #         while dealer_choice != "stay":
    #             if self.dealer.hand_score < 17:
    #                 self.dealer.draw(self.deck)
    #                 self.dealer.addCards()
    #                 if self.dealer.hand_score > 21:
    #                     self.playerwins()
    #                 dealer_choice = "hit"
    #             elif self.dealer.hand_score >= 17:
    #                 dealer_choice = "stay"
    #         self.decide_who_wins()

        # def decide_who_wins(self):
        #     if self.dealer.hand_score > self.player.hand_score:
        #         self.dealerwins()
        #     elif self.dealer.hand_score < self.player.hand_score:
        #         self.playerwins()
            # else:
            #     print("The hand is pushed.\n\n")
            #     dec = input("Play again?\n\n> ")
            #     if dec == "yes":
            #         self.play()
            #     if dec == "no":
            #         exit(0)

        # def playerwins(self):
        #     PlayHand.score_board["player"] += 1


        # def dealerwins(self):
        #     PlayHand.score_board["dealer"] += 1


        # def prn_score(self):
        #     player_score = PlayHand.score_board.get("player")
        #     dealer_score = PlayHand.score_board.get("dealer")
        #     total_hands = player_score + dealer_score
        #     time.sleep(3)
        #     print(f"\n\nAfter {total_hands} hands the score is:")
        #     print(f"{self.player_name} has won {player_score} hands")
        #     print(f"The Dealer has won {dealer_score} hands")
        #     time.sleep(2)
        #     print("\n\nWould you like to play another hand?")
        #     resp = input("> ")
        #     if resp == "yes":
        #         self.play()
        #     if resp == "no":
        #         exit(0)

class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.should_show = False

class Show_Cards(Block):
    pass


def main():
    # choice variable
    who_is_choosing = "player"

    width = 400
    height = 400
    green_color = (0, 180, 0 )

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pete\'s Poker Place')
    clock = pygame.time.Clock()

    # create the rectangle for the bar down on the bottom
    ribbon = pygame.Rect(0, 340, 400, 80)
    ribbon_color = (100, 100, 100)

    # makes our deck, user and dealer objects
    main_deck = Deck()
    user = Player()
    dealer = Dealer()

    # main_deck.show()
    # shuffles the deck
    main_deck.shuffle()
    # main_deck.show()

    # now we deal the cards
    for i in range(0,4):
        if i % 2 == 0:
            user.draw(main_deck)
        else:
            dealer.draw(main_deck)

    for card in dealer.hand:
        card.show()

    for card in user.hand:
        card.show()
    

    # print(f'{user.hand[1].suit} of {user.hand[1].call_numb_val()}')
    # print(dealer.hand)

    # houses the pictures for the two decks
    deck = pygame.image.load('images/face_down.png').convert_alpha()

    
    # user cards
    player_card_1 = pygame.image.load(f'images/{user.hand[0].suit}_{user.hand[0].val}.svg.png').convert_alpha()
    player_card_2 = pygame.image.load(f'images/{user.hand[1].suit}_{user.hand[1].val}.svg.png').convert_alpha()
    # once the user has more than two cards, we add more pictures
    if len(user.hand) == 3:
        player_card_3 = pygame.image.load(f'images/{user.hand[2].suit}_{user.hand[2].val}.svg.png').convert_alpha()
    elif len(user.hand) == 4:
        player_card_4 = pygame.image.load(f'images/{user.hand[3].suit}_{user.hand[3].val}.svg.png').convert_alpha()
    elif len(user.hand) == 5:
        player_card_5 = pygame.image.load(f'images/{user.hand[4].suit}_{user.hand[4].val}.svg.png').convert_alpha()
    elif len(user.hand) == 6:
        player_card_6 = pygame.image.load(f'images/{user.hand[5].suit}_{user.hand[5].val}.svg.png').convert_alpha()

    # dealer cards
    dealer_card_1 = pygame.image.load(f'images/{dealer.hand[0].suit}_{dealer.hand[0].val}.svg.png').convert_alpha()
    if who_is_choosing == "player":
        dealer_card_2 = pygame.image.load('images/face_down.png').convert_alpha()
    else:
        dealer_card_2 = pygame.image.load(f'images/{dealer.hand[1].suit}_{dealer.hand[1].val}.svg.png').convert_alpha()
    if len(dealer.hand) == 3:
        player_card_3 = pygame.image.load(f'images/{dealer.hand[2].suit}_{dealer.hand[2].val}.svg.png').convert_alpha()
    elif len(dealer.hand) == 4:
        player_card_4 = pygame.image.load(f'images/{dealer.hand[3].suit}_{dealer.hand[3].val}.svg.png').convert_alpha()
    elif len(dealer.hand) == 5:
        player_card_5 = pygame.image.load(f'images/{dealer.hand[4].suit}_{dealer.hand[4].val}.svg.png').convert_alpha()
    elif len(dealer.hand) == 6:
        player_card_6 = pygame.image.load(f'images/{dealer.hand[5].suit}_{dealer.hand[5].val}.svg.png').convert_alpha()


    # the two decks for shuffling
    deck_1 = Show_Cards(deck, [180, 200])
    deck_2 = Show_Cards(deck, [220, 200])
    deck_group = pygame.sprite.Group()
    deck_group.add(deck_1, deck_2)

    # The showing the dealers top card and hiding his second card after
    # the he has finishing shuffling all the decks
    dealer_1 = Show_Cards(dealer_card_1, [180, 100])
    dealer_2 = Show_Cards(dealer_card_2, [220, 100])
    
    dealer_card_group = pygame.sprite.Group()
    dealer_card_group.add(dealer_1, dealer_2)

    # Showing both of the players cards face up
    player_1 = Show_Cards(player_card_1, [180, 300])
    player_2 = Show_Cards(player_card_2, [220, 300])
    player_card_group = pygame.sprite.Group()
    player_card_group.add(player_1, player_2)

    
    # Game initialization
    stop_game = False


    while not stop_game:
        # looks at every event in the queue
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True

            # checks if a key was entered
            if event.type == pygame.KEYDOWN:
                # if the Esc key is pressed, then exit the main loop
                if event.key == pygame.K_ESCAPE:
                    stop_game = True

                # if the y key is pressed, then we add a card to our user hand
                if event.key == pygame.K_LEFT:
                    # print these only after we have shuffled
                    for card in player_card_group:
                        card.should_show = True
                    for card in dealer_card_group:
                        card.should_show = True
                    # screen.blit(player_card_group, [250, 250])
                    pygame.display.update()

                # if the h key is pressed, then we know that the user wants another card
                if event.key == pygame.K_h and who_is_choosing == "player":
                    user.addCards()
                    if user.hand_score < 21:
                        user.draw(main_deck)

                    if len(user.hand) == 3:
                        player_card_3 = pygame.image.load(f'images/{user.hand[2].suit}_{user.hand[2].val}.svg.png').convert_alpha()
                        player_3 = Show_Cards(player_card_3, [260, 300])
                        player_3.should_show = True
                        player_card_group = pygame.sprite.Group()
                        player_card_group.add(player_1, player_2, player_3)
                        for card in player_card_group:
                            if card.should_show:
                                screen.blit(card.image, card.rect)
                    elif len(user.hand) == 4:
                        player_card_4 = pygame.image.load(f'images/{user.hand[3].suit}_{user.hand[3].val}.svg.png').convert_alpha()
                        player_4 = Show_Cards(player_card_4, [300, 300])
                        player_4.should_show = True
                        player_card_group = pygame.sprite.Group()
                        player_card_group.add(player_1, player_2, player_3, player_4)
                        for card in player_card_group:
                            if card.should_show:
                                screen.blit(card.image, card.rect)
                    elif len(user.hand) == 5:
                        player_card_5 = pygame.image.load(f'images/{user.hand[4].suit}_{user.hand[4].val}.svg.png').convert_alpha()
                        player_5 = Show_Cards(player_card_5, [340, 300])
                        player_5.should_show = True
                        player_card_group = pygame.sprite.Group()
                        player_card_group.add(player_1, player_2, player_3, player_4, player_5)
                        for card in player_card_group:
                            if card.should_show:
                                screen.blit(card.image, card.rect)
                    elif len(user.hand) == 6:
                        player_card_6 = pygame.image.load(f'images/{user.hand[5].suit}_{user.hand[5].val}.svg.png').convert_alpha()
                        player_6 = Show_Cards(player_card_6, [340, 300])
                        player_6.should_show = True
                        player_card_group = pygame.sprite.Group()
                        player_card_group.add(player_1, player_2, player_3, player_4, player_5, player_6)
                        for card in player_card_group:
                            if card.should_show:
                                screen.blit(card.image, card.rect)
                
                # if the s key is pressed, then we know that the user no longer wants any more cards
                if event.key == pygame.K_s:
                    who_is_choosing = "dealer" 
                    dealer.addCards()
                    dealer.draw(main_deck)
                    dealer_card_2 = pygame.image.load(f'images/{dealer.hand[1].suit}_{dealer.hand[1].val}.svg.png').convert_alpha()
                    dealer_2 = Show_Cards(dealer_card_2, [220, 100])
                    dealer_2.should_show = True
                    dealer_card_group = pygame.sprite.Group()
                    dealer_card_group.add(dealer_1, dealer_2)
                    for card in dealer_card_group:
                        if card.should_show:
                            screen.blit(card.image, card.rect)
                            pygame.display.update()
                    if dealer.hand_score < 17:
                        dealer.draw(main_deck)
                        dealer.addCards()
                        dealer_card_3 = pygame.image.load(f'images/{dealer.hand[2].suit}_{dealer.hand[2].val}.svg.png').convert_alpha()
                        dealer_3 = Show_Cards(dealer_card_3, [260, 100])
                        dealer_3.should_show = True
                        dealer_card_group = pygame.sprite.Group()
                        dealer_card_group.add(dealer_1, dealer_2, dealer_3)
                        time.sleep(3)
                        for card in dealer_card_group:
                            if card.should_show:
                                screen.blit(card.image, card.rect)
                                pygame.display.update()
                    if dealer.hand_score < 17:
                        dealer.draw(main_deck)
                        dealer.addCards()
                        dealer_card_4 = pygame.image.load(f'images/{dealer.hand[3].suit}_{dealer.hand[3].val}.svg.png').convert_alpha()
                        dealer_4 = Show_Cards(dealer_card_4, [300, 100])
                        dealer_4.should_show = True
                        dealer_card_group = pygame.sprite.Group()
                        dealer_card_group.add(dealer_1, dealer_2, dealer_3, dealer_4)
                        time.sleep(3)
                        for card in dealer_card_group:
                            if card.should_show:
                                screen.blit(card.image, card.rect)
                                pygame.display.update()
                    if dealer.hand_score < 17:
                        dealer.draw(main_deck)
                        dealer.addCards()
                        dealer_card_5 = pygame.image.load(f'images/{dealer.hand[4].suit}_{dealer.hand[4].val}.svg.png').convert_alpha()
                        dealer_5 = Show_Cards(dealer_card_5, [300, 100])
                        dealer_5.should_show = True
                        dealer_card_group = pygame.sprite.Group()
                        dealer_card_group.add(dealer_1, dealer_2, dealer_3, dealer_4, dealer_5)
                        time.sleep(3)
                        for card in dealer_card_group:
                            if card.should_show:
                                screen.blit(card.image, card.rect)
                                pygame.display.update()

                    
                if event.key == pygame.K_r:
                    dealer.clear_hand()
                    user.clear_hand()
                    main()
        # gets all the keys currently pressed
        keys = pygame.key.get_pressed()
        # Game logic
        
        # Draw background
        screen.fill(green_color)

        # Game display
        # pre-shuffled deck
        deck_group.draw(screen) ## want to add in some sort of shuffle animation that goes before the player and dealer cards are dealt
        for card in player_card_group:
            if card.should_show:
                screen.blit(card.image, card.rect)
        for card in dealer_card_group:
            if card.should_show:
                screen.blit(card.image, card.rect)
        pygame.draw.rect(screen, ribbon_color, ribbon)


        pygame.display.update()
        # clock.tick(60)

        # # Game display
        # pygame.display.update()
        # clock.tick(60)
    pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()
