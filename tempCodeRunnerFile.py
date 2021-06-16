if dealerTotal > 21:
                print("The Dealer Busted")
                time.sleep(1.5)
                print("You Win")
                #gives you money
                playerMoney = playerMoney + bet
                #breaks out of the current round
                print("You Are Now At: ", playerMoney, "$")
                break