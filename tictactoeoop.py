class Tictactoe():
    def __init__(self):
        self.player = "X"
        print(self.player)
        self.board = ['_','_','_',
                      '_','_','_',
                      '_','_','_']

    def showboard(self):
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])

    def get_user_input(self):
        position = input(f"Enter position from 1 to 9:\n{self.player}'s Turn\n")
        print()
        if not position.isdigit():
            return True
        position = int(position)
        if position<0 or position>9:
            print("Plase enter number between 1 to 9: ")
            return True
        self.board[position-1] = self.player
    

    def check_win(self):
        if self.board[0] == self.board[1] == self.board[2] != "_":
            return True
        if self.board[3] == self.board[4] == self.board[5] != "_":
           return True
        if self.board[6] == self.board[7] == self.board[8] != "_":
           return True
        if self.board[0] == self.board[3] == self.board[6] != "_":
            return True
        if self.board[1] == self.board[4] == self.board[7] != "_":
            return True
        if self.board[2] == self.board[5] == self.board[8] != "_":
            return True
        if self.board[0] == self.board[4] == self.board[8] != "_":
            return True
        if self.board[6] == self.board[4] == self.board[2] != "_":
            return True
    
    def check_draw(self):
        if '_' not in self.board:
            return True
    
    def flip(self):
        if self.player == "X":
            self.player = 'O'
        else:
            self.player = 'X'
        
G = Tictactoe()
while True:
    if G.get_user_input():
        print("The input should be integer\nIt should contain number between 1 to 9")
        continue
    G.showboard()
    if G.check_draw():
        print("Draw")
        break
    win_check = G.check_win()
    if win_check:
        print(f'{G.player} Won')
        break
    G.flip()
