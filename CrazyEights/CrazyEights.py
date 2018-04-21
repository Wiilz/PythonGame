init_cards()
while not game_done:
    blocked = 0
    player_turn()
    if len(p_hand) == 0:
        game_done = True
        print
        print "You won!"
    if not game_done:
        computer_turn()
    if len(c_hand) == 0:
        game_done = True
        print
        print "Computer won!"
    if blocked >= 2:
        game_done = True
        print "Both players blocked.  GAME OVER."
