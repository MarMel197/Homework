class Game:
    
    def who_won(player1, player2):
        if player1.selection == player2.selection:
            return None
        elif player1.selection == 'rock' and player2.selection == 'paper':
            return 'Player 2 wins'
        elif player1.selection == 'rock' and player2.selection == 'scissors':
            return 'Player 1 wins'
        elif player1.selection == 'paper' and player2.selection == 'rock':
            return 'Player 1 wins'
        elif player1.selection == 'paper' and player2.selection == 'scissors':
            return 'Player 2 wins'
        elif player1.selection == 'scissors' and player2.selection == 'rock':
            return 'Player 2 wins'
        elif player1.selection == 'scissors' and player2.selection == 'paper':
            return 'Player 1 wins'
        else:
            return 'Error'