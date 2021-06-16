import random
import time
#importing need libraries

#title line
print("WELCOME TO BLACKJACK♠")
#sets default player money
playerMoney = 1000

while(playerMoney > 0):
    #variables to be reset at the starto of a new round
    dealerTotal = 0
    playerTotal = 0
    playerStand = False
    dealerStand = False
    errorCheck = True
    errorCheck2 = True
    #empty players hand
    playerHand = []
    dealerHand = []

    #sets deck array and empty lists to load player hands
    deck = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]*4
    #score values
    '''
    A -> 1,11
    J-> 10
    Q -> 10
    K -> 10

    '''
    
    #asks to place a bet then subtracts bet from playermoney
    while(errorCheck == True):
        try:
            print("Total:", playerMoney, "$")
            bet = int(input("how much would you like to bet\n"))
            if(playerMoney <= bet):
                playerMoney = 0
                print("ALL IN!")
                print("Total Is Now: 0$")
            else:
                print("Total Is Now:", playerMoney - bet)
            errorCheck = False
        except:
            print("please enter a Number between 1 and ", playerMoney)

    #shuffles deck
    random.shuffle(deck)

    #adds 2 default cards from the deck to the dealers hand
    dealerHand.append(deck[0])
    deck.remove(deck[0])

    dealerHand.append(deck[0])
    deck.remove(deck[0])
    #################################################################################Dealer Hand Logic#############################################################################################
    # prints dealer hand
    print("Dealer's Hand: ", dealerHand)

    #this function calculates the values of the dealers hand
    def dealerTotalHand():
        #makes this a global variable
        global dealerTotal
        dealerTotal = 0
        for x in dealerHand:

            #decides what to do if dealer draws an ace
            if x == "A":
                if dealerTotal >= 10:
                    dealerTotal += 11

                else:
                    dealerTotal += 1
            # decides what to do with a face card
            elif x =="K" or x =="J" or x == 'Q':
                dealerTotal += 10

            #just adds regular cards to variables
            else:
                dealerTotal += x 
        #prints the dealers total
        print("The Dealers Total Is: ", dealerTotal)
        #returns the dealer total
        return dealerTotal

    #calls dealer total to calulate the total
    dealerTotalHand()
    #then prints the total
    print("Dealer Total: ", dealerTotal )

    #decition making of the dealer
    while dealerTotal < 21 and dealerStand == False:
        time.sleep(1.5)
        print("Dealers Turn")
        time.sleep(1.5)
        if dealerTotal <= 16: # the dealer must hit while under 16 
            print("The Dealer Hit")
            time.sleep(1.5)
            dealerHand.append(deck[0])#adds card to the dealer hand array
            deck.remove(deck[0]) #removes the card added from the deck
            #then prints the dealers hand
            print("Dealers Hand: ", dealerHand)
            time.sleep(1.5)
            dealerTotalHand()
            # checks if dealer is over 21
            if dealerTotal > 21:
                print("The Dealer Busted")
                time.sleep(1.5)
                print("You Win")
                #gives you money
                playerMoney = playerMoney + bet*2 + bet
                #breaks out of the current round
                print("You Are Now At: ", playerMoney, "$")

                break

        elif dealerTotal == 17:
            hos = random.randint(1,2)
            if hos == 1:
                print("Dealer hit")
                time.sleep(1.5)
                dealerHand.append(deck[0])
                deck.remove(deck[0])
                dealerTotalHand()
                # checks if dealer is over 21
                if dealerTotal > 21:
                    print("The Dealer Busted")
                    time.sleep(1.5)
                    print("You Win")
                    #gives you money
                    playerMoney = playerMoney + bet*2 + bet
                    print("You Are Now At: ", playerMoney, "$")

                    #breaks out of the current round
                    break
            else:
                print("The Dealer Stood At 17")
                time.sleep(1.5)
        #stands if the dealer is inbetween 18 and 20
        elif dealerTotal >= 18 and dealerTotal <= 20:
            print("The Dealer Stood At ", dealerTotal)
            dealerStand = True
            time.sleep(1.5)
        #if the dealer gets black
        elif dealerTotal == 21:
            print("The Dealer Got Black Jack")

        #if the dealer busts 
        elif dealerTotal > 21:
            print("The Dealer Busted")
            time.sleep(1.5)
            print("You Win")
            playerMoney = playerMoney + bet*2 + bet
            print("You Are Now At: ", playerMoney, "$")

    #################################################################################Player Hand Logic#############################################################################################
    #adds 2 default cards to the players hand
    playerHand.append(deck[0])
    deck.remove(deck[0])

    playerHand.append(deck[0])
    deck.remove(deck[0])
    #prints the player hand
    print("Your Hand: ",playerHand)

    def totalPlayerHand():
        #this totalplayerhand function is the same as the totaldealerhand
        global playerTotal
        playerTotal = 0
        for x in playerHand:

            if x == "A":
                if playerTotal >= 10:
                    playerTotal += 11
                else:
                    playerTotal += 1
            
            elif x =="K" or x =="J" or x == 'Q':
                playerTotal += 10

            else:
                playerTotal += x 
        return playerTotal

    totalPlayerHand()
    print("Your Total: ", playerTotal)

    while(playerTotal < 21 and playerStand == False):
            while errorCheck2 == True:
                try:
                    #gives the user to option to hit or stand
                    print("press 1 to hit")
                    print("press 2 to Stand")
                    playerAction = int(input("Action to preform:\n"))
                    if playerAction == 1:
                        #if the player hit
                        playerHand.append(deck[0])#add a card
                        deck.remove(deck[0])#remove cards from deck
                        playermoney = playerMoney + bet*2 + bet #adds money
                        print(playerHand)
                        totalPlayerHand()
                        print("Your Total is now",playerTotal)
                        #checks if you busted
                        if playerTotal > 21:
                            print("You Busted!")
                            print("Dealer Wins!")
                            break
                        errorCheck2 = False

                    elif playerAction == 2:
                        if(dealerTotal > playerTotal and dealerTotal >= 21):
                            #checks when you stand and compares your scode to the dealers
                            print("You Lose")
                            #adds money and sets player stant to true to pull it out of loop
                            playerMoney = playerMoney - bet
                            playerStand = True
                            print("You Stood With: ", playerHand)
                        errorCheck2 = False
                        #sets error to false so it oulls out of loop
                        break
                    else:
                        #loops it if the user inputs a number larger than 2
                        errorCheck2 = True
                        print("Please enter an number between 1 and 2")
                except:
                    #catches the users input and runs loops the code a prints the error msg
                    print("Please enter 1 or 2")
                    errorCheck2 = True
