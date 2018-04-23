#主循环体

init_cards()
while not game_done:
    blocked = 0
    player_turn()    #轮到玩家
    if len(p_hand) == 0:
        game_done = True
        print
        print "You won!"
    if not game_done:
        computer_turn()    #轮到计算机
    if len(c_hand) == 0:
        game_done = True
        print
        print "Computer won!"
    if blocked >= 2:     #双方都无法继续，所以游戏结束
        game_done = True
        print "Both players blocked.  GAME OVER."

#显示玩家手中的牌
print "\nYour hand: ",
for card in p_hand:
    print card.short_name,
print "    Up card: ", up_card.short_name
if up_card.rank == '8':
    print"    Suit is", active_suit

#得到玩家的选择
print "What would you like to do? ",
response = raw_input("Type a card to play or 'Draw' to take a card: ")
valid_play = False
while not valid_play:   #不断尝试直到玩家输入合法的内容
    selected_card = None
    while selected_card == None:
        if response.lower() == 'draw':
            valid_play = True
            if len(deck) > 0:       #如果抽牌，从这副牌中取牌，并增加到玩家手中
                card = random.choice(deck)
                p_hand.append(card)
                deck.remove(card)
                print "You drew", card.short_name
            else:
                print "There are no cards left in the deck"
                blocked += 1
            return   #已经抽牌，所以回到主循环
        else:
            for card in p_hand:
                if response.upper() == card.short_name:
                    selected_card = card
            if selected_card == None:
                response = raw_input("You don't have that card. Try again:")

    if selected_card.rank == '8':     #出8总是合法的
        valid_play = True
        is_eight = True
    elif selected_card.suit == active_suit:    #检查选择的牌是否与明牌花色一致
        valid_play = True
    elif selected_card.rank == up_card.rank:   #检查选择的牌是否与明牌点数一致
        valid_play = True

    if not valid_play:
        response = raw_input("That's not a legal play.  Try again: ")

    p_hand.remove(selected_card)
    up_card  = selected_card
    active_suit = up_card.suit
    print "You played", selected_card.short_name
    if is_eight:
        get_new_suit()
        
# 玩家出一张8时得到新花色
